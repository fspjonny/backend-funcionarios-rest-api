from django.urls import path
from rest_framework.routers import SimpleRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView, TokenVerifyView)

from cadastro.views.viewsets import CadastroViewSet

from .views.views import api_list

app_name='cadastro'

router = SimpleRouter()
router.register('cadastro/api', CadastroViewSet)

urlpatterns = [
    path('', api_list, name='about_api'),
    path('cadastro/api/token/', 
         TokenObtainPairView.as_view(), name='token_obtain'
    ),
    path('cadastro/api/token/refresh/', 
         TokenRefreshView.as_view(), name='token_refresh'
    ),
    path('cadastro/api/token/verify/', 
         TokenVerifyView.as_view(), name='token_verify'
    ),
]

urlpatterns += router.urls
