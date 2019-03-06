from django.forms import ModelForm
from .models import Kekka


class KekkaForm(ModelForm):
    class Meta:
        model = Kekka
        fields = ['subject', 'student_code', 'date', 'reason']
