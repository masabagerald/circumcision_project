from pyexpat.errors import messages
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.urls import reverse

from circumcision.models import Client, MedicalHistory,Surgery,FollowUpVisit,Religion,Tribe,CircumcisionProcedure


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
     
   

    return render(request, 'client_registration.html', {'religions':religions,'tribes':tribes,'education_choices': Client.EDUCATION_CHOICES,'marital_status':Client.MARITAL_STATUS_CHOICES,
                                                        'payment_method':Client.PAYMENT_METHODS,'hiv_status_choices':MedicalHistory.HIV_STATUS_CHOICES})
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
    visits = FollowUpVisit.objects.filter(Client=client)
    procedures = CircumcisionProcedure.objects.filter(client=client)
   
    return render(request, 'clients\clients_dashboard.html',{'client': client,'visits':visits,'procedures':procedures})



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
                procedure_type=form.cleaned_data['procedure_type'],
                ring_size=form.cleaned_data['ring_size'],
                circumciser_name=form.cleaned_data['name_of_circumciser'],
                # type_of_adverse_event=form.cleaned_data['adverse_events'],
                severity_of_adverse_event=form.cleaned_data['adverse_event_details'],
                # ... populate other fields ...
            )
            # Save the new instance to the database
                circumcision_procedure.save()

                # Now handle the many-to-many fields
                type_of_adverse_events = form.cleaned_data.get('type_of_adverse_event')
                if type_of_adverse_events:
                    circumcision_procedure.type_of_adverse_event.set(type_of_adverse_events)
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



def follow_up_visit_detail(request, visit_id):
    visit = get_object_or_404(FollowUpVisit, id=visit_id)
    return render(request, 'clients/follow_up_visit_detail.html', {'visit': visit})


def edit_follow_up_visit(request, visit_id):
    visit = get_object_or_404(FollowUpVisit, pk=visit_id)
    if request.method == 'POST':
        form = FollowUpVisitForm(request.POST, instance=visit)
        if form.is_valid():
            form.save()
            return redirect('follow_up_visit_detail', visit_id=visit.id)
    else:
        form = FollowUpVisitForm(instance=visit)
    return render(request, 'clients/edit_follow_up_visit.html', {'form': form, 'visit': visit})

def procedure_details(request, procedure_id):
    # Get the procedure by id or return a 404 error if not found
    procedure = get_object_or_404(CircumcisionProcedure, id=procedure_id)
    return render(request, 'clients/procedure_details.html', {'procedure': procedure})


def procedure_edit(request, procedure_id):
    # Get the procedure object to edit, or return a 404
    procedure = get_object_or_404(CircumcisionProcedure, id=procedure_id)
    
    if request.method == 'POST':
        # If the form has been submitted, process the form data
        form = CircumcisionProcedureForm(request.POST, instance=procedure)
        if form.is_valid():
            # If the form is valid, save the changes and redirect to the details view
            form.save()
            return redirect(reverse('procedure_details', args=[procedure.id]))
    else:
        # If it's a GET request, instantiate the form with the procedure instance
        form = CircumcisionProcedureForm(instance=procedure)
    
    # Render the edit form template
    return render(request, 'clients/procedure_edit.html', {'form': form, 'procedure': procedure})



