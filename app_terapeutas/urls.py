from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='lista_terapeutas'),
    path('<int:id>', views.ver_terapeuta, name='ver_terapeuta'),
    path('agregar/', views.agregar_terapeuta, name='agregar_terapeuta'),
    path('editar/<int:id>/', views.editar_terapeuta, name='editar_terapeuta'),
    path('borrar/<int:id>/', views.borrar_terapeuta, name='borrar_terapeuta'),
]