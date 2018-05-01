from django                             import forms

from django.contrib.auth.models         import User
from django.contrib.auth                import get_user_model
from django.contrib.auth.forms          import UserCreationForm, UserChangeForm


class UserCreateForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2','first_name', 'last_name')
        # model = get_user_model()

    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].label = 'Display Name'
    #     seld.fields['email'].label = "Email Address"
    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password'

        )
    #    exclude = ()
