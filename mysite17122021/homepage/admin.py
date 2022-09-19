from django.contrib import admin

# Register your models here.

from .models import Car


class CarAdmin(admin.ModelAdmin):
  list_display = ('id', 'brend', 'color', 'content', 'photo', 'times_create', 'times_update', 'is_published')
  list_display_links = ('id', 'brend')
  search_fields = ('brend', 'content')



admin.site.register(Car, CarAdmin)