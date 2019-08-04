from django.contrib import admin

from .models import Realtor
# Register your models here.
class RealtorAdmin(admin.ModelAdmin):
    list_display=('name','phone','email','is_mvp')
    list_display_links=('name','email')
    search_fields=('name',)
admin.site.register(Realtor,RealtorAdmin)
