import requests
from django.shortcuts import render
from django.conf import settings

def oauthtest(request):
    return render(request, 'oauthtest.html', {
        'link': '{}o/authorize/?response_type=code&client_id={}&redirect_uri={}{}/oauthdone/'.format(
            settings.API_URL,
            settings.OAUTH_CLIENT_ID,
            'https://' if request.is_secure() else 'http://',
            request.META['HTTP_HOST'],
        )
    })

def oauthdone(request):
    # Get token
    r = requests.post(settings.API_URL + 'o/token/', data={
        'grant_type': 'authorization_code',
        'code': request.GET['code'],
        'redirect_uri': '{}{}/oauthdone/'.format('https://' if request.is_secure() else 'http://', request.META['HTTP_HOST']),
        'client_id': settings.OAUTH_CLIENT_ID,
        'client_secret': settings.OAUTH_CLIENT_SECRET,
    })
    oauth = r.json()
    # Get user object + accounts
    headers = {
        'Authorization': oauth['token_type'] + ' ' + oauth['access_token'],
    }
    r = requests.get(settings.API_URL + 'api/users/me/?expand_accounts=True', headers=headers)
    return render(request, 'accounts.html', {
        'user': r.json(),
    })
