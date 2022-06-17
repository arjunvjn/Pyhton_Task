from django.shortcuts import render,redirect
from .models import *
from .forms import CreateStudent

# Create your views here.

count=1


# To get the all student
def list_students(request):
    stu_list=Mark.objects.all()
    return render(request,'list_student.html',{'stu_list':stu_list})

# To get a single student detail
def get_student(request,id):
    s=Student.objects.get(pk=id)
    stu=Mark.objects.get(student=s)
    return render(request,'get_student.html',{'stu':stu})

# To delete a student
def delete_student(request,id):
    stu=Student.objects.get(pk=id)
    stu.delete()
    return redirect('/list_students')

# To create a student
def create_student(request):
    global count
    if request.method=='POST':
        form=CreateStudent(request.POST,request.FILES)
        if form.is_valid():
            stu=form.save(commit=False)
            stu.stu_id='STU_'+ str(count)
            count+=1
            stu.save()
            return render(request,'')
        else:
            return render('/create_student',{'error':form.errors,'form':form})
    else:
        form=CreateStudent()
        return render(request,'create_student.html',{'form',form})

# To enter marks for a student
def enter_marks(request,id):
    if request.method=='POST':
        stu=Student.objects.get(pk=id)
        sub1=request.POST['sub1']
        sub2=request.POST['sub2']
        sub3=request.POST['sub3']
        Mark.objects.create(student=stu,sub1=sub1,sub2=sub2,sub3=sub3)
        return render(request,'enter_mark.html')

# To update a student
def  update_student(request,id):
    stu=Student.objects.get(pk=id)
    if request.method=='POST':
        form=CreateStudent(request.POST,request.FILES,instance=stu)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            return render(request,'update_student.html',{'form':form,'errors':form.errors})
    else:
        form=CreateStudent(instance=stu)
        return render(request,'update_student.html',{'form':form})

# For searching 
def search(request):
    if request.method=='POST':
        if Student.objects.filter(stu_id=request.POST['search']).exists():
            return render(request,'list_student.html',{'stu_list':Student.objects.get(stu_id=request.POST['search'])})
        elif Student.objects.filter(number=request.POST['search']).exists():
            return render(request,'list_student.html',{'stu_list':Student.objects.filter(number=request.POST['search'])})
        elif Student.objects.filter(email=request.POST['search']).exists():
            return render(request,'list_student.html',{'stu_list':Student.objects.filter(email=request.POST['search'])})