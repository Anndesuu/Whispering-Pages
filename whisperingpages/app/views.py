from django.shortcuts import render, redirect
from .forms import newRecipeForm, diaryentry
from .models import newRecipe, ent

def home(request):
   
    return render(request, "home.html")

def page(request):
        form = ent.objects.all() 
        context = {
            'items': form,
        }
        return render(request, "page.html", context)

def sharerecipe(request):
    entry = diaryentry
    return render(request, "addrecipe.html", {'entry':entry})

def addrecipe(request):
    if request.method == "POST":
        form = diaryentry(request.POST) 
        if form.is_valid():
            form.save()
            return redirect('page')

def recipe(request, recipeid):
    recipe = ent.objects.get(pk=recipeid)
    return render(request, 'recipepage.html', {'recipe': recipe})

def delete(request, id):
    entry = ent.objects.get(id=id)
    entry.delete()
    return redirect('page')

def update(request, id):
    entry = ent.objects.get(pk=id)
    if request.method == "POST":
        form = diaryentry(request.POST, instance=entry)
        if form.is_valid():
            form.save()
            return redirect('page')    
    else:
        form = diaryentry(instance=entry)
    return render(request, 'update.html', {'entry': entry, 'form': form})


# def update(request, id):
#     entry = ent.objects.get(pk=id)
#     form = diaryentry(instance=entry)
    
#     if request.method == "POST":
#         entry = diaryentry(request.POST, instance=entry)
#         if entry.is_valid():
#             entry.save()
#             return redirect('page')    
#         else: 
#             entry = diaryentry()
#     return render(request, 'update.html', {'entry': entry})

