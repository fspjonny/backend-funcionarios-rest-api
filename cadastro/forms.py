from dataclasses import fields

from django.forms import ModelForm

from .models import CadastroModel


class CadastroForm(ModelForm):
    class Meta:
        model = CadastroModel
        fields = ['nome', 'sexo', 'nascimento', 'rg', 'cpf', 'email', 
                  'telefone', 'pai', 'mae', 'endereco', 'cargo', 'salario', 
                  'admissao',
                ]
