from django.urls import path
from . import views

urlpatterns = [
    path('note/', views.note, name='note'),
    path('delete/<int:pk>/', views.delete_note, name='delete_note'),
    path("notes/edit/<int:pk>/", views.edit_note, name="edit_note"),
    path("notes/<int:pk>/", views.view_note, name="view_note"),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
]