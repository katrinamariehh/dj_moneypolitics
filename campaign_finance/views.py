from django.db import connection
from django.shortcuts import render
from django.views.generic import ListView
from .models import Contribution
# Create your views here.

# query to get money in oil and gas
# Contribution.objects.filter(real_code__in=['E0000', 'E1000', 'E1100', 'E1110', 'E1120', 'E1140', 'E1150', 'E1160', 'E1170', 'E1180'])


class ContributionView(ListView):
    model = Contribution
    queryset = Contribution.objects.filter(real_code__in=['E0000', 'E1000', 'E1100', 'E1110', 'E1120', 'E1140', 'E1150', 'E1160', 'E1170', 'E1180'])


class OilContributionView(ListView):
    model = Contribution
    template_name = 'campaign_finance/oil_contribution.html'
    # queryset = Contribution.objects.raw("select sum(amount), recip_id from campaign_finance_contribution where real_code in ('E0000', 'E1000', 'E1100', 'E1110', 'E1120', 'E1140', 'E1150', 'E1160', 'E1170', 'E1180') group by recip_id")

    def get_queryset(self):
        cursor = connection.cursor()
        cursor.execute(
            "select legislation_legislator.last_name, legislation_legislator.first_name, sum(campaign_finance_contribution.amount), legislation_vote.vote_value, left(legislation_vote.vote_id, 1) as chamber from campaign_finance_contribution join legislation_legislator on campaign_finance_contribution.recip_id = legislation_legislator.opensecrets_id join legislation_vote on legislation_vote.legislator_id = legislation_legislator.bioguide_id or legislation_vote.legislator_id = legislation_legislator.lis_id where real_code in ('E0000', 'E1000', 'E1100', 'E1110', 'E1120', 'E1140', 'E1150', 'E1160', 'E1170', 'E1180') group by (campaign_finance_contribution.recip_id, legislation_legislator.last_name, legislation_legislator.first_name, legislation_legislator.bioguide_id, legislation_legislator.lis_id, legislation_vote.vote_value, chamber);")
        columns = [col[0] for col in cursor.description]
        results = [dict(zip(columns, row)) for row in cursor.fetchall()]
        house = []
        senate = []
        for legislator in results:
            if legislator['chamber'] == 'h':
                house.append(legislator)
            else:
                senate.append(legislator)
        return [{'name': "senate", "legislators": senate}, {'name': 'house', "legislators": house}]
