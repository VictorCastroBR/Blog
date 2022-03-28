from django.urls import path

from . import views

app_name = 'post'

urlpatterns = [
    path('', views.home),
    path('novo-post/', views.form),
    path('postar/', views.postar),
    path('<int:id_post>/', views.view_post),
    path('edit/<int:id_post>/', views.edit_post),
    path('update/<int:id_post>/', views.update_post),
    path('delete/<int:id_post>', views.delete_post), 
]  
