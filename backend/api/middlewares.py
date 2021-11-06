from django.core.exceptions import PermissionDenied
from django.conf import settings

from . import models


class ForbiddenFilesMiddleware:
    """
    This middleware checks and forbids media files relaterd to the model File
    if the file is hidden and the request does not contain the correct secret.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Check media URLs only
        if request.path.startswith(settings.MEDIA_URL):
            self._check_media_file(request)

        response = self.get_response(request)
        return response

    def _check_media_file(self, request):
        """
        This method checks permissions for the media file.
        It raises PermissionDenied if something is wrong with the access.
        """
        # Allow everything for superuser
        if request.user.is_superuser:
            return

        # Extract file name from the URL
        filename = request.path[len(settings.MEDIA_URL):]

        # Search for the related file
        file = models.File.objects.filter(file=filename).first()

        # If file is found and it is hidden
        if file is not None and file.is_hidden:
            # Extract the secret value from querystring and search for
            # the related secret object.
            secret_key = request.GET.get('secret', '')
            secret = models.Secret.objects.filter(key=secret_key).first()

            # Raise error 403 if no secret object found or
            # the found object does not have permissions to get the file.
            if not (
                        secret and
                        not secret.is_expired and
                        secret.allowed_files.filter(id=file.id).exists()
                    ):
                raise PermissionDenied()
