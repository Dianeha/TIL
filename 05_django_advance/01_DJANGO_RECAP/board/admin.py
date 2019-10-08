from django.contrib import admin
from .models import Article
# Register your models here.

class ArticleModelAdmin(admin.ModelAdmin):
    list_display = 'id', 'title'

admin.site.register(Article, ArticleModelAdmin)