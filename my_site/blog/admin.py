from django.contrib import admin
from .models import Author,Tag,Post
# Register your models here.
class Filter(admin.ModelAdmin):
    list_filter = ("author", "tag", "date")
    list_display = ("title", "date", "author")
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Post,Filter)
admin.site.register(Author)
admin.site.register(Tag)

