import datetime
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.

class SourceIP(models.Model):
    address    = models.GenericIPAddressField(null=False, blank=False)
    subnet     = models.CharField(max_length=3, null=False, blank=False)
    author     = models.ForeignKey(User, null=False, blank=False, default=1, on_delete=models.PROTECT, editable=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.address + '/' + self.subnet


class DestinationDomain(models.Model):
    domain     = models.CharField(null=False, blank=False,max_length=255)
    author     = models.ForeignKey(User, null=False, blank=False, default=1, on_delete=models.PROTECT, editable=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.domain

class DestinationPort(models.Model):
    port       = models.IntegerField(null=False, blank=False, validators=[
            MinValueValidator(1),
            MaxValueValidator(65536)
        ])
    author     = models.ForeignKey(User, null=False, blank=False, default=1, on_delete=models.PROTECT, editable=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return str(self.port)

class Method(models.Model):
    method     = models.CharField(null=False, blank=False,max_length=20)
    author     = models.ForeignKey(User, null=False, blank=False, default=1, on_delete=models.PROTECT, editable=False)
    updated_on = models.DateTimeField(auto_now=True, null=False, blank=True)
    created_on = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return self.method  


