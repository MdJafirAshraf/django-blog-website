from django.urls import path
from .views import (
    blog_list_view,
    blog_create,
    blog_post_details,
    blog_update,
    blog_delete
    )

urlpatterns = [
    # app views path
    path('', blog_list_view),
    path('<str:slug>/', blog_post_details),
    path('<str:slug>/edit', blog_update),
    path('<str:slug>/delete', blog_delete),
]
