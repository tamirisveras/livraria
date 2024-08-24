from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from livraria.models import Livro
from django.core.files.uploadedfile import SimpleUploadedFile

    
class SimpleURLTests(TestCase):

    def setUp(self):
        # Configuração inicial dos testes
        image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.livro = Livro.objects.create(
            nome="Livro Teste",
            autor="Autor Teste",
            categoria="Categoria Teste",
            codigo="12345",
            quantidade=10,
            valor=100.0,
            ano=2023,
            descricao="Descrição do Livro Teste",
            imagem=image
        )

    def test_listar_livros_url(self):
        # Testa a URL da página inicial (listar livros)
        response = self.client.get(reverse('listar_livros'))
        self.assertEqual(response.status_code, 200)

    def test_deletar_livro_url(self):
        # Testa a URL de deletar livro (deve redirecionar, pois a view requer login)
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('deletar_livro', args=[self.livro.id]))
        self.assertEqual(response.status_code, 302) 

    def test_detalhar_livro_url(self):
        # Testa a URL de detalhar livro
        response = self.client.get(reverse('detalhar_livro', args=[self.livro.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.livro.nome)

    def test_cadastrar_livro_url(self):
        # Testa a URL de cadastrar livro (formulário de cadastro)
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('cadastrar_livro'))
        self.assertEqual(response.status_code, 200)

    def test_editar_livro_url(self):
        # Testa a URL de editar livro
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('editar_livro', args=[self.livro.id]))
        self.assertEqual(response.status_code, 200)

    def test_buscar_livro_url(self):
        # Testa a URL de buscar livro
        response = self.client.post(reverse('buscar_livro'), {'infor': 'Livro Teste'})
        self.assertEqual(response.status_code, 200)

    def test_page_login_url(self):
        # Testa a URL da página de login
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)

    def test_autenticar_usuario_url(self):
        # Testa a URL de autenticar usuário
        response = self.client.post(reverse('autenticar_usuario'), {
            'username': 'testuser',
            'password': '12345'
        })
        self.assertEqual(response.status_code, 302)

    def test_cadastrar_usuario_url(self):
        # Testa a URL de cadastrar usuário
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)

    def test_logout_usuario_url(self):
        # Testa a URL de logout do usuário
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout_usuario'))
        self.assertEqual(response.status_code, 302)
