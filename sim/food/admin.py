

# Register your models here.
from django.contrib import admin

from food.models import zip, food

# Register your models here.
class foodInline(admin.StackedInline):
    model = food
    extra =2

@admin.register(zip)
class zipAdmin(admin.ModelAdmin):
    inlines =(foodInline,)
    list_display = ('id','name','description')
@admin.register(food)
class foodAdmin(admin.ModelAdmin):
    list_display = ('id','title','upload_dt')