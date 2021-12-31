from django.urls import path
from .import views
from django.contrib.auth.decorators import login_required

app_name = 'posts'
urlpatterns = [
    path('', views.BlogHome.as_view(), name='home'),
    path('create/', login_required(views.BlogPostCreate.as_view()), name='create'),
    path('post-<str:pk>/', views.BlogPostDetail.as_view(), name='show'),
    path('post-<str:pk>/update/', views.BlogPostUpdate.as_view(), name='update'),
    path('post-<str:pk>/delete/', views.BlogPostDelete.as_view(), name='delete'),
]