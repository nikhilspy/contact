from django.shortcuts import render

# Create your views here.
def IndexPage(request):
    return render(request,"app/index.html")

def RegisterPage(request):
    return render(request, "app/register.html")

def LoginPage(request):
    return render(request,"app/login.html")

def ContactPage(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        msg = request.POST['msg']
    return render(request,"app/contact.html")