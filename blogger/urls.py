from django.urls import path, include
from django.contrib.auth import urls as auth_urls
from django.contrib.auth import views as auth_views

from . import forms
from . import views

urlpatterns = [
        path('', auth_views.login, {'authentication_form':forms.LoginForm}),
        path('login/', auth_views.login, {'authentication_form':forms.LoginForm}),
        path('', include(auth_urls)),
        path('register/', views.SignUpView.as_view()),
        path('blog/create', views.BlogCreateView.as_view()),
        path('blogs/', views.BlogListView.as_view()),
        path('blog/edit/<int:pk>', views.BlogEditView.as_view()),
        path('blog/delete/', views.BlogDeleteView.as_view()),
        path('blog/read/<int:pk>', views.BlogDetailView.as_view()),
        path('blog/<int:pk>/comment/add', views.BlogAddCommentView.as_view()),
    ]
