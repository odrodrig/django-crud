from django.http import HttpResponse
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy

from postgresqlCRUD.models import People

class PeopleCreate(CreateView):
    model = People
    success_url = reverse_lazy('people_list')
    fields = ['first_name', 'last_name', 'email']

#View for listing all of the people.
class PeopleList(ListView):
    model = People
    context_object_name = 'my_peoples'

#View for updating existing people. Returns to list of people when done.
class PeopleUpdate(UpdateView):
    model = People
    success_url = reverse_lazy('people_list')
    fields = ['first_name', 'last_name', 'email']

#View for deleting people. Returns to list of people when done.
class PeopleDelete(DeleteView):
    model = People
    success_url = reverse_lazy('people_list')
