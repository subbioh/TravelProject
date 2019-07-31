from django.shortcuts import render
from .models import Reviewmore



def reviewmore(request):
    reviewmores = Reviewmore.objects
    return render(request, 'reviewmore.html', {'reviewmores':reviewmores})
# Create your views here.
