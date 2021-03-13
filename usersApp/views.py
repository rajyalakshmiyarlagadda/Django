from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm

# Create your views here.
def signUp(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request, "Your account has been created! Your arw now able to login.")
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'usersApp/signup.html', {'form': form})