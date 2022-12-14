from django.contrib import admin

# Register your models here.
class PlaceInline(admin.StackedInline):
    model = place
    extra = 2