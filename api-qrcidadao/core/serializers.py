from rest_framework import serializers
from .models import Denuncia, Veiculo


class VeiculoSerializer(serializers.HyperlinkedModelSerializer):
    esta_ativo = serializers.ChoiceField(
        choices=Veiculo.STATUS_ATIVO_CHOICES, source='get_esta_ativo_display', read_only=True)

    class Meta:
        model = Veiculo
        fields = ['id', 'placa', 'setor_de_origem', 'esta_ativo']


class DenunciaSerializer(serializers.ModelSerializer):
    # Veículo será preenchido automaticamente
    veiculo = VeiculoSerializer(read_only=True)
    veiculo_id = serializers.PrimaryKeyRelatedField(
        queryset=Veiculo.objects.all(), write_only=True, source="veiculo"
    )

    class Meta:
        model = Denuncia
        fields = ['id', 'data', 'local', 'descricao', 'veiculo', 'veiculo_id']
        read_only_fields = ['id', 'data', 'veiculo']

    def create(self, validated_data):
        # A data é gerada automaticamente no modelo
        return Denuncia.objects.create(**validated_data)
