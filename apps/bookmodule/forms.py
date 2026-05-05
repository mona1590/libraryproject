from django import forms
from .models import Book, Booklab9, Author

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        
        

class Book11Form(forms.ModelForm):
    class Meta:
        model = Booklab9
        fields = ['title', 'price', 'quantity', 'pubdate', 'rating', 'publisher', 'authors']

    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all().order_by("name"),
        widget=forms.CheckboxSelectMultiple()
    )
    
    
    
from .models import BookImage

class BookImageForm(forms.ModelForm):
    class Meta:
        model = BookImage
        fields = ['title', 'image']