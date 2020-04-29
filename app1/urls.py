from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path("",views.index),
    path("analyze",views.analyze,name="analyze_text"),
    path("web_scrape",views.web_scrape,name="web_scrape"),
    path("download_pdf",views.download_pdf,name="pdf"),
    path("url_scraping",views.url_scraping,name="scrape_url"),
    path("email_scraping",views.emails_scraping,name="scrape_email"),
    path("phone_number_scraping",views.phoneNumber_scraping,name="phone_number"),

]