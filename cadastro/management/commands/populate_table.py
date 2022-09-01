from cadastro.models import CadastroModel
from django.core.management.base import BaseCommand
from mocks.cadastro_mockup import get_person
from utils.progressbar import progressbar


def create_persons():
    lista_de_pessoas = []
    
    for _ in progressbar(range(100), 'Pessoas'):
        data = get_person()
        obj = CadastroModel(**data)
        lista_de_pessoas.append(obj)
    CadastroModel.objects.bulk_create(lista_de_pessoas)    

class Command(BaseCommand):
    help = "Criar Pessoas no cadastro"

    def handle(self, *args, **options):
        create_persons()
