from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^profile/$',views.Profile,name = 'userprofile'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^new/post/$', views.new_post, name='post'),
    url(r'^hood/$', views.neighbourhood, name='neighbourhood'),
    url(r'^neighbourhood_display/$', views.neibadisplay, name='displayhood'),
    url(r'^join/(\d+)', views.join, name='joinHood'),
    url(r'^exitHood/(\d+)', views.exitHood, name='exitHood'),
    url(r'^business/$', views.bizdisplay, name='bizdisplay'),
    url(r'^social/$', views.social_ammenities, name='social'),
    url(r'^new/business/$', views.business, name='business'),
    url(r'^new/business/$', views.business, name='business'),
    url(r'^search/', views.search_results, name='search_results')


]
