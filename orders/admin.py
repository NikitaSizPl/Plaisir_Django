from django.contrib import admin
from .models import OrderItem, Order

# Register your models here


class OrderItemInline(admin.TabularInline):  # Define inline for OrderItem
    model = OrderItem
    raw_id_fields = ['order', 'product']  # Optional: Use raw_id_fields to show a raw input for the ForeignKey (Product)

class OrderAdmin(admin.ModelAdmin):  # Customize OrderAdmin
    list_display = ['id', 'user']
    inlines = [OrderItemInline]  # Include OrderItem inline in the OrderAdmin

# Register models in admin site
admin.site.register(Order, OrderAdmin)  # Register Order with the customized admin
admin.site.register(OrderItem)