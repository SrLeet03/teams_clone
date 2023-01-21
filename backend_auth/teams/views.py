from django.shortcuts import render
from .models import *
import uuid
from django.http import JsonResponse

# Create your views here.

def create_team(request):
    try:
        title = request.data['title']
        namespace = uuid.UUID('12345678-1234-1234-1234-123456789012')
        name = title
        uid = uuid.uuid5(namespace, name)

        teams.objects.create(
            name = title,
            uid = uid
        )
        
        return JsonResponse({
            'status':200,
            'msg':'created team'
        })
    except Exception as e:
        return JsonResponse({
            'status':400,
            'msg':str(e)
        })
        
def add_member_to_team(request):
    try:
        user = request.data['userid']
        team = request.data['uid']
        
        user = User.objects.get(username = user)
        team = teams.objects.get(uid = team)
        if teams.objects.filter(members=user).exists():
            return JsonResponse({
            'status':400,
            'msg':'user is already a team member'
           })

        team.members.add(user)
        team.save()
        return JsonResponse({
            'status':200,
            'msg':'added member to team'
        })
    except Exception as e:
        return JsonResponse({
            'status':400,
            'msg':str(e)
        })
        