import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DEBUG = True
ROOT_URLCONF = 'urls'
SECRET_KEY = '6o^up^px47mgp2dzoh&*_unzx2d9*gdpyn+ix4mt94y55mj!(y'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR + '/templates/',
        ],
    },
]
API_URL='http://localhost:9000/'

# Change the settings here
OAUTH_CLIENT_ID = ''
OAUTH_CLIENT_SECRET = ''
