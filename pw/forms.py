from django import forms
from django.db.models import fields
from django.forms import ModelForm, widgets
from .models import Contact, Comment

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        widgets = {
            'nome': forms.TextInput(attrs = {'class': 'contact1', 'placeholder': 'Nome'}),
            'apelido': forms.TextInput(attrs = {'class': 'contact1', 'placeholder': 'Apelido'}),
            'telefone': forms.TextInput(attrs = {'class': 'contact1', 'placeholder': 'Telefone'}),
            'email': forms.TextInput(attrs = {'class': 'contact1', 'placeholder': 'Email'}),
            'data_nascimento': forms.DateInput(attrs = {'class': 'contact1', 'placeholder': 'Data Nascimento'}),
        }

        labels = {
            'nome': '',
            'apelido': '',
            'telefone': '',
            'email': '',
            'data_nascimento': '',
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'

        widgets = {
            'nome_completo': forms.TextInput(attrs = {'class': 'contact1', 'placeholder': 'Nome Completo'}),
            'ultimo_comentario': forms.Textarea(attrs = {'class': 'contact1', 'placeholder': 'Comentário'}),
        }

        labels = {
            'nome_completo': '',
            'ultimo_comentario': '',
            'data_comentario': ''
        }