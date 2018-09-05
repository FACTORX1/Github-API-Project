from django.shortcuts import render, HttpResponse
import requests
import json
from app.models import GithubUser

# Create your views here.

def index(request):
    return HttpResponse('Hello world')

def test(request):
    return HttpResponse('Test page')

def profile(request):
    parsedData = []
    if request.method == 'POST':
        username = request.POST.get('user')
        req = requests.get('https://api.github.com/users/' + username)
        jsonList = []
        jsonList.append(json.loads(req.content.decode('utf-8')))
        userData = {}

        try:

            for data in jsonList:
                    userData['id'] = data['id']
                    userData['name'] = data['name']
                    userData['blog'] = data['blog']
                    userData['email'] = data['email']
                    userData['public_gists'] = data['public_gists']
                    userData['public_repos'] = data['public_repos']
                    userData['avatar_url'] = data['avatar_url']
                    userData['followers'] = data['followers']
                    userData['following'] = data['following']
            parsedData.append(userData)
            SaveToDB(parsedData)
        except:
            return HttpResponse("Object Not found")
    return render(request, 'app/profile.html', {'data': parsedData})

def SaveToDB(parsedData):
    for data in parsedData:
        p1 = GithubUser.objects.get_or_create(
            user_id = data['id'],
            username = data['name'],
            blog = data['blog'],
            email = data['email'],
            followers = data['followers'],
            following = data['following'],
        )

    return True