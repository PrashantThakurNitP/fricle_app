
from django.forms import ModelForm
from .models import messageModel
from django import forms

#this class is created so that to provide form for adding todo
class messageForm(ModelForm):
	#specify what class and what model it would be working with
	#title = forms.TextField(required=False, widget=forms.Textarea(attrs={'rows': 2, 'cols': 10}))
    #receiver = forms.CharField(required=False, widget=forms.Textarea(attrs={'rows': 4, 'cols': 10}))

	class Meta:#specify what class we are working with
		model=messageModel
		fields=['title','receiver']#these are feature from model that we will set



