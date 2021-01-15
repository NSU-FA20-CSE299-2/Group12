from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class ProfileCreationForm(UserCreationForm):
    
    class Meta(UserCreationForm):
        model = Profile
        fields = UserCreationForm.Meta.fields

        help_texts = {
            'username': None,
        }