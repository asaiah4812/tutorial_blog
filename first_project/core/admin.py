from django.contrib import admin
from .models import Post, Category

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('name', 'created_at' )
    prepopulate_field = {'slug': ('name',)}

admin.site.register(Category)
