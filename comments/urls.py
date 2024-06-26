from django.contrib import admin
from django.urls import path, include
from books import views
from comments.views import CommentFormCreateView, CommentFormEditView, CommentFormDeleteView

urlpatterns = [
    #path('', views.search_redirect),
    path('create/', CommentFormCreateView.as_view(), name='comment_create'),
    path('edit/', CommentFormEditView.as_view(), name='comment_update'),
    path('delete/<int:comment_id>/', CommentFormDeleteView.as_view(), name='comment_delete'),
]