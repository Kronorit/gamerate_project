from django.urls import path
from .views import review, createReview

urlpatterns = [
    path('<int:id>/', review),
    path('new_review', createReview)
]