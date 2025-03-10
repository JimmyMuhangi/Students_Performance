"""
This module defines the database models for the Students app.
"""

# Create your models here.
from django.db import models


class Student(models.Model):
    """Model representing a student and their academic records."""
    name = models.CharField(max_length=100)
    index_number = models.CharField(max_length=20, unique=True)
    mid_term = models.IntegerField()
    end_term = models.IntegerField()
    total = models.IntegerField(editable=False)
    percentage = models.FloatField(editable=False)

    def save(self, *args, **kwargs):
        # Automatically calculate total and percentage before saving
        self.total = self.mid_term + self.end_term
        self.percentage = (self.total / 200) * 100
        super().save(*args, **kwargs)

    def __str__(self):
        """Returns a string representation of the student."""
        return self.name
    