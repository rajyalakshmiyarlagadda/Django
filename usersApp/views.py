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
            ur_form.save()
            print(ui_form.cleaned_data)
            user_obj = User.objects.get(username=ur_form.cleaned_data.get('username'))
            user_id = user_obj.id
            print(user_id)
            UserImage(user_id=user_id, image=ui_form.cleaned_data.get('image')).save()
            #ui_form.save()
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

# class LogoutView(View):
#     print('request is *******************************')
#     print('please print')
#     template_name='usersApp/logout.html'
    
#     def get(self, request):
#         print(request.session.is_empty())
#         if request.session:
#             messages.error(request, 'Session Expired Please Login Again')
#         logout(request)
#         return redirect(reverse('login'))

class LogoutView(RedirectView):
    
    template_name='usersApp/logout.html'

    def get(self, request, **kwargs):

        # If session expired django clean request.session object.
        # If user came to this view by clicking to logout button request.session not comes empty 
        print('My logout session is:', request.session, request.session.is_empty() )

        if request.session.is_empty():
            messages.error(request, "Your session has expired. Please login again to continue checking out.")

        logout(request)

        if request.GET.get('next'):
            self.url = '{}?next={}'.format(self.url, request.GET.get('next'))

        return super(LogoutView, self).get(request, **kwargs)





