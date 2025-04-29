from django.contrib import admin
from .models import Blog, Comment

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'reading_time')
    search_fields = ('title', 'description')
    list_filter = ('created_date',)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'content')
    search_fields = ('content',)
    list_filter = ('timestamp',)