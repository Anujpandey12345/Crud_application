from django.shortcuts import render,redirect
from .models import *
# Create your views here.
def InsertPageView(request):
    return render(request, 'crud/insert.html')


def InsertData(request):
    #Data Come from HTML to Views
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    contact = request.POST['contact']
    #create object of model class
    #inserting Data into Table
    newUser = Student.objects.create(Firstname=fname,Lastname = lname,Email=email,Contact=contact)

    return redirect('showdata')
# Show Data from the urls
def ShowData(request):
    #SELECT * FROM Table name 
    #fetch all data from the table
    all_data = Student.objects.all()
    return render(request, 'crud/show.html',{'key1' : all_data})


def EditPage(request,pk):
    get_data = Student.objects.get(id=pk)
    return render(request,"crud/edit.html",{'key2' : get_data})

def UpdateData(request,pk):
    udata = Student.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Contact = request.POST['contact']

    udata.save()
    return redirect('showdata')

def DeleteData(request,pk):
    ddata = Student.objects.get(id=pk)
    ddata.delete()
    return redirect('showdata')