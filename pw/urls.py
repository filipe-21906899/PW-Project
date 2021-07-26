from django.urls import path
from .import views

urlpatterns = [
    path('', views.index_page_view, name='index'),
    path('lol', views.lol_page_view, name='lol'),
    path('wow', views.wow_page_view, name='wow'),
    path('about', views.about_page_view, name='about'),
    path('contact', views.contact_page_view, name='contact'),
    path('Comment', views.Comment_page_view, name='comment'),
    path('quizz', views.quizz_page_view, name='quizz'),
    path('start', views.start_page_view, name='start')
]