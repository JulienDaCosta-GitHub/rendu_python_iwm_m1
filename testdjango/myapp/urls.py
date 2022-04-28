from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('edit/<int:question_id>/', views.edit, name='edit'),
    path('delete/<int:question_id>/', views.delete, name='delete'),
    path('insert/', views.insert, name='insert'),
    path('update/<int:question_id>/', views.update, name='update'),
]