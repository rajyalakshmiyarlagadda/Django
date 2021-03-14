from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create_post' ),
    path('about/', views.about, name='about'),
    path('post_detail/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_update/<int:pk>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<int:pk>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('user_post/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),
    path('post_like/<int:pk>', views.PostLike, name='post_like'),
    path('add_comment/<int:pk>', views.AddComment, name='add_comment'),
    path('search/', views.SearchView.as_view(), name='search')
]