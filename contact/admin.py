from django.contrib import admin
from contact import models
# Register your models here.

@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # configuração do seu model no admin do django
    list_display = ('id', 'first_name', 'last_name', 'phone', 'show', )
    ordering = ('-id',) # menos faz com que fique id de forma decrescente
    # list_filter = ('created_date',)
    search_fields = ('first_name', 'last_name') 
    list_per_page = 5 
    list_max_show_all = 200 
    # list_editable = ('first_name', 'last_name')
    list_display_links = ('first_name',)
    

@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    # configuração do seu model no admin do django
    list_display = ('name', )
    ordering = ('-id',) # menos faz com que fique id de forma decrescente