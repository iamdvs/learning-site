from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import logout,authenticate,login
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):

    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f' اکانت شما با موفقیت ثبت شد با نام {username}!')
            return redirect("/")

    else:        
        form=UserRegisterForm
    return render(request,'users/register.html',{'form':form})


            



