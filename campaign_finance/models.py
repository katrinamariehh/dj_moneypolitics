from django.db import models, DataError
import csv
from datetime import datetime

# Create your models here.


class ContributionManager(models.Manager):
    def create_contribution_records(self, path):
        with open(path) as f:
            reader = csv.reader(f, delimiter=',')
            f.readline()
            for row in reader:
                try:
                    Cycle, Fectransid, Contribid, Contrib, Recipid, \
                        Orgname, Ultorg, Realcode, Date, Amount, \
                        Street, City, State, Zip, Recipcode, Type, \
                        CmteId, OtherID, Gender, Microfilm, \
                        Occupation, Employer, Source = row
                except ValueError:
                    import pdb; pdb.set_trace()
                contribution = Contribution(
                    cycle=Cycle,
                    contrib_id=Contribid,
                    contrib=Contrib,
                    recip_id=Recipid,
                    org_name=Orgname,
                    ult_org=Ultorg,
                    real_code=Realcode,
                    amount=Amount,
                    recip_code=Recipcode,
                    transaction_type=Type,
                    cmte_id=CmteId,
                    other_id=OtherID,
                    occupation=Occupation,
                    employer=Employer,
                    source=Source
                )
                try:
                    contribution.save()
                except UnicodeDecodeError:
                    continue


class Contribution(models.Model):
    cycle = models.IntegerField()
    contrib_id = models.CharField(max_length=12)
    contrib = models.CharField(max_length=50)
    recip_id = models.CharField(max_length=9)
    org_name = models.CharField(max_length=50)
    ult_org = models.CharField(max_length=50, blank=True)
    real_code = models.CharField(max_length=5)
    amount = models.IntegerField()
    recip_code = models.CharField(max_length=2)
    transaction_type = models.CharField(max_length=3)
    cmte_id = models.CharField(max_length=9)
    other_id = models.CharField(max_length=9)
    occupation = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    source = models.CharField(max_length=5)


class CandidateManager(models.Manager):
    def create_candidate_records(self, path):
        with open(path) as f:
            reader = csv.reader(f, delimiter=',', quotechar='|')
            for row in reader:
                Cycle, FECCandId, CID, FirstLastP, Party, DistIdRunFor, \
                    DistIdCurr, CurrCand, CycleCand, CRPICO, RecipCode, \
                    NoPacs = row
                candidate = Candidate(
                    cycle=Cycle,
                    fec_cand_id=FECCandId,
                    cid=CID,
                    first_last_p=FirstLastP,
                    party=Party,
                    dist_id_run_for=DistIdRunFor,
                    dist_id_curr=DistIdCurr,
                    curr_cand=CurrCand,
                    cycle_cand=CycleCand,
                    crpico=CRPICO,
                    recip_code=RecipCode,
                    no_pacs=NoPacs)
                candidate.save()


class Candidate(models.Model):
    cycle = models.IntegerField()
    fec_cand_id = models.CharField(max_length=9)
    cid = models.CharField(max_length=9)
    first_last_p = models.CharField(max_length=50)
    party = models.CharField(max_length=1)
    dist_id_run_for = models.CharField(max_length=4)
    dist_id_curr = models.CharField(max_length=4)
    curr_cand = models.CharField(max_length=1)
    cycle_cand = models.CharField(max_length=1)
    crpico = models.CharField(max_length=1)
    recip_code = models.CharField(max_length=2)
    no_pacs = models.CharField(max_length=1)


class CommitteeManager(models.Manager):
    def create_committee_records(self, path):
        with open(path) as f:
            reader = csv.reader(f, delimiter=',', quotechar='|')
            for row in reader:
                Cycle, CmteID, PACShort, Affiliate, Ultorg, RecipID, \
                    RecipCode, FECCandID, Party, PrimCode, Source, \
                    Sensitive, Foreign, Active = row
                committee = Committee(
                    cycle=Cycle,
                    cmte_id=CmteID,
                    pac_short=PACShort,
                    affiliate=Affiliate,
                    ultorg=Ultorg,
                    recip_id=RecipID,
                    recip_code=RecipCode,
                    fec_cand_id=FECCandID,
                    party=Party,
                    prim_code=PrimCode,
                    source=Source,
                    sensitive=Sensitive,
                    foreign=Foreign,
                    active=Active
                    )
                try:
                    committee.save()
                # Maersk causes this problem
                except UnicodeDecodeError:
                    committee = Committee(
                        cycle=Cycle,
                        cmte_id=CmteID,
                        pac_short=PACShort,
                        affiliate=Affiliate,
                        ultorg=PACShort,
                        recip_id=RecipID,
                        recip_code=RecipCode,
                        fec_cand_id=FECCandID,
                        party=Party,
                        prim_code=PrimCode,
                        source=Source,
                        sensitive=Sensitive,
                        foreign=Foreign,
                        active=Active
                        )
                    committee.save()


class Committee(models.Model):
    cycle = models.IntegerField()
    cmte_id = models.CharField(max_length=9)
    pac_short = models.CharField(max_length=50)
    affiliate = models.CharField(max_length=50)
    ultorg = models.CharField(max_length=50)
    recip_id = models.CharField(max_length=9)
    recip_code = models.CharField(max_length=2)
    fec_cand_id = models.CharField(max_length=9)
    party = models.CharField(max_length=1)
    prim_code = models.CharField(max_length=5)
    source = models.CharField(max_length=10)
    sensitive = models.CharField(max_length=1)
    foreign = models.CharField(max_length=1)
    active = models.IntegerField()


class IndividualManager(models.Manager):
    def create_individual_records(self, path):
        with open(path) as f:
            reader = csv.reader(f, delimiter=',', quotechar='|')
            counter = 0
            for row in reader:
                counter += 1
                # if counter == 14352:
                #     continue
                # if counter <= 14300:
                #     continue
                try:
                    Cycle, FECTransId, ContribID, Contrib, RecipID, \
                        Orgname, UltOrg, RealCode, Date, Amount, \
                        Street, City, State, Zip, RecipCode, Type, \
                        CmteID, OtherID, Gender, Microfilm, Occupation, \
                        Employer, Source = row
                except UnicodeDecordError:
                    import pdb; pdb.set_trace()
                if Date == '':
                    continue
                Date = datetime.strptime(Date, "%m/%d/%Y")
                # try:
                #     bytes = str.encode(Orgname)
                #     bytes.decode('utf8')
                # except UnicodeDecodeError:
                #     Orgname = ''
                # try:
                #     bytes = str.encode(UltOrg)
                #     bytes.decode('utf8')
                # except UnicodeDecodeError:
                #     UltOrg = ''
                individual = Individual(
                    cycle=Cycle,
                    fec_trans_id=FECTransId,
                    contrib_id=ContribID,
                    recip_id=RecipID,
                    org_name=Orgname,
                    ultorg=UltOrg,
                    real_code=RealCode,
                    date=Date,
                    amount=Amount,
                    street=Street,
                    city=City,
                    zip_code=Zip,
                    recip_code=RecipCode,
                    transaction_type=Type,
                    cmte_id=CmteID,
                    other_id=OtherID,
                    gender=Gender,
                    microfilm=Microfilm,
                    occupation=Occupation,
                    employer=Employer,
                    source=Source
                )
                try:
                    individual.save()
                except (UnicodeDecodeError, ImportError):
                    continue
                if counter % 1000 == 0:
                    print(counter)
                # print(counter)


class Individual(models.Model):
    cycle = models.IntegerField()
    fec_trans_id = models.CharField(max_length=19)
    contrib_id = models.CharField(max_length=12)
    contrib = models.CharField(max_length=50)
    recip_id = models.CharField(max_length=9)
    org_name = models.CharField(max_length=50)
    ultorg = models.CharField(max_length=50, blank=True)
    real_code = models.CharField(max_length=5)
    date = models.DateField(blank=True)
    amount = models.IntegerField()
    street = models.CharField(max_length=40)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    recip_code = models.CharField(max_length=2)
    transaction_type = models.CharField(max_length=3)
    cmte_id = models.CharField(max_length=9)
    other_id = models.CharField(max_length=9)
    gender = models.CharField(max_length=1)
    microfilm = models.CharField(max_length=20)
    occupation = models.CharField(max_length=50)
    employer = models.CharField(max_length=50)
    source = models.CharField(max_length=5)


class Pac(models.Model):
    cycle = models.IntegerField()
    fec_rec_no = models.CharField(max_length=19)
    pac_id = models.CharField(max_length=9)
    cid = models.CharField(max_length=9)
    amount = models.FloatField()
    date = models.DateField()
    real_code = models.CharField(max_length=5)
    transaction_type = models.CharField(max_length=3)
    di = models.CharField(max_length=1)
    fec_cand_id = models.CharField(max_length=9)


class PacToPac(models.Model):
    cycle = models.IntegerField()
    fec_rec_no = models.CharField(max_length=19)
    filer_id = models.CharField(max_length=8)
    donor_cmte = models.CharField(max_length=50)
    contrib_lend_trans = models.CharField(max_length=50)
    city = models.CharField(max_length=30)
    state = models.CharField(max_length=2)
    zip_code = models.CharField(max_length=5)
    fec_occ_emp = models.CharField(max_length=38)
    prim_code = models.CharField(max_length=5)
    date = models.DateField()
    amount = models.FloatField()
    recip_id = models.CharField(max_length=9)
    party = models.CharField(max_length=1)
    other_id = models.CharField(max_length=9)
    recip_code = models.CharField(max_length=2)
    recip_prim_code = models.CharField(max_length=5)
    amend = models.CharField(max_length=1)
    report = models.CharField(max_length=3)
    pg = models.CharField(max_length=2)
    microfilm = models.CharField(max_length=11)
    transaction_type = models.CharField(max_length=3)
    real_code = models.CharField(max_length=5)
    source = models.CharField(max_length=5)
