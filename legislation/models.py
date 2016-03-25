from django.db import models, DataError
import csv

# Create your models here.


class LegislatorManager(models.Manager):
    def load_current_legislators(self, path):
        with open(path) as f:
            reader = csv.reader(f, delimiter=',')
            f.readline()
            for row in reader:
                last_name, first_name, birthday, gender, type, \
                    state, district, party, url, address, phone, \
                    contact_form, rss_url, twitter, facebook, \
                    facebook_id, youtube, youtube_id, bioguide_id, \
                    thomas_id, opensecrets_id, lis_id, cspan_id, \
                    govtrack_id, votesmart_id, ballotpedia_id, \
                    washington_post_id, icpsr_id, wikipedia_id = row
                legislator = Legislator(
                    last_name=last_name,
                    first_name=first_name,
                    leg_type=type,
                    state=state,
                    district=district,
                    party=party,
                    bioguide_id=bioguide_id,
                    thomas_id=thomas_id,
                    opensecrets_id=opensecrets_id,
                    lis_id=lis_id,
                    govtrack_id=govtrack_id
                )
                legislator.save()


class Legislator(models.Model):
    last_name = models.CharField(max_length=30)
    first_name = models.CharField(max_length=30)
    leg_type = models.CharField(max_length=5)
    state = models.CharField(max_length=2)
    district = models.CharField(max_length=3)
    party = models.CharField(max_length=30)
    bioguide_id = models.CharField(max_length=15)
    thomas_id = models.CharField(max_length=15)
    opensecrets_id = models.CharField(max_length=15)
    lis_id = models.CharField(max_length=10)
    govtrack_id = models.CharField(max_length=15)


class Bill(models.Model):
    congress = models.IntegerField()
    bill_type = models.CharField(max_length=5)
    title = models.CharField(max_length=50, null=True)


class Vote(models.Model):
    bill_id = models.CharField(max_length=10)
    vote_id = models.CharField(max_length=30)
    legislator_id = models.CharField(max_length=15)
    legislator_id_type = models.CharField(max_length=15)
    vote_value = models.CharField(max_length=15)
    vote_type = models.CharField(max_length=15)
    bill_object = models.ForeignKey(Bill)
