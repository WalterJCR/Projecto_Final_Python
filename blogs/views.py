from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic


from blogs.models import Post, Categorias

# Create your views here.

def home_page(request):
    posts = Post.objects.all()
    categorias = Categorias.objects.all()
    featured = Post.objects.filter(featured= True)[:3]

    context = { 
        'posts':posts,
        'categorias':categorias,
        'destacados': featured
        
    }

    return render(request, 'blogs/home_page.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post
    
