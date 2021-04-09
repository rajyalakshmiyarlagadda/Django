from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserImage
from django.contrib.auth.models import User
from .forms import UserRegisterForm, UserImageForm
from django.contrib.auth import logout
from django.views.generic import View, RedirectView
from django.urls import reverse, reverse_lazy
#FormView, RedirectView

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        ur_form = UserRegisterForm(request.POST)
        ui_form = UserImageForm(request.POST, request.FILES)
        print(ui_form)
        if ur_form.is_valid() and ui_form.is_valid():
            user_obj = ur_form.save()
            UserImage(user_id=user_obj.id, image=ui_form.cleaned_data.get('image')).save()
            username = ur_form.cleaned_data.get('username')
            messages.success(
                request, "Your account has been created! Your ar now able to login.")
            return redirect('login')
    else:
        ur_form = UserRegisterForm()
        ui_form = UserImageForm()
    
    context = {
        'ur_form': ur_form,
        'ui_form': ui_form
    }
    return render(request, 'usersApp/signup.html', context)












