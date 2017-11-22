from django.views.generic.edit import CreateView, FormMixin
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django import forms
from django.urls import reverse

from reportlab.pdfgen import canvas
from django.http import HttpResponse

from forwarder.models import Application, Hierarchy

class ForwardForm(forms.Form):
    pass

class ApplicationCreate(CreateView):
    model = Application
    template_name = 'forwarder/application_create.html'
    fields = ['type', 'other']
    success_url = "/listApplication"

    def form_valid(self, form):
        form.instance.applicant = self.request.user
        return super(ApplicationCreate, self).form_valid(form)


class ListApplicationView(ListView):
    template_name = 'forwarder/list.html'

    def get_queryset(self):
        user = self.request.user
        hierarchies = Hierarchy.objects.all()

        #TODO: Generalize
        if(user.designation == 'st'):
            qs = Application.objects.filter(applicant=user)
        elif(user.designation == 'tu'):
            #for hr in hierarchies:
            #    qs += Application.objects.filter(applicant__branch=user.branch)
            qs = Application.objects.filter(applicant__branch=user.branch, hierarchy_level=0)
        elif(user.designation == 'ho'):
            #for hr in hierarchies:
            #    qs += Application.objects.filter(applicant__branch=user.branch)
            qs = Application.objects.filter(applicant__branch=user.branch, hierarchy_level=1)
        else:
            qs = Application.objects.filter(hierarchy_level=2)


        return qs


class ApplicationDetailView(FormMixin, DetailView):
    model = Application
    template_name = 'forwarder/detail.html'
    form_class = ForwardForm

    def get_context_data(self, **kwargs):
        context = super(ApplicationDetailView, self).get_context_data(**kwargs)
        context['form'] = self.get_form()
        return context

    def get_success_url(self):
        return reverse("list-application")

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
            self.object.hierarchy_level += 1
            self.object.save()
        if '_reject' in self.request.POST:
            self.object.hierarchy_level -= 1
            self.object.save()
            pass
        return super(ApplicationDetailView, self).form_valid(form)


def pdf_dl(request, pk):
    # Create the HttpResponse object with the appropriate PDF headers.
    application = Application.objects.get(pk=pk)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="%s.pdf"' % (application)

    # Create the PDF object, using the response object as its "file."
    p = canvas.Canvas(response)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 800, "Name : " + application.applicant.name)
    p.drawString(100, 780, "Admission no : " + str(application.applicant.admn_no))
    p.drawString(100, 760, "Department : " + application.applicant.branch)
    p.drawString(100, 740, "Semester : " + str(application.applicant.semester))
    p.drawString(100, 720, "Parent name : " + application.applicant.parent_name)

    if application.type == "OTH":
        p.drawString(100, 700, "Application type : " + application.other())
    else:
        p.drawString(100, 700, "Application type : " + application.get_type_display())

    p.drawString(100, 680, "Recommended by HOD of " + application.applicant.branch)


    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()
    return response
