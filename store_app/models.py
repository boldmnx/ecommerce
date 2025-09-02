from django.db import models


class Baraa(models.Model):
    ner = models.CharField(max_length=100)
    une = models.DecimalField(max_digits=10, decimal_places=2)
    too = models.IntegerField()


    class Meta:
        db_table = 'baraa_tbl'
    def __str__(self):
        return self.ner
