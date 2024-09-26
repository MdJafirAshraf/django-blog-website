from django.urls import path
from .views import (
    blog_list_view,
    blog_post_details
    )

urlpatterns = [
    # app views path
    path('', blog_list_view),
    path('<str:slug>/', blog_post_details),
]
