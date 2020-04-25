from django.contrib import admin
from .models import Link


class LinkAdmin(admin.ModelAdmin):
    #readonly_fields = ['creado','update']

    def get_readonly_fields(self, request, obj=None):

        if request.user.groups.filter(name='autogestion').exists():
            return  ['creado','update','key','name']
        else:
            return ['creado', 'update']



admin.site.register(Link,LinkAdmin)
# Register your models here.
