from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def details(request):
    return render(request,'details.html')

def event(request):
    return render(request,'event.html')

def error(request):
    return render(request,'404-error.html')

def booking(request):
    return render(request,'booking.html')
'''
class ContactView(View):
    template_name='contact.html'
    def get(self,requst):
        contacts = Contact.objects.all()'''