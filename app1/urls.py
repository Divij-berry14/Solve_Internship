from django.contrib import admin
from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView

urlpatterns = [
    path('',views.indexView, name='home'),
    path('register',views.register,name='register_url'),
    path('login',LoginView.as_view(),name="login_url"),
    path('logout',LogoutView.as_view(next_page='app1:login_url'),name="logout"),
    path("home",views.index1,name="index1"),
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
    path("youtube_download",views.youtube_download,name="ytube"),
    path("youtube_download_res",views.youtube_download_res,name="ytube_res"),
    path("upload_audio",views.upload_audio,name="audio"),
    path('audio_text',views.audio_text,name='audio_txt'),
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)