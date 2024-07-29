from django.shortcuts import render

# Create your views here.
def index(request):
    request.session.flush()
    return render(request, 'index.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'login/login.html')

    if request.method == 'POST':
        return render(request, 'login/loginresult.html')