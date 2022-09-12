from django.forms import ModelForm
from .models import Review, Comment

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['review_title', 'review_text']

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_text']