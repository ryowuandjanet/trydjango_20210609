from django.contrib import admin
from .models import *
 
class PostModelAdmin(admin.ModelAdmin):
  list_display=["title","updated","timestamp"]
  list_display_links=["updated"]
  list_filter=["updated","timestamp"]
  list_editable=["title"]
  search_fields=["title","content"]

  class Meta:
    model=Post

admin.site.register(Post,PostModelAdmin)
admin.site.register(Land)

