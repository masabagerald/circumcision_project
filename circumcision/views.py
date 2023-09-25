from django.shortcuts import render

from circumcision.models import Client

# Create your views here.
def index(request):
    return render(request, 'index.html')

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})
