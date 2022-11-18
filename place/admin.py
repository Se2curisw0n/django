from django.contrib import admin
from .models import Restaurant, Menu,Store,Store_menu
# Register your models here.


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['res_name']

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Menu)
admin.site.register(Store)
admin.site.register(Store_menu)
