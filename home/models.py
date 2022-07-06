# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Notes(models.Model):
    title = models.TextField(unique=True)
    date = models.BinaryField()
    note = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'notes'


class Quotes(models.Model):
    quote = models.TextField(unique=True, blank=True, null=True)
    author = models.TextField(blank=True, null=True)
    genre = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quotes'


class Snippet(models.Model):
    title = models.CharField(max_length=255, unique=True)
    code = models.TextField(unique=True)
    date = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'snippet'

    def __str__(self):
        return self.title


class Theme(models.Model):
    color = models.TextField(unique=True, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'theme'
