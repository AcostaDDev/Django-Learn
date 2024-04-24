from django import forms

from .models import Book

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(label="Emisor")
    cc_myself = forms.BooleanField(required=False)


class InsertBookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year', 'publisher']

        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control'}),
            'author' : forms.TextInput(attrs={'class':'form-control'}),
            'genre' : forms.TextInput(attrs={'class':'form-control'}),
            'year' : forms.NumberInput(attrs={'class':'form-control', 'min':1900, 'max':2100}),
            'publisher' : forms.TextInput(attrs={'class':'form-control'}),
        }