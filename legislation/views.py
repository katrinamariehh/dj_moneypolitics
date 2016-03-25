from django.shortcuts import render
from django.views.generic import ListView
from .models import Legislator, Bill, Vote

# Create your views here.


class LegislatorView(ListView):
    model = Legislator


class BillView(ListView):
    model = Bill


class VoteView(ListView):
    model = Vote
