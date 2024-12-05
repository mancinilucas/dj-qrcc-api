from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Veiculo, Denuncia
from .serializers import VeiculoSerializer, DenunciaSerializer


class VeiculoList(generics.ListCreateAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = "veiculo-list"
    search_fields = ['placa', 'setor_de_origem']
    ordering_fields = ['placa', 'setor_de_origem']
    filterset_fields = ['setor_de_origem', 'esta_ativo']


class VeiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = "veiculo-detail"


class DenunciaList(generics.ListCreateAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    name = "denuncia-list"
    search_fields = ['veiculo__placa', '']


class DenunciaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    name = "denuncia-detail"


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response({
            "veiculos": reverse(VeiculoList.name, request=request),
            "denuncias": reverse(DenunciaList.name, request=request),
        })
