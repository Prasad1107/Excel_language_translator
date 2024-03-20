from django.test import TestCase
from django.conf import settings

# Create your tests here.

def handle_uploaded_file(f):
    path = settings.MEDIA_ROOT
    with open(path+ '/'+ f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)
