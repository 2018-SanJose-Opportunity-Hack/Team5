from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    return render(request,"scratcher/index.html")

def welcome(request):
    if 'user' not in request.session:
        request.session.clear()
        return redirect ("/")
    else:
        return redner(request, "scratcher/welcome.html")

def createEmail(request):
    if request.method == 'POST':
        User.objects.create(
            email = request.POST['email'],
            current_balance = request.POST['balance'],
            saving_category = request.POST['scategory'],
            delta = request.POST['delta']
        )
        user = User.objects.get(email=request.POST['email'])
        request.session['user'] = user.email
        return redirect ("/welcome")
    else:
        return redirect ("/")

def login(request):
    if request.method == 'POST':
        if len(User.objects.filter(email=request.POST['email']))==0:
            request.session.clear()
            return redirect("/")
        else:
            user = User.objects.get(email=request.POST['email'])
            request.session['user'] = user.email
            return redirect ("/welcome")