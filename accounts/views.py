from django.shortcuts import render

# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.models import Permission
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,
                                password=raw_password)
            login(request, user)
            user.is_staff=True
            permission = Permission.objects.get(name='Can change post')
            user.user_permissions.add(permission)
            user.save()
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
