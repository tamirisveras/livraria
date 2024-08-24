from django.db import models

class Livro(models.Model):
    nome = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    categoria = models.CharField(max_length=100)
    codigo = models.CharField(max_length=20)
    quantidade = models.IntegerField()
    valor = models.FloatField()
    imagem = models.ImageField(upload_to='livraria/media', blank=True)
    ano = models.IntegerField()
    descricao = models.TextField()
    pdf = models.FileField(upload_to='livraria/pdfs', blank=True, null=True)

    def __str__(self):
        return self.nome 

