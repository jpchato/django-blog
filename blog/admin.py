from django.contrib import admin
from blog.models import Post

# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    pass 

admin.site.register(Post, ProjectAdmin)