from django.contrib import admin
from django.contrib.contenttypes import generic

class BaseModelAdmin(admin.ModelAdmin):
    actions_on_bottom = True 
    save_as = True
    save_on_top = True
    search_fields = ['name']
    list_display = ['name']
    list_select_related = True
    readonly_fields = ['created_by', 'updated_by', 'created', 'updated', ]

    def save_model(self, request, obj, form, change):        
        obj.updated_by = request.user
        if not change:
            obj.created_by = request.user
        obj.save()

class BaseGenericTabularInline(generic.GenericTabularInline):
    readonly_fields = ['created_by', 'updated_by',]
    exclude = ['slug', 'name', 'order', 'parent',]
    extra = 1

class BaseTabularInline(admin.TabularInline):
    readonly_fields = ['created_by', 'updated_by',]
    exclude = ['slug', 'name', 'order', 'parent',]
    extra = 1