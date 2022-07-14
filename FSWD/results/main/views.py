from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def ccycle(request):
    return render(request,'c_sub.html')

def pcycle(request):
    return render(request,'p_sub.html')

def sem3(request):
    return render(request,'sem3.html')

def sem4(request):
    return render(request,'sem4.html')

def sem5(request):
    return render(request,'sem5.html')

def sem6(request):
    return render(request,'sem6.html')

def chs_branc(request):
    return render(request,'chs_branc.html')

def sem7a(request):
    return render(request,'sem7a.html')

def sem7b(request):
    return render(request,'sem7b.html')

def sem8(request):
    return render(request,'sem8.html')