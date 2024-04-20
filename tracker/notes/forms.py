from .models import AddShow
from django.forms import ModelForm

class AddShowForm(ModelForm):
    class Meta:
        model = AddShow
        fields = ['note']

        labels = {
            'note' : "Create the notes:"
        }
        