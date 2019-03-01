from django.forms import ModelForm
from .models import Notification


class NoteForm(ModelForm):
    class Meta:
        model = Notification
        fields = ['subject', 'absent_date', 'reason']
