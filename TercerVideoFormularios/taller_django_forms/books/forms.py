from django import forms
from django.contrib.auth.models import User


class BookForm(forms.Form):
    title = forms.CharField()
    author = forms.ChoiceField(choices=[(user.pk, user.username) for user in User.objects.all()])
    rating = forms.IntegerField(min_value=0, max_value=5)

    def clean_author(self):
        author = self.cleaned_data.get('author')
        user = User.objects.get(pk=author)
        if user.username == 'admin':
            raise forms.ValidationError('The author cannot be Admin')
        
        return author
