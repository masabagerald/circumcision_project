from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render, redirect

from circumcision.models import Client,Surgery,FollowUpVisit,Religion,Tribe,CircumcisionProcedure


from circumcision.forms import ClientForm ,RegisterForm,CircumcisionProcedureForm,FollowUpVisitForm

from .forms import RegisterForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404


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


def patient_dashbord(request,client_id):
    client = get_object_or_404(Client, id=client_id)
   
    return render(request, 'clients\clients_dashboard.html',{'client': client})



def logout_view(request):
    logout(request)
    return redirect('/index')


def procedure_form(request,client_id):
    if request.method == 'POST':
        form = CircumcisionProcedureForm(request.POST)
        client = get_object_or_404(Client, id=client_id)
        if form.is_valid():
           
            
                circumcision_procedure = CircumcisionProcedure(
                client = client,
                date_of_circumcision=form.cleaned_data['date_of_circumcision'],
                start_time=form.cleaned_data['start_time'],
                end_time=form.cleaned_data['end_time'],
                local_anesthesia=form.cleaned_data['local_anesthesia'],
                type_of_circumcision=form.cleaned_data['type_of_circumcision'],
                ring_size=form.cleaned_data['ring_size'],
                name_of_circumciser=form.cleaned_data['name_of_circumciser'],
                adverse_events=form.cleaned_data['adverse_events'],
                adverse_event_details=form.cleaned_data['adverse_event_details'],
                # ... populate other fields ...
            )
            # Save the new instance to the database
                circumcision_procedure.save()
                return redirect('patient_dashbord',client_id=client.id)  # Replace with the name of your success page
    else:
        form = CircumcisionProcedureForm()

    return render(request, 'clients\procedure_form.html', {'form': form})



def visit_form(request,client_id):
    if request.method == 'POST':
        form = FollowUpVisitForm(request.POST)
        client = get_object_or_404(Client, id=client_id)
        if form.is_valid():
            follow_up_visit = form.save(commit=False)
            # ... perform any custom actions needed before saving ...
            follow_up_visit.save()
            # If your model has many-to-many fields, you need to save them after the initial save.
            form.save_m2m()
            messages.success(request, 'Follow up visit saved successfully!')
            return redirect('patient_dashbord',client_id=client.id)
    else:
        form = FollowUpVisitForm()
    
    context = {
        'form': form,
    }
    return render(request, 'clients\\visit_form.html', context)


