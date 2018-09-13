from django import forms
from .models import *

# class ContactForm(forms.Form):
#     from_email = forms.EmailField(required=True)
#     subject = forms.CharField(required=True)
#     message = forms.CharField(widget=forms.Textarea, required=True)



class FeedbackForm(forms.ModelForm):
    # phone  = forms.IntegerField()
    # neighbourhood =forms.IntegerField()
    # rating = forms.IntegerField()
    # comments = forms.IntegerField()


    class Meta:
        model = Post
        fields= ('phone','neighbourhood','rating','comments')
        
  