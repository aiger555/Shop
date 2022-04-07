from django.contrib import admin
from .models import Order, OrderItem


admin.site.register(OrderItem)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'phone', 'last_name', 'email')
    list_filter = ('first_name', 'phone', 'last_name', 'email')
    search_fields = ('first_name', 'phone', 'last_name', 'email')



