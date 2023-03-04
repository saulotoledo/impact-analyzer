from django.contrib.postgres.fields import ArrayField
from django.db import models

class Table(models.Model):
    """
    Represents an entry in a table. Many table entries form a table.

    Attributes:
        name (str): The name of the table.
        columns (ArrayField): The columns of the field.
    """

    name = models.CharField(max_length=255)
    columns = ArrayField(
        models.CharField(max_length=150, blank=True),
    )
