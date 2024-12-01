from django.urls import path, include
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

urlpatterns = [
    path('veiculos/', views.VeiculoList.as_view(), name='veiculo-list'),
    path('veiculos/<int:pk>/', views.VeiculoDetail.as_view(), name='veiculo-detail'),
    path('denuncias/', views.DenunciaList.as_view(), name='denuncia-list'),
    path('denuncias/<int:pk>/', views.DenunciaDetail.as_view(),
         name='denuncia-detail'),
    path('', views.ApiRoot.as_view(), name=views.ApiRoot.name),
]
