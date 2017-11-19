from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django import forms

from forwarder.models import Application

class ForwardForm(forms.Form):
    pass

class ApplicationCreate(CreateView):
    model = Application
    template_name = 'forwarder/application_create.html'
    fields = ['type', 'other']
    success_url = "/createApplication"

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super(ApplicationCreate, self).form_valid(form)


class ListApplicationView(ListView):
    model = Application
    template_name = 'forwarder/list.html'


class ApplicationDetailView(FormMixin, DetailView):
    model = Application
    template_name = 'forwarder/detail.html'
    form_class = ForwardForm

    def get_context_data(self, **kwargs):
        context = super(ApplicationDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def post(self, request, *args, **kwargs):
        #if not request.user.is_authenticated:
        #    return HttpResponseForbidden()
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        # Here, we would record the user's interest using the message
        # passed in form.cleaned_data['message']
        if '_forward' in self.request.POST:
            pass
        if '_reject' in self.request.POST:
            pass
        return super(ApplicationDetailView, self).form_valid(form)
