from django.db import models


class Benefactor(models.Model):
    name = models.CharField(max_length=100, null=False)
    role = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.name


class Trip(models.Model):
    origin = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    start = models.DateTimeField(auto_now_add=False, blank=False)
    end = models.DateTimeField(auto_now_add=False, blank=False)
    benefactor = models.ForeignKey(
        'Benefactor', on_delete=models.CASCADE, null=False, related_name='trip'
    )

    def __str__(self):
        return f'{self.origin} ({self.start}) --> {self.destination} ({self.end})'  # noqa: E501


class Cost(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=200, null=False)
    where = models.CharField(max_length=100, null=False)
    when = models.DateTimeField(auto_now_add=False, blank=False)
    category = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    trip = models.ForeignKey(
        'Trip', on_delete=models.CASCADE, null=False, related_name='cost'
    )

    def __str__(self):
        return self.name
