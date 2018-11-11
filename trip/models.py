from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Benefactor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, default=1)
    role = models.CharField(max_length=100, null=False)
    admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Benefactor.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
	try:
		instance.benefactor.save()
	except:
		benefactor = Benefactor.objects.create(user=instance)	
		benefactor.save()


class Trip(models.Model):
    name = models.CharField(max_length=100, null=False)
    origin = models.CharField(max_length=100, null=False)
    destination = models.CharField(max_length=100, null=False)
    start = models.CharField(max_length=100, null=False)
    end = models.CharField(max_length=100, null=False)
    benefactor = models.ForeignKey('Benefactor', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Cost(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(max_length=200, null=False)
    where = models.CharField(max_length=100, null=False)
    when = models.CharField(max_length=100, null=False)
    category = models.CharField(max_length=100, null=False)
    value = models.CharField(max_length=100, null=False)
    trip = models.ForeignKey('Trip', on_delete=models.CASCADE)
    receipt = models.ImageField(
        upload_to='receipts/', default='receipts/default.png')

    def __str__(self):
        return self.name
