from django import forms
from app1.models import Blog,Review 

class BlogForm(forms.ModelForm):
    class Meta:
        model=Blog
        fields='__all__'
        # fields=['title','body']
        # exclude=['title']
        widgets={
                'title':forms.TextInput(attrs={'placeholder':'title here'}),
                'author':forms.TextInput(attrs={'placeholder':'author here'}),
                 }
        
    #----------------------clean field method------------

    def clean_title(self):
        title=self.cleaned_data['title']

        if not(title[0].isupper()):
            raise forms.ValidationError('first chracter should be upper case')
        return title
    
    def clean_author(self):
        author=self.cleaned_data['author']
        if not(author[0].isupper()):
            raise forms.ValidationError('author should be upper case')
        return author
    
    def clean_body(self):
        body=self.cleaned_data['body']
        if not(body[0].isupper()):
            raise forms.ValidationError('body should be upper case')
        return body
    
class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        fields='__all__'


    
    
    
    