from django.contrib import admin
from reviews.models import Review, Comment

# Register your models here.

admin.site.register(Review)
admin.site.register(Comment)