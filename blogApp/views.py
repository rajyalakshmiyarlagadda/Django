from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import PostForm
from .models import Post, Comments
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)

# Create your views here.
class PostCreateView(CreateView):
    model = Post
    #form_class = PostForm
    fields = ['title', 'content']
    success_url = '/'

    def form_valid(self, form):
        print (f'Inside the post create view form{self.request.user}')
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostListView(ListView):
    model = Post
    template_name = 'blogApp/index.html'
    context_object_name = 'posts'
    print('I am in list view')

class PostDetailView(DetailView):
    model = Post

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        likes_connected = get_object_or_404(Post, id=self.kwargs['pk'])
        liked = False
        if likes_connected.likes.filter(id=self.request.user.id).exists():
            liked = True
        data['number_of_likes'] = likes_connected.number_of_likes()
        data['post_is_liked'] = liked
        return data   

class PostUpdateView(UpdateView):
    model = Post
    fields = ['title', 'content']
    #success_url = '/post_detail'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

def about(request):
    return render(request, 'blogApp/about.html', {'title': 'About'})  

class UserPostListView(ListView):
    model = Post
    template_name = 'blogApp/user_posts.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        print(user)
        return Post.objects.filter(author=user).order_by('-date_posted') 

def PostLike(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
    else:
        post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)])) 


def AddComment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    print(post)
    if request.method == 'POST':
        user = get_object_or_404(User, id=request.POST.get('user_id'))
        Comments(comments=request.POST.get('comment'), post=post, user=user).save()
    else:
        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))     
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)])) 

class SearchView(ListView):
    model = Post
    template_name = 'blogApp/search.html'
    context_object_name = 'search_results'

    def get_queryset(self):
        result = super(SearchView, self).get_queryset()
        query = self.request.GET.get('search')
        if query:
            postresult = Post.objects.filter(Q(title__contains=query) | Q(content__contains=query))
            result = postresult
        else:
            result = None
        return result    


    
    