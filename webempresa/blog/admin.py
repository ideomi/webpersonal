from django.contrib import admin
from .models import Categori, Post


class CategoriAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ['created','updated']
    list_display = ['title','published','autor','post_cat']
    search_fields = ['title','autor__username']
    date_hierarchy = 'published'
    list_filter = ['autor__username','categori__name']

    def post_cat(self,obj):
        return ','.join([c.name for c in obj.categori.all()])

    post_cat.short_description = 'Categoría'


admin.site.register(Categori,CategoriAdmin)
admin.site.register(Post,PostAdmin)
# Register your models here.
