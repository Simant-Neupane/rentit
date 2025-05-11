from django.contrib import admin
from .models import Category, PerportyType, Property, PropertyImage

# Keep these registrations
admin.site.register(Category)
admin.site.register(PerportyType)

# Create inline for multiple images
class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1
    max_num = 5
    fields = ['image']

# Custom admin for Property to include images
@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    inlines = [PropertyImageInline]
    list_display = ['title', 'category', 'price', 'location']