from django.urls import path
from . import views
from .views import *

from django.contrib.auth import views as auth_views



app_name ='Site'
urlpatterns=[
    path('', PostIndexView.as_view(), name='ex2'),
    path('add/', PostAddView.as_view(), name='add'),
    path('g/<str:genre>', PostGenreView.as_view(), name='genre'),
    path('<int:pk>/edit', PostUpdateView.as_view(), name='post_edit'),
    path('<int:pk>/delete', PostDeleteView.as_view(), name='post_delete'),
    path("<int:pk>/", views.Post_detail, name="post_detail"),
    path("<category>/", views.Post_category, name="post_category"),
    

]