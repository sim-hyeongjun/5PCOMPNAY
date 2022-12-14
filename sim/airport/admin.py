from django.contrib import admin
from airport.models import airport
# Register your models here.

@admin.register(airport)
class airportAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','modify_dt', 'tag_list')
    list_fiter = ('modify_dt',)
    search_fields =('title','content')
    prepopulated_fields = {'slug': ('title',)}

    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())