from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Veiculo, Denuncia
from .serializers import VeiculoSerializer, DenunciaSerializer


class VeiculoList(generics.ListAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = "veiculo-list"


class VeiculoDetail(generics.RetrieveAPIView):
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = "veiculo-detail"


class DenunciaList(generics.ListAPIView):
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    name = "denuncia-list"


class DenunciaDetail(generics.RetrieveAPIView):
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
