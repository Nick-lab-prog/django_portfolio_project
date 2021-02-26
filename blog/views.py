from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

app_name = 'blog'

def all_blogs(request):
	blog_count = Blog.objects.count()
	blogs = Blog.objects.all() 
	#per mettere in ordine si mette invece di all order_by('-date')
	#e per limitare il numero di oggetti mostrati invece si usa una sorta di slice delle liste -> [:x]
	return render(request, 'blog/all_blogs.html', {'blogs':blogs})
def detail(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)#pk sta per primary key
	return render(request, 'blog/detail.html', {'blog':blog})
def home(request):
	return render(request, 'portfolio/home.html')