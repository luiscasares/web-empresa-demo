from django.contrib import admin
from .models import Service

# Register your models here.
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_filter = ('title',)
    readonly_fields=('created', 'updated')
    fieldsets =(
        ('Servicio',{
            'classes': ('collapse',),
            'fields':('title','subtitle','content', 'image')
        }),
        ('Cronología', {
            'classes':('collapse',),
            'fields': ('created','updated')
        }),
    )


admin.site.register(Service, ServicesAdmin)
