from django.shortcuts import render
from .models import Blog 
# Create your views here.
def all_blogs(request):
	blogs = Blog.objects.all() 
	#per mettere in ordine si mette invece di all order_by('-date')
	#e per limitare il numero di oggetti mostrati invece si usa una sorta di slice delle liste -> [:x]
	return render(request, 'blog/all_blogs.html', {'blogs':blogs})
def home(request):
	return render(request, 'home.html', name="home")