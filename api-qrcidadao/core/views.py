from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from .models import Veiculo, Denuncia
from .serializers import VeiculoSerializer, DenunciaSerializer
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.throttling import ScopedRateThrottle


class VeiculoList(generics.ListCreateAPIView):
    throttle_scope = 'user'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = "veiculo-list"
    search_fields = ['placa', 'setor_de_origem']
    ordering_fields = ['placa', 'setor_de_origem']
    filterset_fields = ['setor_de_origem', 'esta_ativo']
    permission_classes = [IsAdminUser]


class VeiculoDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'anon'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Veiculo.objects.all()
    serializer_class = VeiculoSerializer
    name = "veiculo-detail"
    permission_classes = [AllowAny]


class DenunciaList(generics.ListCreateAPIView):
    throttle_scope = 'user'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    name = "denuncia-list"
    search_fields = ['veiculo__placa', '']
    permission_classes = [IsAdminUser]


class DenunciaDetail(generics.RetrieveUpdateDestroyAPIView):
    throttle_scope = 'user'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    name = "denuncia-detail"
    permission_classes = [IsAdminUser]


class DenunciaCreate(generics.CreateAPIView):
    throttle_scope = 'anon'
    throttle_classes = (ScopedRateThrottle,)
    queryset = Denuncia.objects.all()
    serializer_class = DenunciaSerializer
    name = "denuncia-create"
    permission_classes = [AllowAny]


class ApiRoot(generics.GenericAPIView):
    name = "api-root"

    def get(self, request, *args, **kwargs):
        return Response({
            "veiculos": reverse(VeiculoList.name, request=request),
            "denuncias": reverse(DenunciaList.name, request=request),
            "criar_denuncia": reverse(DenunciaCreate.name, request=request),
        })
