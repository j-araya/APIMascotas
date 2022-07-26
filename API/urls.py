from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view

from API.views import PetViewSet, ProductViewSet

router = DefaultRouter()
router.register('pets', PetViewSet, basename='pets')
router.register('products', ProductViewSet, basename='products')

urlpatterns = [
    path('', include(router.urls)),
    path('schema/', get_schema_view(
        title='API adopcion de mascotas',
        description='Una API para administrar un centro de adopcion de mascotas',
        version='1.0.0'

    ), name='schema'),
    path('docs/', TemplateView.as_view(
        template_name='docs.html',
        extra_context={'schema_url':'schema'}
    ), name='docs'),
]