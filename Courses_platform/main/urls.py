from django.urls import path
from .views import *
urlpatterns = [

    path('' , home , name="home"),

    path('detailed/<int:id>' , details , name ="detail"),
    path('course/update/<int:id>' , update_course , name ="update-course"),
    path('course/delete/<int:id>' , delete_course , name ="delete-course"),

    path('course/level/<str:st>' , filter_courses , name ="level"),

    path('course/category/<int:id>' , list_Category , name="catlst" ),

    path('course/create' , Create_course , name="createcourse"),
    path('categopry/create' , createCategory , name='createcat' ),
    path('category/delete/<int:id>/', deleteCategory, name="delete-category"),



]
