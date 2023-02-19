from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *




#FBV for returning string as response
def fbv_string(request):
    return HttpResponse('this is function based viwe string')

#CBV for returnig  string  as response
class cbv_string(View):
    def get(self,request):
        return HttpResponse('cbv string')
    
#FBV to render html file and send context data
def fbv_htmlpage(request):
    d={'name':'bheema'}
    return render(request,'fbv_htmlpage.html',d)


#CBV to  render html file and send context data
class cbvhtmlpage(View):
     def get(self,request):
        d={'name':'malli'}
        return render(request,'cbvHtmlPage.html',d)
     
#FBV to handle the djangoforms
def fbv_djangoform(request):
    SFO=StudentForm()
    d={'sfo':SFO}

    if request.method=='POST':
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))
    return render(request,'fbv_djangoform.html',d)    

#CBV to handle the djangoforms
class CbvDjangoForm(View):
    def get(self,request):
        SFO=StudentForm()
        d={'SFO':SFO}
        return render(request,'CbvDjangoForm.html',d)
    
    def post(self,request):
        sfd=StudentForm(request.POST)
        if sfd.is_valid():
            return HttpResponse(str(sfd.cleaned_data))



