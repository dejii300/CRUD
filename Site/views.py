from django.shortcuts import render
from .models import *
from .forms import *


from django.views.generic.list import ListView

from django.views.generic.edit import FormView, CreateView, UpdateView, DeleteView

from django.db.models import F
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator






# Create your views here.

class PostDeleteView(DeleteView):

    model = Post
    template_name = 'app/delete.html'
    context_object_name = 'post'
    success_url = '/'

    



class PostUpdateView( UpdateView):
    

    model = Post
    template_name = 'app/add.html'
    form_class = postForm
    success_url = '/'

"""
class AddBookView(FormView):
    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
"""       
class PostAddView(CreateView):
    model = Post
    template_name = 'app/add.html'
    form_class = postForm
    success_url = '/'



"""
class IndexView(TemplateView):
    template_name = "home.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Books.objects.all()
        return context
"""



class PostIndexView( ListView):
    model = Post
    template_name = "app/home.html"
    context_object_name = 'posts'
    paginate_by = 2

    #def get_queryset(self):
        #return Books.objects.all()[:3]


class PostGenreView(ListView):
    model = Post
    template_name = 'app/home.html'
    context_object_name = 'posts'
    paginate_by = 1

    def get_queryset(self, *args, **kwargs):
        return Post.objects.filter(genre__icontains=self.kwargs.get('title'))
    

def Post_category(request, category):
    posts = Post.objects.filter(
        Categories__name__contains=category
    ).order_by(
        'created_on'
    )    
    context = {
        "Category": category,
        "posts": posts
    }
    return render(request, "app/post_category.html", context)


def Post_detail(request, pk):
    post = Post.objects.get(pk=pk)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()
    comments = Comment.objects.filter(post=post)
    context = {
        'post': post,
        "comments": comments,
        "form": form,
    }
    return render(request, "app/post_detail.html", context)


