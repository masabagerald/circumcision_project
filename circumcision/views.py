from django.shortcuts import render
from django.shortcuts import render, redirect

from circumcision.models import Client
from circumcision.models import Surgery
from circumcision.models import FollowUpVisit
from circumcision.models import Religion
from circumcision.models import Tribe
from circumcision.forms import ClientForm ,RegisterForm

from .forms import RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    clients = Client.objects.count()
    total_surgeries = Surgery.objects.count()
    #total_followups = FollowUpVisit.objects.count()
    return render(request, 'index.html', {'total_clients': clients,'total_surgeries':total_surgeries,})

@login_required
def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})
@login_required
def client_regsitration(request):
    religions = Religion.objects.all()
    tribes = Tribe.objects.all()
   

    return render(request, 'client_registration.html', {'religions':religions,'tribes':tribes,'education_choices': Client.EDUCATION_CHOICES,'marital_status':Client.MARITAL_STATUS_CHOICES})
@login_required
def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()  # This saves the data to the database.
            return redirect('list_clients')  # Redirect to a success page or listing page.
    else:
        form = ClientForm()

    return render(request, 'client_registration.html', {'form': form})

@login_required
def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            authenticated_user = authenticate(username=user.username, password=form.cleaned_data['password'])
            login(request, authenticated_user)
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'registration/register.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('/index')
