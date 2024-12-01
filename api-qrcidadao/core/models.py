import uuid
from django.db import models


class Veiculo(models.Model):
    STATUS_ATIVO_CHOICES = (
        (True, 'Ativo'),
        (False, 'Inativo'),
    )

    placa = models.CharField(max_length=7, unique=True)
    setor_de_origem = models.CharField(max_length=100)
    esta_ativo = models.BooleanField(
        choices=STATUS_ATIVO_CHOICES, default=False)

    def __str__(self):
        status = dict(self.STATUS_ATIVO_CHOICES).get(
            self.esta_ativo, 'Indefinido')
        return f"Veículo {self.placa} - Setor: {self.setor_de_origem} - Ativo: {status}"


class Denuncia(models.Model):
    veiculo = models.ForeignKey(
        Veiculo, related_name='denuncias', on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now_add=True)
    local = models.CharField(max_length=255)
    descricao = models.TextField(max_length=510)

    def __str__(self):
        return f"Denúncia {self.id} do veículo {self.veiculo.placa} - {self.data}"
