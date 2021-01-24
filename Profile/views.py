from django.shortcuts import render
from .models import Profile
from .forms import profileForm

# Create your views here.

def profile_view(request):
    profile=Profile.objects.get(user=request.user)
    form=profileForm(request.POST or None,request.FILES or None,instance=profile)
    confirm=False

    if request.method =='POST':
         if form.is_valid():
            form.save()
            confirm=True

    context = {
        'profile':profile,
         'form':form,
         'confirm':confirm
    }

    return render(request,'Profile/myprofile.html', context)
