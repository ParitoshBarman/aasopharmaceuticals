from django.shortcuts import render, HttpResponse



def index(request):
    # return HttpResponse('<h1>Welcome to AASO</h1>')
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')
def services(request):
    return render(request,'services.html')
def products(request):
    return render(request,'products.html')
def alldrugs(request):
    return render(request,'alldrugs.html')

def testfunc(request):
    # return HttpResponse('<h1>Welcome to AASO</h1>')
    return render(request,'test.html')
def base(request):
    return render(request,'base.html')
