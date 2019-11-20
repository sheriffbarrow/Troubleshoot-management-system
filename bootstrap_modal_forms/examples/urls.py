from django.urls import path

from . import views


urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('create/', views.ComplaintCreateView.as_view(), name='create_book'),
    path('update/<int:pk>', views.ComplaintUpdateView.as_view(), name='update_book'),
    path('read/<int:pk>', views.ComplaintReadView.as_view(), name='read_book'),
    path('delete/<int:pk>', views.ComplaintDeleteView.as_view(), name='delete_book'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
]
