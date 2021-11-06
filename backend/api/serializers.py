from rest_framework import serializers

from . import models


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Image
        fields = ('id', 'url')


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.File
        fields = ('id', 'url', 'size')


class BlogTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.BlogTag
        fields = ('id', 'name')


class BlogArticleSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = models.BlogArticle
        fields = ('id', 'date', 'title', 'text', 'tags', 'image', 'image_url',
                  'preview_text')

    def get_image_url(self, instance):
        return instance.image.url if instance.image is not None else None

    def get_fields(self, *args, **kwargs):
        """
        Custom get_fields method to remove 'text' field in case of list
        representation (for traffic optimization).
        """
        fields = super().get_fields(*args, **kwargs)
        request = self.context.get('request')
        if request is not None and not request.parser_context.get('kwargs'):
            fields.pop('text', None)
        return fields


class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField('get_image_url')

    class Meta:
        model = models.Project
        fields = ('id', 'title', 'description', 'image', 'image_url', 'source',
                  'article', 'website', 'downloads')

    def get_image_url(self, instance):
        return instance.image.url if instance.image is not None else None


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Contact
        fields = ('id', 'name', 'value', 'url', 'icon')
