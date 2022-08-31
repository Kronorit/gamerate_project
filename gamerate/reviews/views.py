from django.shortcuts import get_object_or_404, render, redirect
from .models import Review, Comment
from .ReviewForm import ReviewForm

reviewForm = ReviewForm()

def createReview(request):
    return render(request, 'reviews/new_review.html', {'reviewForm': reviewForm})

def review(request, id):
    review = get_object_or_404(Review, pk=id)
    comments = Comment.objects.filter(review=id)
    return render(request, 'reviews/review.html', {'review': review, 'comments': comments})