from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_livros, name='listar_livros'),
    path('deletar_livro/<int:id>/', views.deletar_livro, name='deletar_livro'),
    path('livro/<int:id>/', views.detalhar_livro, name='detalhar_livro'), 
    path('livro/novo/', views.cadastrar_livro, name='cadastrar_livro'),
    path('livro/editar/<int:id>/', views.editar_livro, name='editar_livro'),
    path('buscar_livro', views.buscar_livro, name='buscar_livro'),
    path('page_login', views.page_login, name='page_login'),
    path('autenticar_usuario', views.autenticar_usuario, name='autenticar_usuario'),
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('cadastro', views.cadastro, name='cadastro'),
    path('logout_usuario', views.logout_usuario, name='logout_usuario'),
]