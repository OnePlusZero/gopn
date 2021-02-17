from django.contrib import admin
from .models import Post, NewsList
# Register your models here.



@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')

@admin.register(NewsList)

class NewsListAdmin(admin.ModelAdmin):
    list_display = ('title','created_date')