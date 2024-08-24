from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from livraria.models import Livro
from django.core.files.uploadedfile import SimpleUploadedFile


class LivrariaViewsTest(TestCase):

    def setUp(self):
        # Configuração inicial dos testes
        image = SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg')
        self.client = Client()
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
    
    def test_deletar_livro(self):
        # Testa a função deletar_livro
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('deletar_livro', args=[self.livro.id]))
        self.assertRedirects(response, reverse('listar_livros'))
        self.assertFalse(Livro.objects.filter(id=self.livro.id).exists())

    def test_buscar_livro(self):
        # Testa a função buscar_livro
        response = self.client.post(reverse('buscar_livro'), {'infor': 'Livro Teste'})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Livro Teste')

    def test_cadastrar_livro(self):
        # Testa a função cadastrar_livro
        self.client.login(username='testuser', password='12345')
        response = self.client.post(reverse('cadastrar_livro'), {
            'nome': 'Novo Livro',
            'autor': 'Novo Autor',
            'categoria': 'Nova Categoria',
            'codigo': '54321',
            'quantidade': 5,
            'valor': 50.0,
            'ano': 2023,
            'descricao': 'Nova descrição',
        })
        self.assertEqual(response.status_code, 200)
        #self.assertTrue(Livro.objects.filter(nome='Novo Livro').exists())

    def test_detalhar_livro(self):
        # Testa a função detalhar_livro
        response = self.client.get(reverse('detalhar_livro', args=[self.livro.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Livro Teste')

    def test_listar_livros(self):
        # Testa a função listar_livros
        response = self.client.get(reverse('listar_livros'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Livro Teste')

    def test_page_login(self):
        # Testa a função page_login
        response = self.client.get(reverse('page_login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livraria/pages/login.html')

    def test_cadastro(self):
        # Testa a função cadastro
        response = self.client.get(reverse('cadastro'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'livraria/pages/cadastro.html')

    def test_logout_usuario(self):
        # Testa a função logout_usuario
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('logout_usuario'))
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('page_login'))

    def test_cadastrar_usuario(self):
        # Testa a função cadastrar_usuario
        response = self.client.post(reverse('cadastrar_usuario'), {
            'username': 'novousuario',
            'password': 'senha123'
        })
        self.assertRedirects(response, reverse('page_login'))
        #self.assertTrue(User.objects.filter(username='novousuario').exists())
