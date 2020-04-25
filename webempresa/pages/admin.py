from django.contrib import admin
from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    readonly_fields = ['creado','update']
    list_display = ['title','order']


admin.site.register(Pages,PagesAdmin)
# Register your models here.
