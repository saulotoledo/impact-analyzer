from django.db import models
from . import Table
from tags.models import Tag

class TableEntry(models.Model):
    """
    Represents an entry in a table. Many table entries form a table.

    Attributes:
        table (ForeignKey): References the table the current entry belongs to.
        line (int): An identifier for the line in the table. There should not be more than 1 item with the same column and line.
        column (int): The id of the column in the table. There should not be more than 1 item with the same column and line.
        value (str): The value of the column.
        tags (ManyToManyField): The tags attached to the value of this entry.
    """

    table = models.ForeignKey(Table, on_delete=models.CASCADE)
    line = models.IntegerField()
    column = models.IntegerField()
    value = models.TextField()
    tags = models.ManyToManyField(to='tags.Tag', related_name='table_entry', blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                'line',
                'column',
                'table_id',
                name='line_column_unique',
            ),
        ]
