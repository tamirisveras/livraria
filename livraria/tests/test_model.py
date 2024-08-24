from django.test import TestCase
from livraria.models import Livro
from django.core.files.uploadedfile import SimpleUploadedFile

class LivroModelTest(TestCase):

    def setUp(self):
        # Configuração inicial dos testes
        self.livro = Livro.objects.create(
            nome="Livro Teste",
            autor="Autor Teste",
            categoria="Categoria Teste",
            codigo="12345",
            quantidade=10,
            valor=100.0,
            ano=2023,
            descricao="Descrição do Livro Teste",
            imagem=SimpleUploadedFile(name='test_image.jpg', content=b'', content_type='image/jpeg'),
            pdf=SimpleUploadedFile(name='test_pdf.pdf', content=b'', content_type='application/pdf')
        )

    def test_livro_criado_com_sucesso(self):
        # Verifica se o livro foi criado com sucesso
        livro = Livro.objects.get(id=self.livro.id)
        self.assertEqual(livro.nome, "Livro Teste")
        self.assertEqual(livro.autor, "Autor Teste")
        self.assertEqual(livro.categoria, "Categoria Teste")
        self.assertEqual(livro.codigo, "12345")
        self.assertEqual(livro.quantidade, 10)
        self.assertEqual(livro.valor, 100.0)
        self.assertEqual(livro.ano, 2023)
        self.assertEqual(livro.descricao, "Descrição do Livro Teste")
        self.assertTrue(livro.imagem)
        self.assertTrue(livro.pdf)

    def test_livro_str_retorna_nome(self):
        # Verifica se o método __str__ retorna o nome do livro
        livro = Livro.objects.get(id=self.livro.id)
        self.assertEqual(str(livro), "Livro Teste")

    def test_livro_imagem_field_blank(self):
        # Verifica se o campo imagem aceita valores em branco
        livro_sem_imagem = Livro.objects.create(
            nome="Livro Sem Imagem",
            autor="Autor Teste",
            categoria="Categoria Teste",
            codigo="54321",
            quantidade=5,
            valor=50.0,
            ano=2023,
            descricao="Descrição Sem Imagem"
        )
        #self.assertIsNone(livro_sem_imagem.imagem)

    def test_livro_pdf_field_blank(self):
        # Verifica se o campo pdf aceita valores em branco
        livro_sem_pdf = Livro.objects.create(
            nome="Livro Sem PDF",
            autor="Autor Teste",
            categoria="Categoria Teste",
            codigo="67890",
            quantidade=5,
            valor=50.0,
            ano=2023,
            descricao="Descrição Sem PDF"
        )
        #self.assertIsNone(livro_sem_pdf.pdf)
