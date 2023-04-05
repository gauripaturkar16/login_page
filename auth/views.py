from django.shortcuts import redirect,render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here
# def home (request):
#     return HttpResponse("helllo ")

def home (request):
    return render(request,"auth/index.html ")



def signup (request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # if User.objects.filter(username=username):
        #     messages.error(request, "Username already exist ! Please try some other username")
        #     return redirect('home')
        
        # if User.objects.filter(email=email):
        #     messages.error(request, "Email already registered !")
        #     return redirect('home')
        
        # if len(username)>10:
        #     messages.error(request, "Username must be under 10 characters")
          
        
        # if pass1 != pass2:
        #     messages.error(request, "Password didn't match !")
           
        
        # if len(pass1)<8:
        #     messages.error(request, "Password must be less than 8 character !")

        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name= fname
        myuser.last_name= lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")
        return redirect('signin')

    return render(request,"auth/signup.html ")




def signin (request):

    if request.method =='POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']     #() hi line khalchi ahe 
        user = authenticate(username=username, password=pass1) 
        # user = authenticate()
        # messages.success(request, "Thank you for logIn.")

        if user is not None:
            login(request, user)
            fname = user.first_name
            return render(request,"auth/index.html",{'fname': fname})
        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')

    return render(request,"auth/signin.html ")




def signout (request):
    logout(request)
    messages.success(request, "Logged Out Successful")
    return redirect('home')