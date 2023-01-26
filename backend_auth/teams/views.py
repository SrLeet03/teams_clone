from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view
import uuid
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
@api_view(["POST"])
def create_team(request):
    try:
        title = request.data['title']
        namespace = uuid.UUID('12345678-1234-1234-1234-123456789012')
        name = title
        uid = uuid.uuid5(namespace, name)
        user_id = request.data['username']
        user = User.objects.get(username = user_id)
        Team.objects.create(
            name = title,
            uid = uid,
            created_by = user
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
<<<<<<< HEAD
        team = teams.objects.get(uid = team)
=======
        team = User.objects.get(uid = team)
>>>>>>> 3abf081e60c96a2e5856ee5c4fba02d6b981aae4
        if teams.objects.filter(members=user).exists():
            return JsonResponse({
            'status':400,
            'msg':'user is already a team member'
<<<<<<< HEAD
           })
=======
          })
>>>>>>> 3abf081e60c96a2e5856ee5c4fba02d6b981aae4

        team.members.add(user)
        team.save()
        return JsonResponse({
            'status':200,
            'msg':'added member  to team'
        })
    except Exception as e:
        return JsonResponse({
            'status':400,
            'msg':str(e)
        })
        
