from django.test import TestCase

# Create your tests here.

def handle_uploaded_file(f):  
    with open('F:\Python\Demo_project\media\\'+f.name, 'wb+') as destination:  
        for chunk in f.chunks():  
            destination.write(chunk)