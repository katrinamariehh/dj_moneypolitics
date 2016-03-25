from django.shortcuts import render
from django.views.generic import ListView
from .models import Contribution
# Create your views here.

# query to get money in oil and gas
# Contribution.objects.filter(real_code__in=['E0000', 'E1000', 'E1100', 'E1110', 'E1120', 'E1140', 'E1150', 'E1160', 'E1170', 'E1180'])


class ContributionView(ListView):
    model = Contribution
    queryset = Contribution.objects.filter(real_code__in=['E0000', 'E1000', 'E1100', 'E1110', 'E1120', 'E1140', 'E1150', 'E1160', 'E1170', 'E1180'])
