from django.db import models


class Benefactor(models.Model):
    name = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Trip(models.Model):
    origin = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    start = models.CharField(max_length=100, null=False)
    end = models.CharField(max_length=100, null=False)
    benefactor = models.CharField(max_length=100, null=False)

    def __str__(self):
        return f'{self.origin} ({self.start}) --> {self.destination} ({self.end})'


class Cost(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=200, null=False)
    where = models.CharField(max_length=100, null=False)
    when = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    trip = models.CharField(max_length=100, null=False)
    receipt = models.ImageField(
        upload_to='receipts/', default='receipts/default.png')

    def __str__(self):
        return self.name
