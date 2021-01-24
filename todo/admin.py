from django.contrib import admin
from . import models
# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Status)
class StatusAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Tag)
class TagAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Confidentioal)
class ConfidentioalAdmin(admin.ModelAdmin):
    pass
@admin.register(models.Todo)
class TodoAdmin(admin.ModelAdmin):
    pass
