from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Travel

def home(request):
    travels = Travel.objects
    return render(request, 'home.html', {'travels':travels})

def detail(request, travel_id):
    details = get_object_or_404(Travel, pk=travel_id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    travel = Travel()
    travel.title = request.GET['title']
    travel.body = request.GET['body']
    travel.pub_date = timezone.datetime.now()
    travel.save()
    return redirect('/TravelReview/'+str(travel.id))

# Create your views here.
