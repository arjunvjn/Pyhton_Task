from django.urls import path
from . import views

urlpatterns=[
    path('/',views.create_student,name='create_student'),
    path('/list_students',views.list_students,name='list_student'),
    path('/get_student/<id>',views.get_student,name='get_student'),
    path('/delete_student/<id>',views.delete_student,name='delete_student'),
    path('/enter_marks/<id>',views.enter_marks,name='enter_marks'),
    path('/update_student/<id>',views.update_student,name='update_student'),
    path('/search',views.search,name='search')
]