from django.contrib import admin
from .models import Contact
from django.utils.html import format_html
# Register your models here.

# class TeamAdmin(admin.ModelAdmin):
#     def image_tag(self, obj):
#         return format_html('<img src="{}"width="40" style="border-radius:50px;"/>'.format(obj.phtoto.url))

#     list_display=('id','first_name','designation','image_tag','create_date')
#     list_display_links=('id','first_name','image_tag')
#     search_fields=('first_name','designation','last_name')
#     list_filter=('designation','create_date')

admin.site.register(Contact)
