from django.contrib import admin
from .models import Service


class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ['creado','update']


admin.site.register(Service,ServiceAdmin)
# Register your models here.
