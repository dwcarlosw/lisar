from django.contrib import admin

class BaseModelAdmin(admin.ModelAdmin):
    actions_on_bottom = True
    save_as = True
    save_on_top = True
    search_fields = ['created_by']
    list_display = ['created_by']
    list_select_related = True
    readonly_fields = ['created_by', 'updated_by', 'created', 'updated', ]

    def save_model(self, request, obj, form, change):
        obj.updated_by = request.user
        if not change:
            obj.created_by = request.user
        obj.save()