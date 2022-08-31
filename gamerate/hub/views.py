from django.shortcuts import render
from reviews.models import Review

# Create your views here.

def review_index(request):
    no_reviews = Review.objects.count()
    reviews = Review.objects.all()
    return render(request, 'index.html', {'no_reviews': no_reviews, 'reviews': reviews})