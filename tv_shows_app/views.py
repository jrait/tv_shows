from django.shortcuts import render,redirect

from tv_shows_app.models import Shows 

# Create your views here.

def root(request):
    return redirect('/shows')

def index(request):
    context = {
        'all_shows': Shows.objects.all(),
    }
    return render(request,'index.html',context)

def new(request):
    return render(request,'new.html')

def create(request):
    Shows.objects.create(title = request.POST['title'],network = request.POST['network'],release_date = request.POST['release_date'],desc = request.POST['desc'])
    return redirect('/shows')

def delete(request,delete_id):
    show = Shows.objects.get(id = delete_id)
    show.delete()
    return redirect('/shows')

def info(request,info_id):
    context = {
        'show' : Shows.objects.get(id = info_id)
    }
    return render(request,'info.html',context)

def edit(request,edit_id):
    
    context = {
        'show' : Shows.objects.get(id = edit_id)
    }
    return render(request,'edit.html',context)

def edit_show(request,edit_id):
    show = Shows.objects.get(id = edit_id)
    show.title = request.POST['title']
    show.nework = request.POST['network']
    show.release_date = request.POST['release_date']
    show.desc = request.POST['desc']
    show.save()
    return redirect('/shows')
