from django.contrib import admin
from .models import MenuItem, Category

class MenuItemAdmin(admin.ModelAdmin):
    """Настройки административного интерфейса для модели MenuItem."""
    list_display = ('name', 'description', 'price', 'category', 'image', 'slug')
    list_filter = ('category', 'price')
    search_fields = ('name', 'description')
    prepopulated_fields = {'slug': ('name',)}  # Автоматическое заполнение поля slug

admin.site.register(MenuItem, MenuItemAdmin)
admin.site.register(Category)  # Регистрация категории
