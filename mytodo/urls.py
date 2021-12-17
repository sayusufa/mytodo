from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home_page'),
    path('executed/<int:task_id>', views.executed, name='executed'),
    path('unexecuted/<int:task_id>', views.unexecuted, name='unexecuted'),
    path('edit/<int:task_id>', views.edit, name='edit'),
    path('delete/<int:task_id>', views.delete, name='delete'),
    path('warn_user_deleting_all/', views.warn_user_deleting_all, name='warn_user_deleting_all'),
    path('delete_all/', views.delete_all, name='delete_all'),
]