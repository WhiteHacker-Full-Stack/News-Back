from django.contrib import admin
from django.utils.text import slugify

from blog.models import Category, Tags, News, BreakingNews, Newslatter, Flickr, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Newslatter)
admin.site.register(Flickr)
admin.site.register(Comment)


class NewsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
class BreakingAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
admin.site.register(News, NewsAdmin)
admin.site.register(BreakingNews, BreakingAdmin)
