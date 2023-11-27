from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from django.utils import timezone
from django.db.models import Q
from blogs.models import Post, Categorias

# Create your views here.

def home_page(request):
   posts= Post.objects.filter(
      pub_date__lte=timezone.now()
   )
   categorias= Categorias.objects.all()
   featured = Post.objects.filter(featured= True).filter(
      pub_date__lte=timezone.now()
   )[:3]

   context = { 
        'posts':posts,
        'categorias':categorias,
        'destacados': featured
        
   }

   return render(request, 'blogs/home_page.html', context=context)

class PostDetailView(generic.DetailView):
    model = Post
    query = Post.objects.filter(featured= True).filter(
        pub_date_lte=timezone.now()
    )
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all()
        return context
    
class FeaturedListView(generic.ListView):
   model = Post 
   template_name = 'blogs/results.html'

   def get_queryset(self):
      query = Post.objects.filter(featured= True).filter(
         pub_date_lte= timezone.now()
      )

      return query
   
   def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all()
        return context
   
class CategoryListView(generic.ListView):
    model = Post
    template_name = 'blogs/results.html'
    
    def get_queryset(self):
      query = self.request.path.replace('/categorias/', '')
      print(query)
      posts = Post.objects.filter(Categorias_slug=query).filter(
         pub_date_lte= timezone.now()
      )

      return posts
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categorias'] = Categorias.objects.all()
        return context
    
class SearchResultsView(generic.ListView):
   model = Post 
   template_name = 'blogs/results.html'

   def get_queryset(self):
      query = self.request.GET.get("search")
      posts = Post.objects.filter(
         Q (title_icontains=query) | Q(Categoriastitle_icontains=query)
      ).filter(
         pub_date__lte= timezone.now()
      )
      return posts
      
   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)   
      context['categorias'] = Categorias.objects.all()  
      return context