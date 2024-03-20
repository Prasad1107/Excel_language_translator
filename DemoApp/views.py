from django.shortcuts import render, redirect
from django.core.files import File
from django.http import HttpResponse
from django.template import Context,Template
from django.conf import settings 
from .forms import FileForm
from .tests import handle_uploaded_file
from .translator import language_translator


filename = writepath = trans1 = ''
def index(request):  
    if request.method == 'POST':
        global filename, writepath, trans1  
        file1 = FileForm(request.POST, request.FILES)
        if file1.is_valid():
            print("success")
            handle_uploaded_file(request.FILES['file'])
            lang = request.POST.get('language')
            filename = request.FILES['file'].name
            filetype = file_type_identifier(filename)
            print(filetype)
            path = settings.MEDIA_ROOT
            doc = (f"{path}"+"/"+ f"{filename}")
            print(doc)
            writepath = settings.MEDIA_ROOT +"/"+f"translated_{filename}"
            print(writepath)
            trans1 = language_translator(doc, lang, filetype, filename, writepath)
            translate =  trial(filetype, request)
            return translate
            

              
    else:  
        file1 = FileForm()  
        return render(request,"index.html",{'form':file1})

#function to identify filetype
def file_type_identifier(filename):
    f_extns = filename.split(".")
    filetype = f_extns[-1]
    return filetype

#function to run translator according to filetype
def trial(filetype, request):
    file1 = FileForm(request.POST, request.FILES)
    if filetype == 'xlsx':
        trans1.excel_translator()
        return render(request, 'upload.html',{'filename' : filename})
    elif filetype == 'txt':
        trans1.txt_translator()
        return render(request, 'upload.html',{'filename' : f'translated_{filename}'})
    else:
        return render(request,"index2.html",{'form':file1})
