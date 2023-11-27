from django.urls import path

from blogs import views

app_name = 'blogs' 

urlpatterns = [
    path('', views.home_page),
    path('post/<slug:slug>', views.PostDetailView.as_view(), name='post'),
    path('featured/', views.FeaturedListView.as_view(), name='featured'),
    path('Categorias/<slug:slug>', views.CategoryListView.as_view(), name='categoria'),
    path ('search/' , views.SearchResultsView.as_view() , name='search'),
]
