from django.conf.urls import patterns , url , include
from django.views.generic import ListView , DetailView
from blog.models import Post
import  itertools

urlpatterns= patterns ('',

 url (r'^$',ListView.as_view(queryset=Post.objects.all().order_by("-date")[:10],template_name="blog.html")),
  url (r'^(?P<pk>\d+)$',DetailView.as_view(model = Post,template_name="post.html")),
    url(r'^permutate$','blog.views.PermutatenString', name='name'),
     url(r'^resultpage$','blog.views.resultPage',name='result.html'),
)
