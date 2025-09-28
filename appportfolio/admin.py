from django.contrib import admin

# Register your models here.

from .models import Project, CustomUser


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Admin View for Project'''

    list_display = ('first_name', 'last_name', 'email', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('first_name', 'last_name', 'email', 'message')

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    '''Admin View for CustomUser'''

    list_display = ('email', 'username', 'first_name', 'last_name', 'is_active', 'is_staff')
    list_filter = ('is_active', 'is_staff', 'is_superuser', 'date_joined')
   
   
    search_fields = ('email', 'username', 'first_name', 'last_name')
    date_hierarchy = 'date_joined'
    ordering = ('email',)