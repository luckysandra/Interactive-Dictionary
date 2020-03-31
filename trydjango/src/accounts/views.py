from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
# Create your views here.

def login_view(request, *args, **kwargs):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name','')
        user_password = request.POST.get('user_password', '')
        # authenticate user account.
        user = auth.authenticate(request, username=user_name, password=user_password)
        if user is not None:
            # login user account.
            auth.login(request, user)
            response = HttpResponseRedirect('/')
            # set cookie to transfer user name to login success page.
            response.set_cookie('user_name', user_name, 3600)
            return response
        else:
            error_json = {'error_message': 'Никнейм или пароль некорректны.'}
            return render(request, 'login.html', error_json)
    else:
        return render(request, 'login.html')

def signup_view(request, *args, **kwargs):
    request_method = request.method
    print('request_method = ' + request_method)
    if request_method == 'POST':
        user_name = request.POST.get('user_name', '')
        user_password = request.POST.get('user_password', '')
        user_email = request.POST.get('user_email', '')
        if len(user_name) > 0 and len(user_password) > 0 and len(user_email) > 0:
            # check whether user account exist or not.
            user = auth.authenticate(request, username=user_name, password=user_password)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=user_name, password=user_password, email=user_email)
                # update user object staff field value and save to db.
                if user is not None:
                    user.is_staff = False
                    # save user properties in sqlite auth_user table.
                    user.save()
                # redirect web page to register success page.
                response = HttpResponseRedirect('/accounts/register_success/')
                # set user name, pasword and email value in session.
                request.session['user_name'] = user_name
                request.session['user_password'] = user_password
                request.session['user_email'] = user_email
                return response
            else:
                error_json = {'error_message': 'Такой аккаунт уже есть. Пожалуйста, выберите другой никнейм.'}
                return render(request, 'signup.html', error_json)
        else:
            error_json = {'error_message': 'Никнейм, пароль и email должны быть заполнены.'}
            return render(request, 'signup.html', error_json)
    else:
        return render(request, 'signup.html')
def success_view(request, *args, **kwargs):
	return render(request, 'register_success.html')