from django.urls import path

from .views import HomePageView, AboutView, SnackListView

urlpatterns=[
    path('', HomePageView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
     path('snacks/', SnackListView.as_view(), name='snack_list'),

]