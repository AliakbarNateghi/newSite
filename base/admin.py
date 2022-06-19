from django.contrib import admin

from .models import pro


class proAdmin(admin.ModelAdmin):
    list_display = ['name', 'kind', 'description', 'price', 'image', 'available']


admin.site.register(pro, proAdmin)
