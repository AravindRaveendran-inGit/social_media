from .models import Profile,Relationship


def profile_avatar(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        pic = profile_obj.profile_pic
        return{'picture':pic}
    return{}

def no_invitations_received(request):
    if request.user.is_authenticated:
        profile_obj = Profile.objects.get(user=request.user)
        qs_count = Relationship.objects.invitations_recevied(profile_obj).count
        return{'invites_num':qs_count}
    return{}


