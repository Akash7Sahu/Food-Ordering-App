from django.contrib import admin
from zappyapp.models import Item,Cart

class ItemAdmin(admin.ModelAdmin):
    list_display=['iname','id','price','description']
    search_fields=['iname','category']
    list_filter=['category','price']
    list_editable=['price','description']


admin.site.register(Item,ItemAdmin)# Register your models here.

class CartAdmin(admin.ModelAdmin):
    list_display=['name','price','user']

admin.site.register(Cart,CartAdmin)
