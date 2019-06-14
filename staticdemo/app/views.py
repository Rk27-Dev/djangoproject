from django.shortcuts import render
from .forms import staticforms
from .models import registermodel
from .forms import registerform,nameform,ageform,gfnameform
# Create your views here.
def home(request):
    return render (request,'home.html')
def tqs(request):
    return  render(request,'tqs.html')
def staticview(request):
    form=staticforms()
    if request.method=='POST':
        form=staticforms(request.POST)
        if form.is_valid():
            print('form is valied ..printg the data')
            print('name:',form.cleaned_data['name'])
            print('rollno:', form.cleaned_data['rollno'])
            print('email:', form.cleaned_data['email'])
            print('address:', form.cleaned_data['address'])
            return tqs(request)
    return render(request,'staticview.html',{'form':form})

def registerview(request):
    form=registerform()
    if request.method=='POST':
        form=registerform(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print('data inserted succsessfully')
    return render(request,'register.html',{'form':form})
def display(request):
    data=registermodel.objects.all()
    return render(request,'register.html',{'data':data})




import json
from django.http import HttpResponse
# ## context display
def cont(request):
    data={
        'name':'ravi',
        'age':27,
        'sal':15000,
        'dept':'python'
    }
    json_data=json.dumps(data)
    return HttpResponse(json_data,content_type='application/jason')


### session management
def session_view(request):
    count=request.session.get('count',0)
    newcount=count+1
    request.session['count']=newcount
    print(request.session.get_expiry_age())
    print(request.session.get_expiry_date())
    print(request.session.set_expiry(50))
    return render(request,'count.html',{'count':newcount})


##session API

def name_view(request):
    form=nameform()
    return  render(request,'name.html',{'form':form})
def age_view(request):
    form=ageform()
    name=request.GET['name']
    request.session['name']=name
    return  render(request,'age.html',{'form':form})
def gf_view(request):
    age=request.GET['age']
    request.session['age']=age
    form=gfnameform()
    return  render(request,'gf.html',{'form':form})
def result_view(request):
    gf=request.GET['gf']
    request.session['gf']=gf
    request.session.set_expiry(20)
    return  render(request,'result.html')
