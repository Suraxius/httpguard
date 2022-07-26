from django.db import models

from acls.models import *

# Create your models here.
class Rule(models.Model):
    sourceIPs          = models.ManyToManyField(SourceIP, blank=False, name="Source IP")
    destinationDomains = models.ManyToManyField(DestinationDomain, blank=False, name="Destination Domains")
    destinationPorts   = models.ManyToManyField(DestinationPort, blank=False, name="Destination Ports")
    method             = models.ManyToManyField(Method, blank=False, name="HTTP Methods")
    author             = models.ForeignKey(User, null=False, blank=False, default=1, on_delete=models.PROTECT, editable=False)
    updated_on         = models.DateTimeField(auto_now=True, null=False, blank=True)
    created_on         = models.DateTimeField(auto_now_add=True, blank=True)

