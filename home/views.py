from django.shortcuts import render , HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("This is Home Page.......")

    # with variable
    # context = {
    #     'var1':'Piyush is Making this website',
    #     'var2': 'Rahul kumar is Owner of Kumar Path Lab'
    # }
    # return render(request, 'index.html' , context)
# without variable
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')


def tests(request):
    return render(request, 'tests.html')