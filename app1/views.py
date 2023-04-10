from django.shortcuts import render,redirect
from app1.forms import BlogForm,ReviewForm
from django.http import HttpResponse
from app1.models import Blog,Review

# Create your views here.

def BlogVW(request):
    form=BlogForm()
    if request.method=='POST':
        form=BlogForm(request.POST,)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1> data is stored </h1>')
    return render(request,'blog.html',{'form':form})

def UpdateBlog(request,pk):
    data=Blog.objects.get(id=pk)
    form=BlogForm(instance=data)
    if request.method=='POST':
        form=BlogForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
        return HttpResponse('<h1>data is updated </h1>')
    return render(request,'updateblog.html',{'form':form})

def ReadBlog(request):
    data=Blog.objects.all()
    return render(request,'read.html',{'data':data})

def ReadOne(request,pk):
    data=Blog.objects.get(id=pk)
    review=Review.objects.filter(blog=pk)
    return render(request,'ReadOne.html',{'data':data,'review':review})
 
def DeleteOne(request,pk):
    data=Blog.objects.get(id=pk)
    if request.method=='POST':
        Blog.objects.get(id=pk).delete()
        return redirect('/read/')
    return render(request,'delete.html',{'data':data})

def ReviewVW(request):
    form=ReviewForm()
    if request.method=='POST':
        form=ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/read/')
    return render(request,'review.html',{'form':form})
    
