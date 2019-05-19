from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('<int:post_id>', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    path('create/', views.create, name='create'),
    path('edit/<int:post_id>', views.edit, name="edit"),
    path('update/<int:post_id>', views.update, name="update"),
    path('delete/<int:post_id>', views.delete, name="delete"),
    path('new_comment/<int:post_id>', views.new_comment, name="new_comment"),
    path('like/<int:post_id>', views.like, name="like"),
]
