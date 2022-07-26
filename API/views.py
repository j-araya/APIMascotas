from django.views.generic import TemplateView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly

from API.models import Pet, Product
from API.serializers import PetSerializer, ProductSerializer

class PetViewSet(ModelViewSet):

    """ Viewset para las mascotas """

    serializer_class = PetSerializer
    queryset = Pet.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]

class ProductViewSet(ModelViewSet):

    """ Viewset para los productos vendidos """

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
        
class DocumentationView(TemplateView):
    template_name = 'docs.html'
    