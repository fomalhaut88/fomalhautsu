import re

from django.db import models
from django.utils import timezone
from django.utils.html import mark_safe
from django.utils.crypto import get_random_string


SECRET_LENGTH = 8


class Image(models.Model):
    image = models.ImageField(upload_to='images', db_index=True)

    def __str__(self):
        return self.image.name

    @property
    def url(self):
        return self.image.url

    def image_tag(self):
        return mark_safe('<img src="{}" height="150px">'.format(self.url))

    image_tag.short_description = "Изображение"
    image_tag.allow_tags = True


class File(models.Model):
    file = models.FileField(upload_to='files', db_index=True)
    is_hidden = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.file.name

    @property
    def url(self):
        return self.file.url

    @property
    def size(self):
        return self.file.size


class BlogTag(models.Model):
    name = models.CharField(max_length=250)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name


class BlogArticle(models.Model):
    date = models.DateField()
    title = models.CharField(max_length=1000)
    text = models.TextField()
    tags = models.ManyToManyField('BlogTag', blank=True)
    image = models.ForeignKey('Image', on_delete=models.SET_NULL,
                              null=True, default=None, blank=True)
    is_hidden = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date',)

    def __str__(self):
        return self.title

    @property
    def preview_text(self):
        return self._remove_markdown_specs(self.text)[:300]

    def _remove_markdown_specs(self, text):
        text = re.sub(r"[\*\_\'\`\#\~]+", "", text)
        text = re.sub(r"\!\[.*?\]\(.*?\)", "", text)
        text = re.sub(r"\[.*?\]\((.*?)\)", "\1", text)
        return text


class Project(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ForeignKey('Image', on_delete=models.SET_NULL,
                              null=True, default=None, blank=True)
    source = models.URLField(null=True, default=None, blank=True)
    article = models.ForeignKey('BlogArticle', on_delete=models.SET_NULL,
                                null=True, default=None, blank=True)
    website = models.URLField(null=True, default=None, blank=True)
    downloads = models.ManyToManyField('File', blank=True)
    is_hidden = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=100)
    value = models.CharField(max_length=1000)
    url = models.CharField(max_length=1000)
    icon = models.CharField(max_length=100,
                            null=True, default=None, blank=True)
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ('order',)

    def __str__(self):
        return self.name


class Secret(models.Model):
    key = models.CharField(max_length=SECRET_LENGTH, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expires_at = models.DateTimeField()
    allowed_files = models.ManyToManyField('File', blank=True)

    def __str__(self):
        return self.key

    @property
    def is_expired(self):
        return timezone.now() > self.expires_at

    def save(self, **kwargs):
        if self.pk is None:
            assert not self.key, "Secret key must be empty on create"
            self.key = get_random_string(length=SECRET_LENGTH)
        super().save(**kwargs)
