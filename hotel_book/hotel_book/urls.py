from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from hotel_web_book import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hotel_book.views.home', name='home'),
    # url(r'^hotel_book/', include('hotel_book.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.hotel_home,name='hotel_home'),
    url(r'^hotel_price_home$',views.hotel_price_home,name='hotel_price'),
    url(r'^hotel_price$',views.hotel_price,name='hotel_price_submit')


)
