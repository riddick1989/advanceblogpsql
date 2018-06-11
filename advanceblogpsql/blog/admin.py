from django.contrib import admin
from .models import Post
# Register your models here.



class Listdisplay(admin.ModelAdmin):
    list_display = ["title","timestamp","updated"]
    list_editable = ["title"]
    list_display_links = ["timestamp"]
    list_per_page = 15
    list_filter = ["title"]
    search_fields = ["title"]
    prepopulated_fields = {"slug":("title",)}

    class META :
        models = Post


admin.site.register(Post,Listdisplay)