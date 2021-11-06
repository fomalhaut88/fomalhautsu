from rest_framework.viewsets import ReadOnlyModelViewSet

from . import models, serializers


class ImageViewSet(ReadOnlyModelViewSet):
    queryset = models.Image.objects.all()
    serializer_class = serializers.ImageSerializer


class FileViewSet(ReadOnlyModelViewSet):
    queryset = models.File.objects.none()
    serializer_class = serializers.FileSerializer

    def get_queryset(self):
        if self.request.user.is_superuser:
            # Show all files for superuser
            return models.File.objects.all()
        else:
            # Show all not hidden files and
            # the ones allowed by the given secret.
            secret_key = self.request.GET.get('secret', '')
            public_files = models.File.objects.filter(is_hidden=False)
            protected_files = self._get_protected_files(secret_key)
            return (public_files | protected_files).order_by('order')

    def _get_protected_files(self, secret_key):
        try:
            secret = models.Secret.objects.get(key=secret_key)
        except models.Secret.DoesNotExist:
            pass
        else:
            if not secret.is_expired:
                return secret.allowed_files.filter(is_hidden=True)
        return models.File.objects.none()


class BlogTagViewSet(ReadOnlyModelViewSet):
    queryset = models.BlogTag.objects.all()
    serializer_class = serializers.BlogTagSerializer


class BlogArticleViewSet(ReadOnlyModelViewSet):
    queryset = models.BlogArticle.objects.filter(is_hidden=False)
    serializer_class = serializers.BlogArticleSerializer


class ProjectViewSet(ReadOnlyModelViewSet):
    queryset = models.Project.objects.filter(is_hidden=False)
    serializer_class = serializers.ProjectSerializer


class ContactViewSet(ReadOnlyModelViewSet):
    queryset = models.Contact.objects.all()
    serializer_class = serializers.ContactSerializer
