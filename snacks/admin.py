from django.contrib import admin
from .models import Snack

@admin.register(Snack)
class SnackAdmin(admin.ModelAdmin):
    list_display = ('name', 'purchaser', 'description_short')
    search_fields = ['name', 'purchaser__username'] 
    list_filter = ('purchaser',)

    def description_short(self, obj):
        """Create a shortened version of the description for display."""
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description
    description_short.short_description = 'Short Description'