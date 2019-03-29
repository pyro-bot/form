from django.contrib import admin
from form.models import Context, Intent, TrainExample


admin.site.register(Context)
admin.site.register(Intent)

@admin.register(TrainExample)
class ExampleAdmin(admin.ModelAdmin):
    list_filter = ('intent', 'intent__context')
    list_display = ('intent', 'example')
    search_fields = ('example',)

    def intent__context(self, obj):
        return obj.intent.context
