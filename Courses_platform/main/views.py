from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from .models import *
from .forms import *

def home(request):
    courses = Course.objects.all().order_by('start_date')
    categories = Category.objects.all()
    context = { 'tasks':courses ,
                'categories' :categories
              }
    return render(request , 'main/home.html',context)

def details(request ,id):
    

    course = get_object_or_404(Course , id=id)

    context = {
        'course':course
    }
    return render(request , 'main/detailed.html' , context)

def filter_courses(request , st):
    courses = Course.objects.filter(level = st)
    context = {
        'courses' :courses
    }
    return render(request , 'main/courselevel.html' , context)

def list_Category(request, id):
    courses = Course.objects.filter(category=id)
    categories = Category.objects.all()

    context = {
        "courses": courses,
        "categories": categories,
        "selected_category": Category.objects.get(id=id),  
    }
    return render(request, 'main/category_courses.html', context)
def Create_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid() :
            form.save()            
            return redirect('home')
    else:  
        form = CourseForm()
    return render(request , 'main/create_course.html' ,{'form' :form} )

def createCategory(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid() :
            form.save()           
            return redirect('home')
    else:  
        form = CategoryForm()
    return render(request , 'main/create_cat.html' ,{'form':form})
def update_course(request , id ):
    task = get_object_or_404(Course , id=id)
    if request.method == 'POST':
        form = CourseForm(request.POST , instance=task)
        if form.is_valid() :
            form.save()         
            return redirect('home')
    else:  
        form = CourseForm(instance=task)
    return render(request, 'main/updatecourse.html' , {'form':form})
def delete_course(request , id):
    course = get_object_or_404(Course , id=id)
    course.delete()
    return redirect('home')
def deleteCategory(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == "POST":
        category.delete()
        return redirect('home')
    return render(request, 'main/delete_category.html', {'category': category})
