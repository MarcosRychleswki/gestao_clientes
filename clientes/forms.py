from django.forms import ModelForm
from .models import Person, Produto




class PersonForm(ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']


class ProdutoForm(ModelForm):
    class Meta:
        model = Produto
        fields = ['descricao', 'preco']