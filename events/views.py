from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from .models import Event, Category, Koszyk
from .forms import EventForm, CategoryForm
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from opencage.geocoder import OpenCageGeocode
import datetime

def index(request):
    latest_news_list = Event.objects.order_by('-pub_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(latest_news_list, 10)
    numofnews = len(Event.objects.all())
    categories = Category.objects.all()
    timenow = timezone.now()
    nadch = Event.objects.filter(data__gt=timenow.now())
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
            'latest_news_list': latest_news_list,
            'Title': Event.title,
            'Data': Event.data,
            'Place': Event.place,
            'description': Event.description,
            'numofnews': numofnews,
            'category': Category.name,
            'categories': categories,
            'nadch': nadch,
    }

    return render(request, 'events/main_page.html', context)

def index2(request):
    latest_news_list = Event.objects.order_by('-pub_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(latest_news_list, 10)
    numofnews = len(Event.objects.all())
    categories = Category.objects.all()
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
            'latest_news_list': latest_news_list,
            'Title': Event.title,
            'Data': Event.data,
            'Place': Event.place,
            'description': Event.description,
            'numofnews': numofnews,
            'users': users,
            'category': Category.name,
            'categories': categories,
    }

    return render(request, 'profil.html', context)


def events(request):
    latest_news_list = Event.objects.order_by('-pub_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(latest_news_list, 10)
    numofnews = len(Event.objects.all())
    categories = Category.objects.all()
    timenow = timezone.now()
    #nadch = Event.objects.filter(pub_date__range=[timenow.now(), Event.objects.all().values('data')])
    nadch = Event.objects.filter(data__gt=timenow.now())
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
            'latest_news_list': latest_news_list,
            'Title': Event.title,
            'Data': Event.data,
            'Place': Event.place,
            'description': Event.description,
            'numofnews': numofnews,
            'category': Category.name,
            'categories': categories,
            'users': users,
            'timenow': timenow,
            'nadch': nadch,

    }

    return render(request, 'events/all_events.html', context)

def create(request):

    if request.method == "POST":
        form = EventForm(request.POST)
        #adding = Event()

        #adding.title = request.POST.get("Title")
        #adding.data = request.POST.get("Data")
        #adding.place = request.POST.get("Place")
        #adding.country = request.POST.get("Country")
        #adding.save()



        if form.is_valid():
            event = form.save(commit=False)

            event.pub_date = timezone.now()
            event.likes = 0
            event.save()
            return HttpResponseRedirect("/events/")
    else:
        form = EventForm()
    context = {'form': form}

    return render(request, 'add_event.html', context)

def createCategory(request):

    if request.method == "POST":
        form = CategoryForm(request.POST)

        if form.is_valid():
            cat = form.save(commit=False)

            #event.pub_date = timezone.now()
            #event.likes = 0
            cat.save()
            return HttpResponseRedirect("/events/")
    else:
        form = CategoryForm()
    context = {'form': form}

    return render(request, 'add_category.html', context)


def search(request):
    template = 'events/all_events.html'

    categories = Category.objects.all()
    numofnews = len(Event.objects.all())


    query = request.GET.get('q')

    result = Event.objects.filter(Q(title__contains=query) | Q(description__contains=query) | Q(place=query))

    page = request.GET.get('page', 1)
    paginator = Paginator(result, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'result': result,
        'page': page,
        'paginator': paginator,
        'users': users,

        'numofnews': numofnews,
        'category': Category.name,
        'categories': categories,

    }
    return render(request, template, context)


def search_by_date(request):
    template = 'events/all_events.html'

    categories = Category.objects.all()
    numofnews = len(Event.objects.all())


    query = request.GET.get('q')

    result = Event.objects.filter(Q(data__contains=query))

    page = request.GET.get('page', 1)
    paginator = Paginator(result, 10)
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
        'result': result,
        'page': page,
        'paginator': paginator,
        'users': users,

        'numofnews': numofnews,
        'category': Category.name,
        'categories': categories,

    }
    return render(request, template, context)


def listofcategories(request, pk):
    categories = Category.objects.all()
    post = Event.objects.all()
    category = get_object_or_404(Category, pk=pk)
    post = post.filter(category=category)
    template = 'events/listofcategories.html'
    context = {
        'categories': categories,
        'post': post,
        'category': category
    }
    return render(request, template, context)


def detail(request, news_id):

    event = Event.objects.get(pk=news_id)
    category = Category.objects.all()

    return render(request, 'events/detail.html', {'events': event, 'category': category })


def likepost(request, news_id):
    obj = get_object_or_404(Event, id=news_id)
    if request.method == "POST":
        obj.likes = obj.likes + 1
        obj.save()
    return HttpResponseRedirect("../")


def calendar(request):
    categories = Category.objects.all()
    event = Event.objects.all()

    context = {
        'categories': categories,
        'event': event,
    }
    return render(request, 'events/calendar.html', context)


def fanpage(request):
    categories = Category.objects.all()
    event = Event.objects.all()

    context = {
        'categories': categories,
        'event': event,
    }
    return render(request, 'events/fanpage.html', context)

def koszyk(request):
    latest_news_list = Event.objects.order_by('-pub_date')

    page = request.GET.get('page', 1)
    paginator = Paginator(latest_news_list, 10)
    numofnews = len(Event.objects.all())
    categories = Category.objects.all()
    zaplanowane = Koszyk.objects.all()
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        users = paginator.page(1)
    except EmptyPage:
        users = paginator.page(paginator.num_pages)
    context = {
            'latest_news_list': latest_news_list,
            'Title': Event.title,
            'Data': Event.data,
            'Place': Event.place,
            'description': Event.description,
            'numofnews': numofnews,
            'users': users,
            'category': Category.name,
            'categories': categories,
            'zaplanowane': zaplanowane,
    }

    return render(request, 'events/koszyk.html', context)


def koszyk_add(request, pk):
    event = get_object_or_404(Event, pk=pk)
    koszyk = Koszyk.objects.filter(user=request.user, event=event).first()
    if not koszyk:
        koszyk = Koszyk(user=request.user, event=event)
        #koszyk.user = request.user
        #koszyk.event = event
        koszyk.quantity += 1
        koszyk.save()
    return HttpResponseRedirect(reverse('koszyk'))


def delete_koszyk(request, pk):
    obj = get_object_or_404(Koszyk, id=pk)
    if request.method == "POST":
        obj.delete()

    return HttpResponseRedirect("../../koszyk/")