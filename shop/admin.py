from django.contrib import admin

from .models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'uploaded_at')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Product)
