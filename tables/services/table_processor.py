import csv
import time
from django.db import transaction
from tables.models import Table, TableEntry

class TableProcessorService:
    def __init__(self, table_processing_batch_size):
        self.table_processing_batch_size = table_processing_batch_size

    def parse_csv_table(self, file_name, uploaded_file):
        """
        Parses a table in the CSV format, returning a list of dictionaries representing the data.
        Assumes the first line contains the column names.

        Parse a CSV file and return a list of dictionaries, with each dictionary
        representing a row in the CSV file. The keys of each dictionary correspond
        to the column names in the CSV file.

        :param file: A file object representing the CSV file.
        :param file_name: The name of the file.
        :return: A list of dictionaries representing the parsed rows.
        """

        csv_content = uploaded_file.read().decode('utf-8').splitlines()
        csv_table = csv.DictReader(csv_content, delimiter=',', quotechar='"')
        column_names = csv_table.fieldnames
        rows = list(csv_table)

        table = self._create_table(file_name, column_names)
        rows = self._prepare_entries(table, column_names, rows)

        try:
            with transaction.atomic():
                TableEntry.objects.bulk_create(rows, batch_size=self.table_processing_batch_size)
        except Exception as e:
            # TODO: Consider moving the table to the transaction instead of manually triggering the delete below
            # If the delete fail we will end with inconsistency in the database
            table.delete()
            return []

        return rows

    def _create_table(self, file_name, column_names) -> Table:
        # We append a timestamp to the dataset name for illustration purposes:
        upload_timestamp = int(time.time())
        dataset_name = "%s_%s" % (upload_timestamp, file_name)

        return Table.objects.create(name=dataset_name, columns=column_names)

    def _prepare_entries(self, table: Table, columns, rows):
        prepared_rows = []

        # This should be a background job due to resource usage,
        # but I am doing it here just as an example:
        for row_num, row in enumerate(rows):
            for col_num, col_name in enumerate(columns):
                new_entry = TableEntry(
                    table=table,
                    line=row_num,
                    column=col_num,
                    value=row[col_name],
                )

                prepared_rows.append(new_entry)

        return prepared_rows
