from django import forms
from store.models import Product
        
class BookForm(forms.Form):
    book_name = forms.CharField(max_length=100)
    author_name = forms.CharField(max_length=100)