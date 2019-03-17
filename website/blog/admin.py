from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    """
    How to display Post elements in administration interface
    """

    # displayed fields
    list_display = ('title', 'slug', 'author', 'publish',
                    'status')

    # to filter results
    list_filter = ('status', 'created', 'publish', 'author')

    # searchable fields
    search_fields = ('title', 'body')

    # initialize slug with title
    prepopulated_fields = {'slug': ('title',)}

    # to display author with ga lookup widget
    raw_id_fields = ('author',)

    # to nagivate using date hierarchy
    date_hierarchy = 'publish'

    # post are ordered by author and publication date
    ordering = ['status', 'publish']


admin.site.register(Post, PostAdmin)
