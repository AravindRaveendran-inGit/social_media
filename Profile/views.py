from django.shortcuts import render
from .models import Profile, Relationship
from .forms import profileForm


# Create your views here.

def profile_view(request):
    profile = Profile.objects.get(user=request.user)
    form = profileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm
    }

    return render(request, 'Profile/myprofile.html', context)

def invites_received_view(request):
    profile = Profile.objects.get(user=request.user)
    qs = Relationship.objects.invitations_recevied(profile)

    context={'qs':qs}
    return render(request,"Profile/my_invites.html",context)


def profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles(user)

    context={'qs':qs}
    return render(request,"Profile/profile_list.html",context)

def invite_profiles_list_view(request):
    user = request.user
    qs = Profile.objects.get_all_profiles_to_invite(user)

    context={'qs':qs}
    return render(request,"Profile/to_invite_list.html",context)





