from django.contrib import admin
from .models import Listing
# Register your models here.
class ListAdmin(admin.ModelAdmin):
    list_display=('id','title','is_published','price','realtors')
    list_display_links=('id','title')
    search_fileds=('name',)
    list_filter=('realtors',)


admin.site.register(Listing,ListAdmin)