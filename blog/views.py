from http.client import HTTPResponse
from lib2to3.fixes.fix_input import context
from msilib.schema import ListView

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView

from .models import News, Category, Tags, BreakingNews, Newslatter, Flickr
from .forms import NewsForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.
# 👉---------------------------Pages------------------------------👈

def index(request):
    news = News.objects.all().order_by('sort_time')
    breakingNews = BreakingNews.objects.all().order_by('sort_time')
    carousel= news.filter(tags= Tags.objects.get(name = "carousel"))
    tranding= news.filter(tags= Tags.objects.get(name = "tranding"))
    feature= news.filter(tags= Tags.objects.get(name = "feature"))
    latest= news.filter(tags= Tags.objects.get(name = "latest"))
    category = Category.objects.all()
    # none = News.objects.get(id = 1)
    flickr = Flickr.objects.all()


    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Qabul qilindi</h1>")
    else:
        form = NewsForm()

    context = {
        'news':news,
        # 'none': none,
        'carousel': carousel,
        'tranding': tranding,
        'latest': latest,
        'feature': feature,
        'brakingNews': breakingNews,
        'category': category,
        "form": form,
        'flickr': flickr
    }

    return render(request, 'pages/index.html', context=context)

def contact(request):
    flickr = Flickr.objects.all()
    category = Category.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        form1 = CommentForm(request.POST)
        if form.is_valid():
            form.save()

            return HttpResponse("<h1>Qabul qilindi</h1>")
        if form1.is_valid():
            form1.save()
            return HttpResponse("<h1>Qabul qilindi</h1>")
    else:
        form = NewsForm()
        form1 = CommentForm()

    context = {
        'form': form,
        'flickr': flickr,
        'category': category,
        'form1': form1
    }
    return render(request, 'pages/contact.html', context=context)

def category(request, id):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Qabul qilindi</h1>")
    else:
        form = NewsForm()
    if id == 0 :
        name = 0
        news = News.objects.all().order_by('sort_time')
        tranding = news.filter(tags=Tags.objects.get(name="tranding"))
        feature = news.filter(tags=Tags.objects.get(name="feature"))
        latest = news.filter(tags=Tags.objects.get(name="latest"))
        category = Category.objects.all()
        flickr = Flickr.objects.all()
        context = {
            'name': name,
            'tranding': tranding,
            'latest': latest,
            'feature': feature,
            'category': category,
            'form': form,
            'flickr': flickr
        }
    else:
        name = Category.objects.get(id =id)
        news = News.objects.all().order_by('sort_time').filter(category= name)
        tranding = news.filter(tags=Tags.objects.get(name="tranding"))
        feature = news.filter(tags=Tags.objects.get(name="feature"))
        latest = news.filter(tags=Tags.objects.get(name="latest"))
        category = Category.objects.all()
        flickr = Flickr.objects.all()
        context = {
            'name': name,
            'tranding': tranding,
            'latest': latest,
            'feature': feature,
            'category': category,
            'form': form,
            'flickr': flickr
        }


    return render(request, 'pages/category.html', context=context)

def single(request):
    flickr = Flickr.objects.all()
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Qabul qilindi</h1>")
    else:
        form = NewsForm()

    new = News.objects.all()[1]
    news = News.objects.all().order_by('sort_time')
    tranding = news.filter(tags=Tags.objects.get(name="tranding"))
    category = Category.objects.all()
    context = {
        'new': new,
        'tranding': tranding,
        'category': category,
        'form': form,
        'flickr': flickr
    }

    return render(request, 'pages/single.html', context=context)

# 👉---------------------------Pages end------------------------------👈


# 👉---------------------------Detail------------------------------👈

def detail(request, slug):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("<h1>Qabul qilindi</h1>")
    else:
        form = NewsForm()

    new = get_object_or_404(News, slug= slug)
    news = News.objects.all().order_by('sort_time')
    tranding = news.filter(tags=Tags.objects.get(name="tranding"))
    category = Category.objects.all()
    flickr = Flickr.objects.all()
    context = {
        'new': new,
        'tranding': tranding,
        'category': category,
        'form': form,
        'flickr': flickr
    }
    return render(request, 'detail/NewsDetail.html', context=context)


# 👉---------------------------Detail end------------------------------👈

# 👉---------------------------update create delete ---------------------👈

class NewsCreateView(CreateView):
    model = News
    template_name = 'views/addNews.html'
    fields = ['title', 'body', 'img', 'tags', 'category','slug' ]
    success_url = reverse_lazy('index')


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'views/updateView.html'
    fields = ['title', 'body', 'img', 'tags', 'category' ]
    success_url = reverse_lazy('index')


class NewsDeleteView(DeleteView):
    model = News
    template_name = 'views/deleteView.html'
    success_url = reverse_lazy('index')


# 👉---------------------------update create delete end---------------------👈








