from django.shortcuts import render
from django.shortcuts import render, redirect

from circumcision.models import Client
from circumcision.models import Surgery
from circumcision.models import FollowUpVisit
from circumcision.models import Religion
from circumcision.models import Tribe
from circumcision.forms import ClientForm

# Create your views here.
def index(request):
    clients = Client.objects.count()
    total_surgeries = Surgery.objects.count()
    #total_followups = FollowUpVisit.objects.count()
    return render(request, 'index.html', {'total_clients': clients,'total_surgeries':total_surgeries,})

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})

def client_regsitration(request):
    religions = Religion.objects.all()
    tribes = Tribe.objects.all()
   

    return render(request, 'client_registration.html', {'religions':religions,'tribes':tribes,'education_choices': Client.EDUCATION_CHOICES,'marital_status':Client.MARITAL_STATUS_CHOICES})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the data to the database.
            return redirect('list_clients')  # Redirect to a success page or listing page.
    else:
        form = ClientForm()

    return render(request, 'client_registration.html', {'form': form})
