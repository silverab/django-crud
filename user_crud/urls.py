from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.user_form, name='insert'),
    path('<int:id>/', views.user_form, name='update'),
    path('delete/<int:id>', views.user_delete, name='delete'),
    path('list/', views.user_list, name='list')
]