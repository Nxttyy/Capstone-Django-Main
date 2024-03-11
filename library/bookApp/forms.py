from django import forms

class CommentForm(forms.Form):
    content = forms.CharField(label="Comment content", max_length=500)