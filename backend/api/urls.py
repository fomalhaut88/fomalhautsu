from django.urls import path
from rest_framework.routers import SimpleRouter

from . import views


router = SimpleRouter(trailing_slash=False)
router.register(r'images', views.ImageViewSet)
router.register(r'files', views.FileViewSet)
router.register(r'blog-tags', views.BlogTagViewSet)
router.register(r'blog-articles', views.BlogArticleViewSet)
router.register(r'projects', views.ProjectViewSet)
router.register(r'contacts', views.ContactViewSet)

urlpatterns = router.urls
