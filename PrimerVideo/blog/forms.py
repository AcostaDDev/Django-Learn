from django import forms

class PostForm(forms.Form):
    title = forms.CharField(label="Titulo para el post", max_length=250)
    body = forms.CharField(label="Contenido", widget=forms.Textarea)
    published = forms.BooleanField(label="¿Publicar?")