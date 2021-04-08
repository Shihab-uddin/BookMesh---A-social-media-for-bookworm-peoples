from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import createUserForm, userUpdateForm, profileUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.


def register_view(request):
    if request.method == 'POST':
        form = createUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Welcome to BookMesh !')
            return redirect('login')
    else:
        form = createUserForm()

    
    return render(request, 'users/Registration.html', {'form':form})

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

def profilesettings_view(request):
    if request.method == 'POST':
        u_form = userUpdateForm()
        p_form = profileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Updated!')
            return redirect('profile')
    else:
        u_form = userUpdateForm()
        p_form = profileUpdateForm(instance=request.user.profile)

    context = {
        'u_form' : u_form,
        'p_form' : p_form
    }
    return render(request, 'users/Profile_settings.html', context)


def logout_view(request):
    logout(request)
    return redirect('login')