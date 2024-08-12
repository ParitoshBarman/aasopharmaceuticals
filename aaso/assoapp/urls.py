from django.contrib import admin
from django.urls import path
from assoapp import views
# import views
# from django.contrib.sitemaps.views import sitemap
# from autoimgProject.sitemaps import StaticViewsSitemap

# sitemaps = {
#     'sitemap': StaticViewsSitemap
# }




urlpatterns = [
    path("", views.index, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact'),
    path("services", views.services, name='services'),
    path("products", views.products, name='products'),
    path("alldrugs", views.alldrugs, name='alldrugs'),
    path("privacypolicy", views.privacypolicy, name='privacypolicy'),
    path("termsconditions", views.termsconditions, name='termsconditions'),
    path("faq", views.faq, name='faq'),

    path("test", views.testfunc, name='testfunc'),
    path("base", views.base, name='base'),
    
    # path("sitemap.xml", sitemap, {"sitemaps": sitemaps}, name="django.contrib.sitemaps.views.sitemap"),
    
]