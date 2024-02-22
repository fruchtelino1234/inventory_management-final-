from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Category, InventoryItem
from django import forms
# from .models import UploadedImage
from django.db import models
from django.forms import ImageField
from django import forms
from .models import Image

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class InventoryItemForm(forms.ModelForm):
	category = forms.ModelChoiceField(queryset=Category.objects.all(), initial=0)
	class Meta:
		model = InventoryItem
		fields = ['name', 'quantity', 'category']


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['title', 'image']




