from django.contrib import admin
from django.urls import path
from blogApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.PostListView.as_view(), name='index'),
    path('create/', views.PostCreateView.as_view(), name='create_post' ),
    path('about/', views.about, name='about'),
    path('post_detail/<slug:the_slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post_update/<slug:the_slug>/', views.PostUpdateView.as_view(), name='post_update'),
    path('post_delete/<slug:the_slug>/', views.PostDeleteView.as_view(), name='post_delete'),
    path('user_post/<str:username>/', views.UserPostListView.as_view(), name='user_posts'),
    path('post_like/<slug:the_slug>', views.PostLike, name='post_like'),
    path('add_comment/<slug:the_slug>/', views.AddComment, name='add_comment'),
    path('search/', views.SearchView.as_view(), name='search')
]