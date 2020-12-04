from django.shortcuts import render,redirect
from .models import *
from django.views.generic import View,ListView,DetailView
# Create your views here.
def index(request):
    return render(request,'index.html')

def gallery(request):
    return render(request,'gallery.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

class EventListView(ListView):
    model = Event
    template_name = 'event.html'
    context_object_name = 'events'
    paginate_by = 4
    queryset = Event.objects.order_by('-event_name')[:6]

class EventDetailView(DetailView):
    model = Event
    template_name = 'details.html'

def error(request):
    return render(request,'404-error.html')

def booking(request):
    return render(request,'booking.html')

def test(request):
    return render(request,'test.html')

class ContactView(View):
    template_name = 'contact.html'
    raise_exception = True
    permission_denied_message = 'You must Login Now.'
    def get(self,request):
        return render(request,self.template_name)
    def post(self,request):
        data = request.POST
        contact = Contact()
        contact.name = data['name']
        contact.mail =data['mail']
        contact.counrty = data['counrty']
        contact.phone = data['phone']
        contact.message = data['message']
        contact.save()
        return redirect("contact")
        return render(request,self.template_name)