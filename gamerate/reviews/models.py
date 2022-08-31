from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Review(models.Model):
    review_title = models.CharField(max_length=120, null=False)
    review_text = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f'{self.review_title} review by {self.user.get_username()}'

class Comment(models.Model):
    comment_text = models.TextField(null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, null=False)
    votes = models.IntegerField(default=0)
    pub_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.get_username()}'s comment on {self.review.user.get_username()}'s review"

