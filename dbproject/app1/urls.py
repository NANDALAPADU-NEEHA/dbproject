from django.urls import path
from app1 import views

urlpatterns=[
    path('',views.Home,name='homepage'),
    path('createAuthor',views.CreateAuthor,name='author'),
    path('createBook',views.CreateBook,name='book'),
]