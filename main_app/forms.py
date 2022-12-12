from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, DateInput
from main_app.models import *

# Create your forms here.

# Form for creating new user
class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
			profile = Profile.objects.create(id=user.id, user=user)
			profile.save()
		return user

# Form for updating user profile
class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username', 'email']

# Form for updating user profile
class UpdateProfileForm(forms.ModelForm):
    profilePic = forms.ImageField(
    	widget=forms.FileInput(attrs={'class': 'form-control-file'}))
    bio = forms.CharField(widget=forms.Textarea(
    	attrs={'class': 'form-control', 'rows': 5}))

    class Meta:
        model = Profile
        fields = ['profilePic', 'bio']

# Form for creating new event
class EventForm(ModelForm):
  class Meta:
    model = Event
    widgets = {
        'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = ['title','content', 'start_time']
    
  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    
# Forms for Post
class PostForm(ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'content', 'image', 'tag']

