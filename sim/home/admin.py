from django.contrib import admin

from home.models import town, home

# Register your models here.
class homeInline(admin.StackedInline):
    model = home
    extra =2

@admin.register(town)
class townAdmin(admin.ModelAdmin):
    inlines =(homeInline,)
    list_display = ('id','name','description')
@admin.register(home)
class homeAdmin(admin.ModelAdmin):
    list_display = ('id','title','upload_dt')
    