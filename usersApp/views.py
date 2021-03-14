from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm
from django.contrib.auth import logout
from django.views.generic import View, RedirectView
from django.urls import reverse, reverse_lazy
#FormView, RedirectView

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usersApp/signup.html', {'form': form})

# class LogoutView(View):
    
#     def get(self, request):
#         if request.session:
#             messages.success(request, 'Successfully Logged Out')
#         else:
#             messages.error(request, 'Session Expired Please Login Again')
#         logout(request)
#         return redirect(reverse('login'))





