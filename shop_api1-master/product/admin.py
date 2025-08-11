from django.contrib import admin

from .models import Product, Category

@admin.register(Product)
class RroductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'price']
    list_filter = ['customer__username', 'customer__email', 'category__title']
    search_fields = ['title']
    exclude = ['image']
    ordering = ['price']

    # def has_delete_permission(self, request, obj = ...):
    #     return request.user == obj.customer
    
    # def has_add_permission(self, request):
    #     return False
    
    # def has_change_permission(self, request, obj = ...):
    #     return request.user == obj.customer
admin.site.register(Category)
