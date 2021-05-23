from django.shortcuts import render,redirect 
from django.contrib.auth.hashers import make_password
from store.models.customer import Customer
from django.views import View

class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self, request):
        postData = request.POST
        first_name =postData.get('firstname')
        last_name =postData.get('lastname')
        mobile=postData.get('mobile')
        email=postData.get('email')
        password=postData.get('password')
        #validation
        value={
            'first_name' : first_name,
            'last_name' : last_name,
            'mobile' : mobile,
            'email': email
        }
        customer=Customer(first_name=first_name,
                                last_name=last_name,
                                 mobile=mobile,
                                email=email,
                                password=password)
        error_message=None
        if (not first_name):
            error_message='First name is requird...'
        elif len(first_name)<4:
            error_message='First name must be above 4 charactor'
        elif (not last_name):
            error_message='Last name is requird...'
        elif len(last_name)<4:
            error_message='Last name must be above 4 charactor'
        elif (not mobile):
            error_message='Mobile number requird...'
        elif len(mobile)<4:
            error_message='Mobile Number must be 10 Char'
        elif len(email)<5:
            error_message='email must be 5 char above'
        elif len(password)<5:
            error_message='password must be 5 char above'
        elif customer.isExists():
            error_message='Email id already registered'


        #saving
        if not error_message:
            
            print(first_name , last_name , mobile , email , password)
            customer.password=make_password(customer.password)
            customer.register()
            return redirect('homepage')
        else:

            data = {
                'error' : error_message,
                'values':value
            }

            return render(request,'signup.html', data)


       
