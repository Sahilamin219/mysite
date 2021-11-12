from django.shortcuts import render
from django.http import HttpResponse
# from django.contrib.auth.models import User
# from django.contrib.auth import authenticate, login
from .models import Signup
from django import forms
from .forms import UserRegistrationForm

#render is used to render templates
# Create your views here.
def homepage(request):
	return render(request=request,
		template_name="main/home.html",
		context ={"tutorials": Tutorial.objects.all})
def homepage(request):
	return render(request=request,
		template_name="main/signin.html",
		context ={"signin": Signup.objects.all})
def home(request):
 	return render(request, 'mysite/about.html')
def register(request):
	form = UserCreationForm()
	return render(request, 'models/forms.html',{'form':form})
def about(request):
	# return HttpResponse('<h1>Jamia Materials</h1>')
	return render(request, 'main/about.html')
# def register(request):
#  	if request.method == 'POST':
#  		form = UserRegistrationForm(request.POST)
#  		if form.is_valid():
#  			UserObj = form.cleaned_data
#  			username = userObj["username"]
#  			email = userObj['email']
#  			password = userObj["password"]
#  			if not (User.objects.filter(username=username).exits() or User.objects.filter(email=email).exits()):
#  				User.objects.create_user(username, email, password)
#  				user = authenticate(username = username, password=password)
#  				login(request, user)
#  				return HttpResponseRedirect('/')

#  			else:
#  				raise forms.ValidationError('Looks like a username with that email or password already exists')

#  	else:
#  		form = UserRegistrationForm()

#  	return render(request, 'mysite/signin.html', {'form': form})


# from django.contrib.auth import login, authenticate
# from django.shortcuts import render, redirect

# from mysite.core.forms import SignUpForm

# def login(request):
#     if request.method == 'POST':
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = UserRegistrationForm()
#     return render(request, 'login.html', {'form': form})
