from django.shortcuts import render , redirect
from .models import Student ,mystudent,Class,Professor,Subject,Others,Salary,Expenses
from django.contrib import messages
from django.contrib.auth.models import User
from accounts.models import School_Detail
from datetime import date,datetime
from django.core.files.storage import FileSystemStorage
from .forms import *
from django.contrib.auth import login, authenticate
from django.template.loader import get_template
from .utils import render_to_pdf
from django.db.models import Count,Q
from datetime import datetime
import requests
import pandas as pd
import io
import csv
# from .file_handle import handle_image_file
# Create your views here.

from django.http import HttpResponse
def index(request):
    studs=len(Student.objects.all())
    profs=len(Professor.objects.all())
    total_class=len(Class.objects.all())

    return render(request,'index.html',{'studs':studs,'profs':profs,'total_class':total_class})


def index1(request , name):
    if request.user.is_authenticated:
        user = User.objects.get(username=name)
        id = user.id
        if request.method=='POST':
            user = User.objects.get(id=id)
            print(user.username)
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            school_name = request.POST['school_name']
            school_code = request.POST['school_code']
            
            user.username=username
            user.first_name=first_name
            user.last_name=last_name
                
            user.save()
            school = School_Detail.objects.get(user_id=id)
            
            school.school_name =school_name
            school.school_code =school_code
            school.image = request.FILES['image']
            school.school_category = request.POST['school_category']
                    
            school.save()
            studs=Student.objects.filter(user_id=id).count()
            profs=Professor.objects.filter(user_id=id).count()
            total_class=Class.objects.filter(user_id=id).count()
            profile = School_Detail.objects.get(user_id=id)
            schools = School_Detail.objects.all()
            return render(request,'index-1.html',{'profile':profile,'studs':studs,'profs':profs,'total_class':total_class,'schools':schools})
        else:
            studs=Student.objects.filter(user_id=id).count()
            profs=Professor.objects.filter(user_id=id).count()
            total_class=Class.objects.filter(user_id=id).count()
            profile = School_Detail.objects.get(user_id=id)
            if profile.image is None:
                profile.image='1'
            schools = School_Detail.objects.all()
            for school in schools:
                if school.image is None:
                    school.image='1'
            return render(request,'index-1.html',{'profile':profile,'studs':studs,'profs':profs,'total_class':total_class,'schools':schools})
    else:
        return redirect('404-page')
def index2(request):
    return render(request,'index-2.html')

# Professor

def all_professors(request):
    professor = Professor.objects.all()
    return render(request,'Professor/all-professors.html',{'professor' : professor})
def  add_professor(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method == 'POST':
        if User.objects.filter(id=userid).exists():
            name = request.POST['name']
            f_Name = request.POST['f_Name']
            contact1 = request.POST['contact1']
            contact2 = request.POST['contact2']
            address = request.POST['address']
            if request.POST['dob'] != '':
                print("I'm Here"+request.POST['dob'])
                d = datetime.strptime(request.POST['dob'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                dob = d
            if request.POST['joining_date'] != '':
                d2 = datetime.strptime(request.POST['joining_date'], '%m/%d/%Y')
                d2.strftime('%Y/%m/%d')
                joining_date = d2
            religion = request.POST['religion'] 
            current_class = request.POST['current_class']
            section = request.POST['section']
            subject = request.POST['subject']
            shift = request.POST['shift']
            gender = request.POST['gender']
            age = request.POST['age']
            cnic = request.POST['cnic']
            experience = request.POST['experience']
            education_level = request.POST['education_level']
            bank_name = request.POST['bank_name']
            branch_code = request.POST['branch_code']
            account_number = request.POST['account_number']
            email = request.POST['email']
            status = request.POST['status']
            
            image = request.FILES.get('image',False)
            if Professor.objects.filter(name=name,f_Name=f_Name).exists():
                print("User Exist")
            elif Class.objects.filter(classname=request.POST['current_class'],section=request.POST['section']).exists() == False:
                messages.error(request,'Class Does not exist Please Add Class First!')
            else:
                myclass = Class.objects.get(classname=request.POST['current_class'],section=request.POST['section'])
                classid=myclass.id
            if Subject.objects.filter(classid_id=classid,subject=subject).exists() == False:
                messages.error(request,'Subject Does not exist in this class Please Add subject First into the Respected Class!')
            else:
                mysubject = Subject.objects.get(classid_id=classid,subject=subject)
                subjectid = mysubject.id


                print(request.POST['current_class'])
                print(request.POST['section'])
                professor = Professor(  
                name=name,
                f_Name=f_Name,
                contact1 = contact1,
                contact2 = contact2,
                address = address,
                dob = dob,
                joining_date = joining_date,
                religion = religion,
                shift = shift,
                gender = gender,
                age = age,
                cnic = cnic,
                experience=experience,
                user_id = userid,
                class_id_id = classid,
                subject_id = subjectid,
                email = email,
                bank_name = bank_name,
                branch_code = branch_code,
                account_number = account_number,
                education_level = education_level,
                status=status,
                image=image
                )
                professor.save()
                messages.success(request,'User Added Succfully')
        return redirect('all-professors')
    else:
         
        className = Class.objects.order_by('classname').distinct('classname')
        classSection = Class.objects.distinct('section')
        classShift = Class.objects.distinct('shift')
        subjects = Subject.objects.distinct('subject')
        user = User.objects.get(id=userid)
        # print(user.username)
        return render(request,'Professor/add-professor.html',{'className':className,'user':user,'classSection':classSection,'classShift':classShift,'subjects':subjects})

def  professor_profile(request,id):
    professor = Professor.objects.get(id=id) 
    profclass = Class.objects.get(id=professor.class_id_id)
    profsubject = Subject.objects.get(id=professor.subject_id)
    className = Class.objects.order_by('classname').distinct('classname')
    classSection = Class.objects.distinct('section')
    classShift = Class.objects.distinct('shift')
    subjects = Subject.objects.distinct('subject')
    professor= Professor.objects.get(id=id)
    return render(request,'Professor/professor-profile.html',{'prof':professor,'className':className,'classSection':classSection,'classShift':classShift,'subjectName':subjects,'profclass':profclass,'profsubject':profsubject})

def  edit_professor(request,id):
    professor = Professor.objects.get(id=id) 
    if request.method=='POST':
        if Professor.objects.filter(name=request.POST['name'],f_Name=request.POST['f_Name']).count()>1:
            messages.error(request,"Teacher Exist")
        elif Class.objects.filter(classname=request.POST['current_class'],section=request.POST['section']).exists() == False:
            messages.error(request,'Class Does not exist Please Add Class First!')
        
        elif Subject.objects.filter(classid_id=Class.objects.get(classname=request.POST['current_class'],section=request.POST['section']).id,subject=request.POST['subject']).exists() == False:
            messages.error(request,'Subject Does Not Exist in Following class Please Make Sure You Have Added All Subjects  into the Following Class!')
        
        else:
            myclass = Class.objects.get(classname=request.POST['current_class'],section=request.POST['section'])
            classid=myclass.id
            professor.class_id_id = classid
            subject=Subject.objects.get(classid_id=classid,subject=request.POST['subject'])
            professor.subject_id = subject.id
            professor.name = request.POST['name']
            professor.f_Name = request.POST['f_Name']
            professor.contact1 = request.POST['contact1']
            professor.contact2 = request.POST['contact2']
            professor.address = request.POST['address']
            if request.POST['dob'] != '':
                print("I'm Here"+request.POST['dob'])
                d = datetime.strptime(request.POST['dob'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                professor.dob = d
            if request.POST['joining_date'] != '':
                d2 = datetime.strptime(request.POST['joining_date'], '%m/%d/%Y')
                d2.strftime('%Y/%m/%d')
                professor.joining_date = d2
            professor.religion = request.POST['religion'] 
            professor.shift = request.POST['shift']
            professor.gender = request.POST['gender']
            professor.age = request.POST['age']
            professor.cnic = request.POST['cnic']
            professor.experience = request.POST['experience']
            professor.education_level = request.POST['education_level']
            professor.bank_name = request.POST['bank_name']
            professor.branch_code = request.POST['branch_code']
            professor.account_number = request.POST['account_number']
            professor.email = request.POST['email']
            professor.status = request.POST['status']
            if request.FILES.get('image') is not None:
                professor.image = request.FILES.get('image')
            professor.save()
            print(professor.name)
            messages.success(request,'Profile Updated!!')
        return redirect('all-professors')
    else:
        profclass = Class.objects.get(id=professor.class_id_id)
        profsubject = Subject.objects.get(id=professor.subject_id)
        className = Class.objects.order_by('classname').distinct('classname')
        classSection = Class.objects.distinct('section')
        classShift = Class.objects.distinct('shift')
        subjects =Subject.objects.distinct('subject')
        # print(user.username)
        return render(request,'Professor/edit-professor.html',{'prof':professor,'className':className,'classSection':classSection,'classShift':classShift,'subjectName':subjects,'profclass':profclass,'profsubject':profsubject})

def search_professor(request):
    if request.method=='POST':
        search = request.POST['search']
        print(search)
        result = Professor.objects.filter(Q(name__icontains=search) | Q(f_Name__icontains=search))
        no_result = ''
        if result.count()==0:
            no_result='No Result Found'
        return render(request,'Professor/all-professors.html',{'professor' : result,'no_result':no_result})
    else:
        professor = Professor.objects.all()
        return render(request,'Professor/all-professors.html',{'professor' : professor})

def delete_professor(request,id):
    professor = Professor.objects.get(id=id)
    professor.delete()
    messages.success(request,'Profile Deleted!!')
    return redirect('all-professors')

def professor_csv(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method=='POST':

        if request.FILES.get('csv_file') is not None: 
            csv_file = request.FILES.get('csv_file')
            if not csv_file.name.endswith('.csv'):
                messages.error(request,'It is Not a CSV File')
            else:
                data_set =csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for column in csv.reader(io_string,delimiter=',',quotechar="|"):
                    if Student.objects.filter(gr=column[0]).count()<1:
                        _, created =Student.objects.update_or_create(
                            
                                
                                name=column[0],
                                f_Name=column[1],
                                contact1 = column[2],
                                contact2 = column[3],
                                address = column[4],
                                dob = date.today(),
                                admit_date = date.today(),
                                religion = column[7],
                                admit_class = column[8],
                                current_class = column[10],
                                section = column[11],
                                shift = column[12],
                                last_school = column[13],
                                gender = column[14],
                                age = column[15],
                                cnic = column[16],
                                status = column[17],
                                user_id = userid
                        )
                        messages.success(request,'Students Added ')
                    
        else:
            messages.error(request,'No File Selected')
       
        return redirect('all-students')

    else:
        for row in Student.objects.all():
            
            if Student.objects.filter(gr=row.gr).count() > 1:
                row.delete()
        # student = Student.objects.get(status='')
        studs = Student.objects.all()
        return render(request,"Student/all-students.html",{'studs' : studs})






# Student
def  all_students(request):
    studs = Student.objects.all()
    # studs=[stud1,stud2]
    return render(request,"Student/all-students.html",{'studs' : studs})

def  add_student(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method == 'POST':
        # if Student.objects.filter(gr=request.POST['gr']).exists() == True:
        #     messages.error(request,'Student could not be Added Because GR is Already Exist!')
        # else:
        if User.objects.filter(id=userid).exists():
            name = request.POST['name']
            f_Name = request.POST['f_Name']
            contact1 = request.POST['contact1']
            contact2 = request.POST['contact2']
            address = request.POST['address']
            religion = request.POST['religion']
            
            if request.POST['dob'] != '':
                print("I'm Here"+request.POST['dob'])
                d = datetime.strptime(request.POST['dob'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                dob = d
            if request.POST['admit_date'] != '':
                d2 = datetime.strptime(request.POST['admit_date'], '%m/%d/%Y')
                d2.strftime('%Y/%m/%d')
                admit_date = d2
            admit_class = request.POST['admit_class']
            current_class = request.POST['current_class']
            section = request.POST['section']
            shift = request.POST['shift']
            last_school = request.POST['last_school']
            gender = request.POST['gender']
            age = 19
            gr = request.POST['gr']
            cnic = request.POST['cnic']
            status = request.POST['status']
            image = request.FILES.get('image',False)
            if Student.objects.filter(gr=gr).exists():
                messages.error(request,'Gr Exist')
                print('Gr Exist')
            elif Class.objects.filter(classname=current_class,section=section).exists() == False:
                messages.error(request,'Class Does not exist Please Add Class First!')

            else:
                myclass = Class.objects.get(classname=request.POST['current_class'],section=request.POST['section'])
                classid=myclass.id
                student = Student(
                                gr = gr,
                                name=name,
                                f_Name=f_Name,
                                contact1 = contact1,
                                contact2 = contact2,
                                address = address,
                                dob = dob,
                                admit_date = admit_date,
                                religion = religion,
                                admit_class = admit_class,
                                current_class = current_class,
                                section = section,
                                shift = shift,
                                last_school = last_school,
                                gender = gender,
                                age = age,
                                cnic = cnic,
                                status = status,
                                user_id = userid,
                                c_class_id = classid,
                                image=image
                                )

                student.save()
                messages.success(request,'Student Added!!')
                print('user added')
        return redirect('all-students')
    
    else:
         
        className = Class.objects.order_by('classname').distinct('classname')
        classSection = Class.objects.distinct('section')
        classShift = Class.objects.distinct('shift')
        subjects = Subject.objects.distinct('subject')
        
        user = User.objects.get(id=userid)
        # print(user.username)
        return render(request,'Student/add-student.html',{'className':className,'user':user,'classSection':classSection,'classShift':classShift,'subjects':subjects})
def  edit_student(request,id):
    
    stud=Student.objects.get(id=id)
    if request.method=='POST':
        if Student.objects.filter(gr=request.POST['gr']).count() > 1:
            messages.error(request,'Student could not be Updated Because GR is Already Exist!')
        
        elif Class.objects.filter(classname=request.POST['current_class'],section=request.POST['section']).exists() == False:
            messages.error(request,'Class Does not exist Please Add Class First!')
        
        else:
            myclass = Class.objects.get(classname=request.POST['current_class'],section=request.POST['section'])
            classid=myclass.id
            stud.c_class_id = classid
            stud.name = request.POST['name']
            stud.f_Name = request.POST['f_Name']
            stud.contact1 = request.POST['contact1']
            stud.contact2 = request.POST['contact2']
            stud.address = request.POST['address']
            if request.POST['dob'] != '':
                print("I'm Here"+request.POST['dob'])
                d = datetime.strptime(request.POST['dob'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                stud.dob = d
            if request.POST['admit_date'] != '':
                d2 = datetime.strptime(request.POST['admit_date'], '%m/%d/%Y')
                d2.strftime('%Y/%m/%d')
                stud.admit_date = d2
            
            stud.religion = request.POST['religion']
            stud.admit_class = request.POST['admit_class']
            stud.current_class = request.POST['current_class']
            stud.section = request.POST['section']
            stud.shift = request.POST['shift']
            stud.last_school = request.POST['last_school']
            stud.gender = request.POST['gender']
            stud.age = 19
            stud.gr = request.POST['gr']
            stud.cnic = request.POST['cnic']
            stud.status = request.POST['status']
            if request.FILES.get('image') is not None:
                stud.image = request.FILES.get('image')
            print(stud.image)
            stud.save()
            print(stud.name)
            messages.success(request,'Student Profile Updated!!')
        return redirect('all-students')
        
    else:
        
         
        className = Class.objects.order_by('classname').distinct('classname')
        classSection = Class.objects.distinct('section')
        classShift = Class.objects.distinct('shift')
        
        return render(request,'Student/edit-student.html',{'stud':stud,'className':className,'classSection':classSection,'classShift':classShift})

def student_csv(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method=='POST':

        if request.FILES.get('csv_file') is not None: 
            csv_file = request.FILES.get('csv_file')
            if not csv_file.name.endswith('.csv'):
                messages.error(request,'It is Not a CSV File')
            else:
                data_set =csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for column in csv.reader(io_string,delimiter=',',quotechar="|"):
                    if Student.objects.filter(gr=column[0]).count()<1:
                        _, created =Student.objects.update_or_create(
                            
                                gr = column[0],
                                name=column[1],
                                f_Name=column[2],
                                contact1 = column[3],
                                contact2 = column[4],
                                address = column[5],
                                dob = date.today(),
                                admit_date = date.today(),
                                religion = column[8],
                                admit_class = column[9],
                                current_class = column[10],
                                section = column[11],
                                shift = column[12],
                                last_school = column[13],
                                gender = column[14],
                                age = column[15],
                                cnic = column[16],
                                status = column[17],
                                user_id = userid
                        )
                        messages.success(request,'Students Added ')
                    
        else:
            messages.error(request,'No File Selected')
       
        return redirect('all-students')

    else:
        for row in Student.objects.all():
            
            if Student.objects.filter(gr=row.gr).count() > 1:
                row.delete()
        # student = Student.objects.get(status='')
        studs = Student.objects.all()
        return render(request,"Student/all-students.html",{'studs' : studs})

def student_pdf(request,id):
    template =get_template('Student/pdf-student.html')
    student =Student.objects.get(id=id)
    prof = {
        "gr" : student.gr,
        "name": student.name,
        "f_Name": student.f_Name,
        "contact1" : student.contact1,
        "contact2" : student.contact2,
        "address" : student.address,
        "dob" : student.dob,
        "admit_date" : student.admit_date,
        "religion" : student.religion,
        "admit_class" : student.admit_class,
        "current_class" : student.current_class,
        "section" : student.section,
        "shift" : student.shift,
        "last_school" : student.last_school,
        "gender" : student.gender,
        "age" : student.age,
        "cnic" : student.cnic,
        "status" : student.status,
        "image" : student.image
        }
    html = template.render(prof)
    pdf = render_to_pdf('Student/pdf-student.html',prof)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "myname_%s.pdf"
        content = "inline; filename='%s'" %(filename)
        response['Content-Disposition'] = content
        return response
    else:
        return render(request,'Student/student-profile.html',{'prof':prof})
    

def delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.success(request,'Student Profile  Deleted!!')
    return redirect('all-student')

# Other

def all_others(request):
    others = Others.objects.all()
    return render(request,'Others/all-others.html',{'others' : others})

def  add_other(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method == 'POST':
        if User.objects.filter(id=userid).exists():
            name = request.POST['name']
            f_Name = request.POST['f_Name']
            contact1 = request.POST['contact1']
            contact2 = request.POST['contact2']
            address = request.POST['address']
            if request.POST['dob'] != '':
                print("I'm Here"+request.POST['dob'])
                d = datetime.strptime(request.POST['dob'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                dob = d
            if request.POST['joining_date'] != '':
                d2 = datetime.strptime(request.POST['joining_date'], '%m/%d/%Y')
                d2.strftime('%Y/%m/%d')
                joining_date = d2
            religion = request.POST['religion'] 
            shift = request.POST['shift']
            gender = request.POST['gender']
            age = request.POST['age']
            cnic = request.POST['cnic']
            experience = request.POST['experience']
            education_level = request.POST['education_level']
            bank_name = request.POST['bank_name']
            branch_code = request.POST['branch_code']
            account_number = request.POST['account_number']
            email = request.POST['email']
            status = request.POST['status']
            image = request.FILES.get('image',False)
            job_title = request.POST['job_title']
            if Others.objects.filter(name=name,f_Name=f_Name).exists():
                print("User Exist")
                messages.error(request,'User Exist')
            else:
                other = Others(  
                name=name,
                f_Name=f_Name,
                contact1 = contact1,
                contact2 = contact2,
                address = address,
                dob = dob,
                joining_date = joining_date,
                religion = religion,
                shift = shift,
                gender = gender,
                age = age,
                cnic = cnic,
                experience=experience,
                user_id = userid,
                email = email,
                bank_name = bank_name,
                branch_code = branch_code,
                account_number = account_number,
                education_level = education_level,
                status= status,
                job_title = job_title,
                image=image
                )
                other.save()
                messages.success(request,'User Added Succfully')
        return redirect('all-others')
    else:
        user = User.objects.get(id=userid)
        return render(request,'Others/add-other.html',{'user':user})


def  edit_other(request,id):
    professor = Others.objects.get(id=id) 
    if request.method=='POST':
        if Others.objects.filter(name=request.POST['name'],f_Name=request.POST['f_Name']).count()>1:
            messages.error(request,"User Exist")  
        else:
            professor.name = request.POST['name']
            professor.f_Name = request.POST['f_Name']
            professor.contact1 = request.POST['contact1']
            professor.contact2 = request.POST['contact2']
            professor.address = request.POST['address']
            if request.POST['dob'] != '':
                print("I'm Here"+request.POST['dob'])
                d = datetime.strptime(request.POST['dob'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                professor.dob = d
            if request.POST['joining_date'] != '':
                d2 = datetime.strptime(request.POST['joining_date'], '%m/%d/%Y')
                d2.strftime('%Y/%m/%d')
                professor.joining_date = d2
            professor.religion = request.POST['religion'] 
            professor.shift = request.POST['shift']
            professor.job_title = request.POST['job_title']
            professor.gender = request.POST['gender']
            professor.age = request.POST['age']
            professor.cnic = request.POST['cnic']
            professor.experience = request.POST['experience']
            professor.education_level = request.POST['education_level']
            professor.bank_name = request.POST['bank_name']
            professor.branch_code = request.POST['branch_code']
            professor.account_number = request.POST['account_number']
            professor.email = request.POST['email']
            professor.status = request.POST['status']
            if request.FILES.get('image') is not None:
                professor.image = request.FILES.get('image')
            professor.save()
            print(professor.name)
            messages.success(request,'Profile Updated!!')
        return redirect('all-others')
    else:
        # print(user.username)
        return render(request,'Others/edit-other.html',{'prof':professor})

def  other_profile(request,id):
    other=Others.objects.get(id=id)
    return render(request,'Others/other-profile.html',{'prof':other})

def search_other(request):
    if request.method=='POST':
        search = request.POST['search']
        print(search)
        result = Others.objects.filter(Q(name__icontains=search) | Q(f_Name__icontains=search))
        no_result = ''
        if result.count()==0:
            no_result='No Result Found'
        return render(request,'Others/all-others.html',{'professor' : result,'no_result':no_result})
    else:
        other = Others.objects.all()
        return render(request,'Others/all-others.html',{'professor' : other})

def delete_other(request,id):
    other = Others.objects.get(id=id)
    other.delete()
    messages.success(request,'Profile Deleted!!')
    return redirect('all-others')

def other_csv(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method=='POST':

        if request.FILES.get('csv_file') is not None: 
            csv_file = request.FILES.get('csv_file')
            if not csv_file.name.endswith('.csv'):
                messages.error(request,'It is Not a CSV File')
            else:
                data_set =csv_file.read().decode('UTF-8')
                io_string = io.StringIO(data_set)
                next(io_string)
                for column in csv.reader(io_string,delimiter=',',quotechar="|"):
                    if Student.objects.filter(gr=column[0]).count()<1:
                        _, created =Student.objects.update_or_create(
                            
                                
                                name=column[0],
                                f_Name=column[1],
                                contact1 = column[2],
                                contact2 = column[3],
                                address = column[4],
                                dob = date.today(),
                                admit_date = date.today(),
                                religion = column[7],
                                admit_class = column[8],
                                
                                section = column[11],
                                shift = column[12],
                                last_school = column[13],
                                gender = column[14],
                                age = column[15],
                                cnic = column[16],
                                status = column[17],
                                user_id = userid
                        )
                        messages.success(request,'Students Added ')
                    
        else:
            messages.error(request,'No File Selected')
       
        return redirect('all-students')

    else:
        for row in Student.objects.all():
            
            if Student.objects.filter(gr=row.gr).count() > 1:
                row.delete()
        # student = Student.objects.get(status='')
        studs = Student.objects.all()
        return render(request,"Student/all-students.html",{'studs' : studs})



# Course

def  all_courses(request):
    className = Class.objects.all()
    students = []
    count = 0
    for myclass in className:
        if Student.objects.filter(c_class_id=myclass.id).exists():
            students.append(Student.objects.filter(c_class_id=myclass.id).count())
    className2 = Class.objects.order_by('classname').distinct('classname')
    classSection = Class.objects.distinct('section')
    classShift = Class.objects.distinct('shift')
    professor = Professor.objects.all()
    return render(request,'Class/all-courses.html',{'classes':className,'className2':className2,'classSection':classSection,'classShift':classShift,'professor':professor})
    
def  add_course(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method == 'POST':
        classname= request.POST['classname']
        section= request.POST['section']
        shift= request.POST['shift']
        
        if User.objects.filter(id=userid).exists():
            if Class.objects.filter(classname=classname).exists() == True :
                print('matched')
                messages.error(request,'Class Already exist')
            else:
                if section=='1':
                    myclass=Class(
                        classname=classname,
                        section='A',
                        shift=shift,
                        user_id=userid
                    )
                    messages.success(request,'Class Added')
                    myclass.save()

                elif section=='2':
                    myclass=Class(
                        classname=classname,
                        section='A',
                        shift=shift,
                        user_id=userid
                    )
                    myclass.save()
                    myclass=Class(
                        classname=classname,
                        section='B',
                        shift=shift,
                        user_id=userid
                    )
                    messages.success(request,'Class Added')
                    myclass.save()
                elif section=='3':
                    myclass=Class(
                        classname=classname,
                        section='A',
                        shift=shift,
                        user_id=userid
                    )
                    myclass.save()
                    myclass=Class(
                        classname=classname,
                        section='B',
                        shift=shift,
                        user_id=userid
                    )
                    myclass.save()
                    myclass=Class(
                        classname=classname,
                        section='C',
                        shift=shift,
                        user_id=userid
                    )
                    messages.success(request,'Class Added')
                    myclass.save()
                elif section=='4':
                    myclass=Class(
                        classname=classname,
                        section='A',
                        shift=shift,
                        user_id=userid
                    )
                    myclass.save()
                    myclass=Class(
                        classname=classname,
                        section='B',
                        shift=shift,
                        user_id=userid
                    )
                    myclass.save()
                    myclass=Class(
                        classname=classname,
                        section='C',
                        shift=shift,
                        user_id=userid
                    )
                    myclass.save()
                    myclass=Class(
                        classname=classname,
                        section='D',
                        shift=shift,
                        user_id=userid
                    )
                    messages.success(request,'Class Added')
                    myclass.save()
                else:
                    print('Bas krddo')
            # print(classname,section,shift)
        return redirect('all-courses')
    else:
        user = User.objects.get(id=userid)

        return render(request,'Class/add-course.html',{'user':user})

def  edit_course(request):
    return render(request,'Class/edit-course.html')

def delete_course(request,id):
    course = Class.objects.get(id=id)
    course.delete()
    messages.success(request,'Class Deleted!!')
    return redirect('all-courses')

def search_courses(request):
    if request.method=='POST':
        classname = request.POST.get('classname',None)
        section = request.POST.get('section',None)
        shift = request.POST.get('shift',None)
        profname = request.POST.get('profname',None)

        check = 0
        if classname is not None and section is not None and shift is not None and profname is not None:
            if Class.objects.filter(classname=classname,section=section,shift=shift).exists():
                searchclass = Class.objects.filter(classname=classname,section=section,shift=shift)
                if Professor.objects.filter(class_id_id=searchclass.id).exists()==False:
                    no_result='No result'
                else:
                    check = 1
            else:
                no_result='No result'

        elif classname is not None and section is not None and shift is not None:
            if Class.objects.filter(classname=classname,section=section,shift=shift).exists():
                searchclass = Class.objects.filter(classname=classname,section=section,shift=shift)
                check = 1
            else:
                no_result='No result'
        elif classname is not None and section is not None:
            if Class.objects.filter(classname=classname,section=section).exists():
                searchclass = Class.objects.filter(classname=classname,section=section)
                check = 1
            else:
                no_result='No result'
        elif classname is not None and shift is not None:
            if Class.objects.filter(classname=classname,shift=shift).exists():
                searchclass = Class.objects.filter(classname=classname,shift=shift)
                check = 1
            else:
                no_result='No result'
        elif classname is not None and profname is not None:
            if Class.objects.filter(classname=classname).exists():
                searchclass = Class.objects.filter(classname=classname)
                if Professor.objects.filter(class_id_id=searchclass.id).exists()==False:
                    no_result='No result'
                else:
                    check = 1
            else:
                no_result='No result'
        elif section is not None and shift is not None:
            if Class.objects.filter(section=section,shift=shift).exists():
                searchclass = Class.objects.filter(section=section,shift=shift)
                check = 1
            else:
                no_result='No result'
        elif section is not None :
            if Class.objects.filter(section=section).exists():
                searchclass = Class.objects.filter(section=section)
                check = 1
            else:
                no_result='No result'
       
        elif shift is not None:
            if Class.objects.filter(shift=shift).exists():
                searchclass = Class.objects.filter(shift=shift)
                check = 1
            else:
                no_result='No result'
        elif classname is not None:
            if Class.objects.filter(classname=classname).exists():
                searchclass = Class.objects.filter(classname=classname)
                check = 1
            else:
                no_result='No result'
        elif profname is not None:
            classi = Professor.objects.distinct('name')
            for sclass in classi:
                if sclass.name==profname:
                    classid = sclass.class_id_id
            if Class.objects.filter(id=classid).exists():
                searchclass = Class.objects.filter(id=classid)
                check = 1
            else:
                no_result='No result'
        else:
            no_result='No result'
        
        if check == 1:
            students = []
            count = 0
            # if Student.objects.filter(c_class_id=searchclass.id).exists():
            #     students.append(Student.objects.filter(c_class_id=searchclass.id).count())
            className2 = Class.objects.order_by('classname').distinct('classname')
            classSection = Class.objects.distinct('section')
            classShift = Class.objects.distinct('shift')
            professor = Professor.objects.all()
            return render(request,'Class/all-courses.html',{'classes':searchclass,'className2':className2,'classSection':classSection,'classShift':classShift,'professor':professor})

        else:
            className2 = Class.objects.order_by('classname').distinct('classname')
            classSection = Class.objects.distinct('section')
            classShift = Class.objects.distinct('shift')
            professor = Professor.objects.all()
            return render(request,'Class/all-courses.html',{'no_result':no_result,'className2':className2,'classSection':classSection,'classShift':classShift,'professor':professor})
    else:
        return redirect(request,'all-courses')

# Subject 

def  all_subjects(request):
    return render(request,'Subject/all-subjects.html')

def  add_subject(request,name):
    mainuser = User.objects.get(username=name)
    userid = mainuser.id
    if request.method=='POST':
        subject=request.POST['subject']
        shift=request.POST['shift']
        classname = request.POST['classname']
        section=request.POST['section']
        myclass=Class.objects.get(classname=classname,section=section,shift=shift)
        classid=myclass.id
        if Class.objects.filter(classname=classname,section=section):
            if User.objects.filter(id=userid).exists():
                subject=Subject(
                    user_id=userid,
                    subject=subject,
                    classid_id =classid,
                    )
                subject.save()
            return redirect('all-subjects')
    else:    
        
        className = Class.objects.order_by('classname').distinct('classname')
        classSection = Class.objects.distinct('section')
        classShift = Class.objects.distinct('shift')
        
        user = User.objects.get(id=userid)
        # print(user.username)
        return render(request,'Subject/add-subject.html',{'className':className,'user':user,'classSection':classSection,'classShift':classShift})


# Salary

def add_salary(request,name):
    if User.objects.filter(username=name).exists():
        user = User.objects.get(username=name)
        uid = user.id
        if request.method == 'POST':
            staff_name = request.POST['staff_name']
            salary = request.POST['salary']
            if request.POST['payment_date'] != '':
                d = datetime.strptime(request.POST['payment_date'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                payment_date = d
                
            month = request.POST['mon']
            staff = request.POST['staff']
            if staff=='1':
                if Professor.objects.filter(name=staff_name).exists():
                    professor = Professor.objects.get(name=staff_name)
                    salary = Salary(user_id=user.id,professor_id=professor.id,name=staff_name,salary=salary,payment_date=payment_date,month=month,person=staff)
                    salary.save()
                    messages.success(request,'Salary Added Succfully')
                else:
                    messages.error(request,'Selected Satff is Not A teacher.Please select correct combination')
            elif staff=='2':
                if Others.objects.filter(name=staff_name).exists():
                    other = Others.objects.get(name=staff_name)
                    salary = Salary(user_id=user.id,other_id=other.id,name=staff_name,salary=salary,payment_date=payment_date,month=month,person=staff)
                    salary.save()
                    messages.success(request,'Salary Added Succfully')
                else:
                    messages.error(request,'Selected Satff is A teacher.Please select correct combination')
            else:
                messages.error(request,'Select a Profession')
            return redirect('all-salary')
        professor = Professor.objects.get(user_id=uid)
        others = Others.objects.get(user_id=uid)
        return render(request,'Salary/add-salary.html',{'professor':professor,'others':others})
    else:
        
        return render(request,'Salary/add-salary.html')


def all_salary(request):
    salary = Salary.objects.all()
    professor = Professor.objects.all()
    others = Others.objects.all()
    count = 0
    return render(request,'Salary/all-salary.html',{'salary':salary,'count':count,'professor':professor,'others':others})


# Expenses
def all_expenses(request):
    
    user = request.user
    expenses = Expenses.objects.all()
    return render(request,'Expenses/all-expenses.html',{'expenses':expenses})

def add_expense(request,name):
    if User.objects.filter(username=name).exists():
        user=User.objects.get(username=name)
        if request.method =='POST':
            exp_amount = request.POST['exp_amount']
            if request.POST['exp_date'] != '':
                d = datetime.strptime(request.POST['exp_date'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                exp_date = d
            exp_description = request.POST['exp_description']
            exp_mon = request.POST['exp_mon']
            expense = Expenses(
                user_id = user.id,
                exp_amount=exp_amount,
                exp_date = exp_date,
                exp_description = exp_description,
                exp_mon = exp_mon
            )
            expense.save()
            messages.success(request,'Expense Added Succfully')
            return redirect('all-expenses')
        else:
            return redirect('all-expenses')
    else:    
        return redirect('login')

def edit_expense(request,id):
    return render(request,'Expenses/edit-expense.html')

def table_expense(request,id):
    expense = Expenses.objects.filter(user_id=id)
    return render(request,'Expenses/table-expense.html',{'expenses':expense})

def search_expense(request,id):
    
    if request.method =='POST':
        exp_amount = request.POST['exp_amount']
        exp_date = ''
        exp_mon = ''
        condition = ''
        no_result = ''
        if request.POST['exp_date'] != '':
                d = datetime.strptime(request.POST['exp_date'],'%m/%d/%Y')
                d.strftime('%Y/%m/%d')
                exp_date = d
        if request.POST['exp_mon'] != '':
            exp_mon = request.POST['exp_mon']
        exp_description = request.POST['exp_description']
        if request.POST['condition'] != '':
            condition = request.POST['condition']
        
        if exp_amount is not None and exp_date is not None and exp_description is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_description__icontains=exp_description) | Q(exp_date__icontains=exp_date) | Q(exp_mon__icontains=exp_mon))
        
        elif exp_date is not None and exp_description is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_description__icontains=exp_description) | Q(exp_date__icontains=exp_date) | Q(exp_mon__icontains=exp_mon))
        
        elif exp_amount is not None and exp_description is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_description__icontains=exp_description) | Q(exp_mon__icontains=exp_mon))
        
        elif exp_amount is not None and exp_date is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_date__icontains=exp_date) | Q(exp_mon__icontains=exp_mon))
        
        elif exp_amount is not None and exp_date is not None and exp_description is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_description__icontains=exp_description) | Q(exp_date__icontains=exp_date))
        
        elif exp_date is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_date__icontains=exp_date) | Q(exp_mon__icontains=exp_mon))
        
        elif exp_date is not None and exp_description is not None:
            result = Expenses.objects.filter(Q(exp_description__icontains=exp_description) | Q(exp_date__icontains=exp_date))
        
        elif exp_amount is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_mon__icontains=exp_mon))

        elif exp_amount is not None and exp_description is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_description__icontains=exp_description))
        
        elif exp_description is not None and exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_description__icontains=exp_description) | Q(exp_mon__icontains=exp_mon))

        elif exp_amount is not None and exp_date is not None:
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount) | Q(exp_date__icontains=exp_date))
            
        elif exp_amount is not None :
            result = Expenses.objects.filter(Q(exp_amount__icontains=exp_amount))
        
        elif exp_date is not None:
            result = Expenses.objects.filter(Q(exp_date__icontains=exp_date))
        
        elif exp_description is not None:
            result = Expenses.objects.filter(Q(exp_description__icontains=exp_description))
        
        elif exp_mon is not None:
            result = Expenses.objects.filter(Q(exp_mon__icontains=exp_mon))
        
        else:
            no_result='No result'

        if result.count()==0:
            no_result='No result'

        return render(request,'Expenses/all-expenses.html',{'expenses':result,'no_result':no_result})
    else:
        return redirect('all-expenses')



def page_404(request):
    return render(request,'404.html'),

def  page_505(request):
    return render(request,'505.html'),

def  add_department(request):
    return render(request,'add-department.html')

def  add_library_assets(request):
    professor = Professor.objects.all()
    return render(request,'add-library-assets.html',{'professor':professor})



def  advance_form_element(request):
    return render(request,'advance-form-element.html')




def  alerts(request):
    return render(request,'alerts.html')







def  analytics(request):
    return render(request,'analytics.html')

def  area_charts(request):
    return render(request,'area-charts.html')

def  bar_charts(request):
    return render(request,'bar-charts.html')


def  basic_form_element(request):
    return render(request,'basic-form-element.html')

def  buttons(request):
    return render(request,'buttons.html')

def  c3(request):
    return render(request,'c3.html')

def  accordion(request):
    return render(request,'accordion.html')

def  code_editor(request):
    return render(request,' code-editor.html')

def  course_info(request):
    return render(request,'course-info.html')
 
def  course_profile(request):
    return render(request,'course-profile.html')

def  data_maps(request):
    return render(request,'data-maps.html')

def  data_table(request):
    if request.method=='POST':
       
        return redirect('data_table.html')
    else:
        studs = Student.objects.all()
        return render(request,'data-table.html',{'studs' : studs})

def  departments(request):
    return render(request,'departments.html')

def  dual_list_box(request):
    return render(request,'dual-list-box.html')



def  edit_department(request):
    return render(request,'edit-department.html')

def  edit_library_assets(request):
    return render(request,' edit-library-assets.html')


def  events(request):
    return render(request,'events.html')

def  google_map(request):
    return render(request,'google-map.html')

def  images_cropper(request):
    return render(request,'images-cropper.html')

def  library_assets(request):
    professor = Professor.objects.all()
    return render(request,'library-assets.html',{'professor':professor})

def  line_charts(request):
    return render(request,'line-charts.html')

def  lock(request):
    return render(request,'lock.html')

# def  login(request):
#     return render(request,'login.html')

def  mailbox_compose(request):
    return render(request,'mailbox-compose.html')

def  mailbox_view(request):
    return render(request,'mailbox-view.html')

def  mailbox(request):
    return render(request,'mailbox.html')

def  modals(request):
    return render(request,'modals.html')

def  multi_upload(request):
    return render(request,'multi-upload.html')

def  notifications(request):
    return render(request,'notifications.html')

def  password_meter(request):
    return render(request,'password-meter.html')

def  password_recovery(request):
    return render(request,'password-recovery.html')

def  pdf_viewer(request):
    return render(request,'pdf-viewer.html')

def  peity(request):
    return render(request,'peity.html')

def  preloader(request):
    return render(request,'preloader.html')


    # else:
        # return redirect('all-professors')


def  login(request):
    return render(request,'Registration/login.html')

def  rounded_chart(request):
    return render(request,'rounded-chart.html')

def  sparkline(request):
    return render(request,'sparkline.html')

def  static_table(request):
    professor = Professor.objects.all()
    return render(request,'mytable.html',{'professor':professor})

def  student_profile(request,id):
    stud = Student.objects.get(id=id)
    return render(request,'Student/student-profile.html',{'prof':stud,'stud':stud})

def  tabs(request):
    return render(request,'tabs.html')

def  tinymc(request):
    return render(request,'tinymc.html')

def  tree_view(request):
    return render(request,'tree-view.html')

def  x_editable(request):
    return render(request,'x-editable.html')

def  course_payment(request):
    return render(request,'course-payment.html')
    
def  widgets(request):
    return render(request,'widgets.html')


# Salary
# def professor_salary(request):
    