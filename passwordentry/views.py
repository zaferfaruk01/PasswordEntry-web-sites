from django.shortcuts import render,redirect
from django.http import HttpResponse

from django.contrib import messages

import keyboard

def index(request):
    
    
    def key_press(key):
        print(key.name," ",key.event_type," ",key.time)

    keyboard.hook(key_press)
    
    
    if request.method == 'POST':
        #verilen sifreyi ve kullanıcın sifresini alma,
        #altının çizgili olmasının sebebi kullanılmıyor olması
        
        verilensifre = request.POST['verilensifre']
        girilensifre = request.POST['girilensifre']
        
        #verilen bilgilerle ilgili kayıt var mı? kontrol yeri olucak!!
        dogru_mu=1

        if verilensifre==girilensifre :
            dogru_mu=1
        else:
            dogru_mu=0
        
        
        if dogru_mu==1 :
            messages.add_message(request, messages.SUCCESS, 'Şifre Girişi Başarılı')
            return render(request,'passwordentry/index.html')
        else:
            messages.add_message(request, messages.ERROR, 'Şifre Girişi Başarısız!')
            return render(request,'passwordentry/index.html')
    
    else:
        print("pass")
      
    return render (request, 'passwordentry/index.html')
    
def islem(request):
    
    pass

    