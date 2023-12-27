from django.shortcuts import render, redirect

from .models import CustomUser


def registration(request):
    if request.method == 'POST':
        try:
            user = CustomUser()
            user.email = request.POST['email']
            user.full_name = request.POST['full_name']
            user.set_password(request.POST['password'])
            user.save()
            return redirect('login')
        except Exception as e:
            return render(request, 'registration/registration.html')
    else:
        return render(request, 'registration/registration.html')

# def registration(request):
#     form = RegistrationForm(request.POST)
#     if request.method == 'POST':
#         if form.is_valid():
#             form.save()
#             return redirect('login')
#         else:
#             return messages.error(request, 'Invalid form')
#     else:
#         return render(request, 'registration/registration.html', {'form': form})

def login(request):
    if request.method == 'POST':
        try:
            user = CustomUser.objects.get(email=request.POST['email'])
            if user.check_password(request.POST['password']):
                request.session['user_id'] = user.id
                return redirect('home')
            else:
                return render(request, 'registration/sign_in.html', )
        except Exception as e:
            return render(request, 'registration/sign_in.html',)
    return render(request, 'registration/sign_in.html')