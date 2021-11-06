from django.contrib import admin

from . import models


@admin.register(models.Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('url', 'image_tag')
    readonly_fields = ('image_tag',)


@admin.register(models.File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('url', 'is_hidden', 'order')


@admin.register(models.BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')


@admin.register(models.BlogArticle)
class BlogArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'image', 'is_hidden')


@admin.register(models.Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'image', 'source', 'article', 'website',
                    'is_hidden', 'order')


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'url', 'icon', 'order')


@admin.register(models.Secret)
class SecretAdmin(admin.ModelAdmin):
    list_display = ('key', 'created_at', 'expires_at', 'is_expired')
    fields = ('expires_at', 'allowed_files')
