from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *
from django.core.files.storage import FileSystemStorage


# Create your views here.


def signup(request):

    if request.method == 'POST':

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user_status = request.POST['user_status']

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request,'username is already taken!!!')
                return redirect('signup')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'email is already used!!!')
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()

                if user_status == 'client':
                    address = request.POST['address']
                    image = request.File['image']

                    client_obj = Client(
                        user = user,
                        address = address,
                        profile_image = image
                    )
                    client_obj.save()
                    print('client is created...')

                elif user_status == 'astrologer':
                    address = request.POST['address']
                    image = request.File['image']
                    certificate = request.File['certificate']

                    astrologer_obj = Astrologer(
                        user = user,
                        address = address,
                        profile_image = image,
                        certificate = certificate
                    )
                    astrologer_obj.save()
                    print('Astrologer is created...')
                


                print('user is created...')

               
                user_auth = auth.authenticate(username=username, password=password1)

                if user_auth is not None:
                    auth.login(request, user_auth)
                    return redirect('/')
        else:
            messages.info(request,'passwords are not matched!!!')
            return redirect('signup')
    else:
        return render(request, 'signup.html')




def login(request):

    if request.method== 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials!!!')
            return redirect('login')

    else:
        return render(request,'login.html')  
    

def logout(request):
    auth.logout(request)
    return redirect('/')  

