from django.forms import ModelForm, EmailInput
from .models import Review

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_text']