from django import forms
from livraria.models import Livro

class LivroForm(forms.ModelForm):

    class Meta:
        model = Livro
        fields = ('nome','autor','categoria','codigo', 
        'quantidade', 'valor', 'imagem', 'ano', 'descricao', 'pdf')

        widgets = {
            'nome': forms.TextInput(attrs={ 'class': 'form-control', 
                                            'placeholder':'Nome do livro'}),
            'autor': forms.TextInput(attrs={ 'class': 'form-control'}),
            'categoria': forms.TextInput(attrs={ 'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={ 'class': 'form-control'}),
            'quantidade': forms.TextInput(attrs={ 'class': 'form-control'}),
            'valor': forms.TextInput(attrs={ 'class': 'form-control'}),
            'imagem': forms.FileInput(attrs={ 'class': 'form-control'}),
            'ano': forms.TextInput(attrs={ 'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={ 'class': 'form-control'}),
            'pdf': forms.FileInput(attrs={ 'class': 'form-control'}),
        }