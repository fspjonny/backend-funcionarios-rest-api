from rest_framework import serializers

from cadastro.models import CadastroModel


class CadastroSerializer(serializers.ModelSerializer):
    class Meta:
        model = CadastroModel
        fields = ['id', 'nome', 'sexo', 'nascimento', 'cpf', 'rg', 'email', 
                  'telefone', 'pai', 'mae', 'endereco', 'cargo', 'salario',
                  'admissao',
                ]
