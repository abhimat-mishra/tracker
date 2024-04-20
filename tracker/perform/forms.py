from .models import Actions
from django.forms import ModelForm

class ActionsForm(ModelForm):
    class Meta:
        model = Actions
        fields = "__all__"

        labels = {
            'date':"Enter the date:",
            'time':"Time when commited the task",
            'task':"Discribe the work"
        }