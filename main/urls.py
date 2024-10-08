from django.urls import path
from main.views import show_main
from main.views import show_main, create_book
from main.views import (
    show_main,create_book, 
    show_xml,show_json, 
    show_xml_by_id,show_json_by_id, 
    register,login_user,logout_user,
    show_css,edit_book,delete_book
)

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-book/', create_book, name='create_book'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('edit-book/<int:id>', edit_book, name='edit_book'),
    path('delete/<int:id>', delete_book, name='delete_book'), 
]