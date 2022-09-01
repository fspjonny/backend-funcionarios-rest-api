
from cadastro.models import CadastroModel
from cadastro.serializers import CadastroSerializer
from rest_framework.permissions import BasePermission
from rest_framework.viewsets import ModelViewSet


class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        user = view.request.user
        
        if user.is_superuser:
            return True
        else:
            return request.method in ('GET', 'OPTIONS', 'HEAD', 'PATCH', 'POST',)


class CadastroViewSet(ModelViewSet):
    queryset = CadastroModel.objects.all().order_by('-id')
    serializer_class= CadastroSerializer
    permission_classes = [IsAdmin,]
