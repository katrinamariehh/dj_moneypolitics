from django.conf.urls import patterns, include, url
from django.contrib import admin
from legislation.views import LegislatorView, BillView, VoteView
from campaign_finance.views import ContributionView

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^legislators/$', LegislatorView.as_view()),
    url(r'^bills/$', BillView.as_view()),
    url(r'^votes/$', VoteView.as_view()),
    url(r'^contributions/$', ContributionView.as_view())
)
