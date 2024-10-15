from django.contrib import admin
from .models import Car
from django.utils.html import format_html


class CarAdmin(admin.ModelAdmin):
    def image_tag(self, obj):
        return format_html('<img src="{}"width="40" style="border-radius:50px;"/>'.format(obj.car_photo.url))

    list_display=('title','model','image_tag','price','is_features')
    list_display_links=('title','image_tag')
    search_fields=('title','model','price')
    list_filter=('title','price')
    list_editable=('is_features',)

admin.site.register(Car,CarAdmin)
# admin.site.register(Car)


