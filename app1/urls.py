from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path("",views.index),
    path("emails_text",views.emails_text,name="emails_txt"),
    # path("analyze",views.analyze,name="analyze_text"),
    path("phone_number_text",views.phone_numbers_text,name='phone_text'),
    path("url_text",views.url_text,name="text_url"),
    # path("web_scrape",views.web_scrape,name="web_scrape"),
    path("download_pdf",views.download_pdf,name="pdf"),
    path("download_pdf_result",views.download_pdf_result,name="download_pdf_res"),
    path("url_scrape",views.url_scrape,name="scrape_url"),
    path("url_scraping_result",views.url_scraping_result,name="scrape_url_res"),
    path('email_scrape',views.emails_scrape,name="scrape_email"),
    path("email_scraping_result",views.emails_scraping_result,name="scrape_email_res"),
    path("phone_number_scrape",views.phone_number_scrape,name="phone_number"),
    path("phone_number_scrape_result",views.phoneNumber_scraping_result,name="phone_scrape_res"),
    path("google_maps",views.google_maps,name="gmaps"),
    path("gmaps_redirect",views.google_maps_redirect,name="gmaps_redirect"),

]