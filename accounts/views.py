from django.shortcuts import render , redirect
from django.contrib.auth.models import User , auth
from django.contrib import messages
from .models import School_Detail
from calc.models import Student,Professor,Class
# from .models import image_user
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
# Email Verification
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .token_generator import account_activation_token
from django.http import HttpResponse
from django.contrib.auth import login, authenticate

def register(request):
    if request.method =='POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']
        # image =  request.FILES['image']
        school_name = request.POST['school_name']
        school_code = request.POST['school_code']
        
        if password==re_password:
            if User.objects.filter(username=username).exists():
                print('user already exist')
                messages.error(request,'User Name is Already Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                print('email already exist')
                messages.error(request,'Email Address Already Exist')
                return redirect('register')
            else:
                
                user = User.objects.create_user(username=username , password=password , email=email , first_name=first_name ,last_name=last_name)
                
                user.is_active = False
                user.save()

                school = School_Detail(
                    user_id = user.pk,
                    school_name =school_name,
                    school_code =school_code,
                    school_category = request.POST['school_category']
                )
                # image_u=image_user(user_id=user.id,image=image)
                # image_u.save()
                school.save()
                #email Verification

                current_site = get_current_site(request)
                email_subject = 'Activate Your Account'
                message = render_to_string('Registration/activate_account.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': user.pk,
                    'token': account_activation_token.make_token(user),
                })
                to_email = email
                emailmess = EmailMessage(email_subject, message, to=[to_email])
                emailmess.send()
                messages.warning(request,'We have sent you an email, please confirm your email address to complete registration')


                
                print('image save')
                return redirect('login')
        else:
            print('Password did not match')
            return redirect('register')     
    else:
        return render(request,'Registration/register.html')



def activate_account(request, uid, token):
    try:
        # uid = force_bytes(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        
        return HttpResponse('Your account has been activate successfully')
    else:
        return HttpResponse('Activation link is invalid!')



def login(request):
    if request.method =='POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username,password)
        mainuser = auth.authenticate(username=username,password=password)
        if mainuser is not None:
            auth.login(request,mainuser)
            uname = str(mainuser.username)
            return redirect('home/'+uname)
        
        if User.objects.filter(username=username).exists() == False:
            messages.error(request,'Username Does Not Exist!!')
            return redirect('login')

        user = User.objects.get(username=username)
        if user.is_active == False:
            messages.warning(request,'Please Verify Your Email')
            return redirect('login')

        if user.password != password:
            messages.error(request,'Incorrect Password')
            return redirect('login')
        

    else:
        # auth.logout(request)
        return render(request,'Registration/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login') 

# def update_user(request,id):
    # if request.method=='POST':
    #     return redirect('home/'+str(id)+'/')
    # else:
    #     return redirect('home/'+str(id)+'/')
        