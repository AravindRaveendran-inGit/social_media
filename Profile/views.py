
from django.shortcuts import render
from django.http import HttpResponse
from .models import Profile

# Create your views here.

def profile_view(request):
    profile = Profile.objects.get(user = request.user)

    context = {
        'profile' : profile
    }

    return render(request,'Profile/myprofile.html',context)



