from django.contrib import admin

from .models import CadastroModel


@admin.register(CadastroModel)
class CadastroAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'nome', 'sexo', 'nascimento', 'rg', 'cpf', 'email', 'telefone',
        'pai', 'mae', 'endereco', 'cargo', 'salario', 'admissao')
    list_per_page = 10
    list_display_links = 'nome',
    list_filter = 'nome', 'rg', 'cpf', 'email'

