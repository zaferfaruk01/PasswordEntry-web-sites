from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages


# Create your views here.


def login(request):
    if request.method == 'POST':
        #user login
        username = request.POST['username']
        password = request.POST['password']

        #verilen bilgilerle ilgili kayıt var mı?
        user = auth.authenticate(username = username , password = password)
        #session id oluşturuyor
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Oturum Açıldı')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Kullanıcı adı veya parola yanlış')
            return redirect('login')
    else:
        return render (request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        
        #user kayıt
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'Bu kullanıcı adı daha önce alınmış.')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'Bu mail daha önce alınmış.')
                    return redirect('register')
                else:
                    #hiçbir sorun yok
                    #user kayıt işlemi
                    user = User.objects.create_superuser(username = username, password = password, email = email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Hesabınız oluşturuldu!')
                    
                    return redirect('login')
        else:
            messages.add_message(request, messages.ERROR, 'Parolalar eşleşmiyor.')
            return redirect('register')
        
        return redirect('register')
    else:
        return render (request, 'user/register.html')

    return render (request, 'user/register.html')

def logout(request):

    if request.method =='POST':
        auth.logout(request)
        #session id yisiler
        messages.add_message(request,messages.SUCCESS,'Oturumunuz kapatıldı.')
        return redirect('index')
    return render (request, 'user/logout.html')
