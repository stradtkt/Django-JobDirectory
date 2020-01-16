from django.contrib import admin

from .models import Directory, Applied

class DirectoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'logo', 'salary', 'developer_level', 'duration')
    list_display_links = ('id', 'title', 'logo')
    list_filter = ('skills',)
    list_editable = ('developer_level', 'duration')
    search_fields = ('title', 'description', 'location', 'developer_level', 'duration')

admin.site.register(Directory, DirectoryAdmin)

class AppliedAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'directory', 'created')
    list_display_links = ('id',)
    list_filter = ('user','directory')
    search_fields = ('user', 'directory', 'created')

admin.site.register(Applied, AppliedAdmin)

