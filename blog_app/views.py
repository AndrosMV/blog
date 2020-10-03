from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('-fecha_publicacion')
    return render(request, 'blog/post_list.html', {'contenido':posts})

def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/post_detail.html', {'contenido':post})