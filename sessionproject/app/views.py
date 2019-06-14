from django.shortcuts import render

# Create your views here.
from .forms import Additem
def additem_view(request):
    form=Additem()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
        request.session.set_expiry(120)
    return render(request,'additem.html',{'form':form})
def display_view(request):
    return render(request,'displayitem.html')
def session_info_view(request):
    session=request.session
    age=session.get_expiry_age()
    date=session.get_expiry_date()
    print('age',age)
    print('date',date)
    return  render(request,'additem.html')
def session_delete(request):
    request.session.delete(session_key="")