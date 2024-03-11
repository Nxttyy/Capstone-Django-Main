from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(label="Comment content", max_length=500)

class SearchForm(forms.Form):
    prompt = forms.CharField(label="Search books", max_length=30)