from django.views.generic.edit import CreateView
from manager.models import Application

# Create your views here.

class ApplicationCreate(CreateView):
    model = Application
    template_name = 'manager/application_create.html'
    fields = ['type', 'other']
