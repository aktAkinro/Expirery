from django.contrib import admin
from .models import Drug, DrugBatch, Alert


# Register your models here.
admin.site.register(Drug)
admin.site.register(DrugBatch)

