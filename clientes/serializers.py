from rest_framework import serializers
from .models import Cliente
from clientes.validators import *


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not cpf_valido(data['cpf']):
            raise serializers.ValidationError({'cpf': "cpf invalido"})
        if not nome_valido(data['nome']):
            raise serializers.ValidationError({'nome': "Nao digite numero nesse campo"})
        if not rg_valido(data['rg']):
            raise serializers.ValidationError({'rg': "O RG deve ter 9 digitos"})
        if not celular_valido(data['celular']):
            raise serializers.ValidationError(
                {'celular': "O numero celular precisa seguir padrao: xx xxxxx-xxxx"})

        return data
