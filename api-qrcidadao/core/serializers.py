from rest_framework import serializers
from .models import Denuncia, Veiculo


class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    esta_ativo = serializers.ChoiceField(
        choices=Veiculo.STATUS_ATIVO_CHOICES, source='get_esta_ativo_display', read_only=True)

    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'setor_de_origem', 'esta_ativo']


class DenunciaSerializer(serializers.HyperlinkedModelSerializer):
    veiculo = VeiculoSerializer(read_only=True)

    class Meta:
        model = Denuncia
        fields = ['id', 'data', 'local', 'descricao', 'veiculo']
        read_only_fields = ['id', 'data']
