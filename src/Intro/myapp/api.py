from rest_framework import viewsets
from myapp.models import Produto
from myapp.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer