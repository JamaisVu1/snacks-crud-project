from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Snack
from django.urls import reverse_lazy, reverse


class HomePageView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['snacks'] = Snack.objects.all()  
        return context
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'
    
class SnackDetailView(DetailView):
    model = Snack
    template_name = 'detail.html'

class SnackCreateView(CreateView):
    model = Snack
    template_name = 'create.html'
    fields = ['name', 'purchaser', 'description']
    success_url = reverse_lazy('snack_list')

class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'update.html'
    fields = ['name', 'purchaser', 'description']
    def get_success_url(self):
        return reverse('snack_detail', kwargs={'pk': self.object.pk})

class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'delete.html'
    success_url = reverse_lazy('snack_list')