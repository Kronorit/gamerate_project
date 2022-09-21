from datetime import datetime

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from .models import Comment, Review
from .forms import ReviewForm, CommentForm

def createReview(request):
    request.session['last_url'] = request.build_absolute_uri()
    userId = request.session.get('_auth_user_id')
    if userId == None:
        return redirect('/login/', permanent=False)
    else:
        if request.method == "POST":
            user = User.objects.get(pk=userId)
            reviewForm = ReviewForm(request.POST)
            if reviewForm.is_valid():
                cleanForm = reviewForm.cleaned_data
                review = Review(review_title=cleanForm['review_title'], 
                                review_text=cleanForm['review_text'], 
                                user=user, 
                                pub_date=datetime.now())
                review.save()
                return HttpResponseRedirect("/")
        else:
            reviewForm = ReviewForm()
            return render(request, 'reviews/new_review.html', {'reviewForm': reviewForm})

def review(request, id):
    request.session['last_url'] = request.build_absolute_uri()
    userId = request.session.get('_auth_user_id')
    review = get_object_or_404(Review, pk=id)
    comments = Comment.objects.filter(review=id)
    if userId == None:
        user = request.user
    else:
        user = User.objects.get(pk=userId)
    if request.method == "POST":
        commentForm = CommentForm(request.POST)
        if commentForm.is_valid():
            cleanForm = commentForm.cleaned_data
            comment = Comment(comment_text=cleanForm['comment_text'],
                            user=user,
                            review=review,
                            pub_date=datetime.now())
            comment.save()
            return HttpResponseRedirect(f"/review/{id}")
    else:
        commentForm = CommentForm()
        return render(request, 'reviews/review.html', {'review': review, 
                                                       'comments': comments, 
                                                       'commentForm':commentForm,
                                                       'user': user})
