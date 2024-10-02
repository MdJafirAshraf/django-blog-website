from django import forms

class BlogPostForm(forms.Form):
    title = forms.CharField()
    slug = forms.CharField()
    content = forms.CharField(widget=forms.Textarea)