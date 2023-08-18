from .import views
from django.urls import path

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('get-token/', views.get_token, name='get-token'),
    path('update-profile/', views.UpdateProfileView.as_view(), name='update-profile'),
]