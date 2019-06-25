from django.shortcuts import render,HttpResponse
from django.views.generic import TemplateView
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Series
from .models import Articles
from django.core.paginator import Paginator

def index(request):
    art_posts=Articles.objects.all()
    return render(request,'index.html',{'articles':art_posts})

# class Articlemain(ListView,request):
#     template_name='article/article_main.html'
#     context_object_name='articles'
#     ordering=['-date_posted']
#     paginate_by = 5
    
def indexA(request):
    article_list=Articles.objects.all()
    paginator=Paginator(article_list,6)
    page=request.GET.get('page')
    articles=paginator.get_page(page)
    
    return render(request,'article/article_main.html',{'articles':articles})


class PostListView(ListView):
    model=Articles
    template_name='index.html'
    context_object_name='articles'
    ordering=['-date_posted']

class ArticleDetialView(DetailView):
    model=Articles
    template_name='article/article_detail.html'

class ArticleCreateView(LoginRequiredMixin,CreateView):
    model=Articles
    template_name='article/article_form.html'
    fields=['title','content']

    def form_valid(self,form):
        form.instance.auther =self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model=Articles
    template_name='article/article_form.html'
    fields=['title','content']

    def form_valid(self,form):
        form.instance.auther =self.request.user
        return super().form_valid(form)

    def test_func(self):
        article=self.get_object()
        if self.request.user == article.auther:
            return True
        return False    

class ArticleDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Articles
    template_name='article/article_confirm_delete.html'
    success_url='/'
    def test_func(self):
        article=self.get_object()
        if self.request.user == article.auther:
            return True
        return False    

class Seri(TemplateView):

    def get(self,request):

        series=Series.objects.all()
        return render(request,'series.html',{'series':series})


def seriesDetail(request,slug):
    des=Series.objects.get(pk=slug)
    return render(request,'seriesDetail.html',{'des':des,})