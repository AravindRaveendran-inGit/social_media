from django.urls import path

from .views import (profile_view, invites_received_view, profiles_list_view, invite_profiles_list_view,ProfileDetailView, ProfileListView, send_invitation
                    ,remove_from_friends, accept_invitations, reject_invitations)

app_name = 'profileapp'

urlpatterns =[
path('',ProfileListView.as_view(),name="profiles-lists-view"),
path('myprofile/',profile_view, name = 'my-profile'),
path('my-invites/',invites_received_view,name="my-invites-view"),
path('to-invite/',invite_profiles_list_view,name="to-invite-lists-view"),
path('send-invite/',send_invitation,name="send-invite"),
path('remove-friend/',remove_from_friends,name="remove-friend"),
path('<slug>/',ProfileDetailView.as_view(),name="profile-detail-view"),
path('my-invites/accept-request/',accept_invitations,name="accept-request"),
path('my-invites/cancel-request/',reject_invitations,name="cancel-request"),

]