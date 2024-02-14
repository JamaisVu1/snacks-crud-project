from django.views.generic import TemplateView, ListView
from .models import Snack


class HomePageView(TemplateView):
    template_name='home.html'
    
class AboutView(TemplateView):
    template_name = 'about.html'
    
class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'