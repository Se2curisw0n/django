from django import forms
from .models import User, Review
from allauth.account.forms import LoginForm

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = [
            'title',
            'restaurant_name',
            'rating',
            'image1',
            'image2',
            'image3',
            'content',
        ]
        widgets = {
            'rating': forms.RadioSelect,
        }


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'intro',
        ]
        widgets = {
            'intro': forms.Textarea,
        }

class MyCustomLoginForm(LoginForm):

    def login(self, *args, **kwargs):

        # Add your own processing here.

        # You must return the original result.
        return super(MyCustomLoginForm, self).login(*args, **kwargs)