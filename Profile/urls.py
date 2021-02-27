from django.urls import path

from .views import (profile_view, invites_received_view, profiles_list_view, invite_profiles_list_view, ProfileListView, send_invitation
                    ,remove_from_friends)

app_name = 'profileapp'

urlpatterns =[
path('myprofile/',profile_view, name = 'my-profile'),
path('my-invites/',invites_received_view,name="my-invites-view"),
path('all-profiles/',ProfileListView.as_view(),name="profiles-lists-view"),
path('to-invite/',invite_profiles_list_view,name="to-invite-lists-view"),
path('send-invite/',send_invitation,name="send-invite"),
path('remove-friend/',remove_from_friends,name="remove-friend"),
]