from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(certificates)

@admin.register(certificates)
class CertAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}