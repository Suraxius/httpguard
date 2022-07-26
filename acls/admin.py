from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(SourceIP)
admin.site.register(DestinationDomain)
admin.site.register(DestinationPort)
admin.site.register(Method)