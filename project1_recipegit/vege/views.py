from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from django.core.paginator import Paginator
from django.db.models import Q, Sum

@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        
        data = request.POST
        recipe_name = data.get('recipe_name')
        recipe_description = data.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')
        
        Recipe.objects.create(
             recipe_name = recipe_name,
             recipe_description = recipe_description,
             recipe_image = recipe_image,
        )
        return redirect('/recipes/')
    queryset = Recipe.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recipe_name__icontains = request.GET.get('search'))
    context = {'recipes' : queryset}
    return render(request , 'recipes.html' , context)
 
 

def home(request):
    return render(request, 'home.html', {'page': 'home'})

def base(request):
    return render(request, 'base.html', {'page': 'base'})

def delete_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    recipe.delete()
    return redirect('/recipes/')

def update_recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id)
    
    if request.method == 'POST':
        recipe.recipe_name = request.POST.get('recipe_name')
        recipe.recipe_description = request.POST.get('recipe_description')

        if 'recipe_image' in request.FILES:
            recipe.recipe_image = request.FILES['recipe_image']
        
        recipe.save()
        return redirect('/recipes/')
    
    context = {'page': 'recipes', 'recipe': recipe}
    return render(request, 'update_recipe.html', context)

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.info(request, "Invalid Username")
            return render(request, "login.html")
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.info(request, "Invalid Credentials")
            return redirect('/login/')
        
        else:
            login(request, user)
            return redirect('/recipes/')
        
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not first_name or not last_name or not username or not password:
            messages.error(request, "All fields are required.")
            return render(request, "register.html")

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already exists.")
            return render(request, "register.html")

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
        ) 
        
        user.set_password(password)
        user.save()
        
        messages.info(request, 'Account created successfully')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/recipes/')
        
    return render(request, "register.html")

@login_required(login_url='/login/')
def add_recipe(request):
    if request.method == 'POST':
        recipe_name = request.POST.get('recipe_name')
        recipe_description = request.POST.get('recipe_description')
        recipe_image = request.FILES.get('recipe_image')

        recipe = Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image
        )
        recipe.save()
        return redirect('/recipes/')
        
    
    context = {'page': 'recipes', 'recipe': recipe}
    return render(request, 'recipe.html' ,)
