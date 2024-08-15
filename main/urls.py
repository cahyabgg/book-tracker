from django.urls import path
from main.views import show_main
from main.views import show_main, create_book


app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-book', create_book, name='create_book'),
]