from django.contrib import admin
from .models import ProcessCatalogue,ProcessGroup

# Register your models here.

class ProcessCatalogueAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)
class ProcessGroupAdmin(admin.ModelAdmin):
    readonly_fields=('created_at','updated_at',)

admin.site.register(ProcessCatalogue,ProcessCatalogueAdmin)
admin.site.register(ProcessGroup,ProcessGroupAdmin)