from rest_framework import viewsets
from Fornecedores.models import fornecedor
from Fornecedores.serializer import FornecedorSerializer

class FornecedorViewSet(viewsets.ModelViewSet):
    queryset = fornecedor.objects.all()
    serializer_class = FornecedorSerializer