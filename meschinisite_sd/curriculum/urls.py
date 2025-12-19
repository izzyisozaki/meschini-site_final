from django.urls import path
from . import views

app_name = 'curriculum'

urlpatterns = [
    # URL per aggiungere nuova esperienza
    path('esperienza/aggiungi/', views. aggiungi_esperienza, name='aggiungi_esperienza'),
    # URL per modificare esperienza esistente
    # <int:pk> cattura un numero dall'URL e lo passa come parametro 'pk' alla view
    path('esperienza/modifica/<int:pk>/', views.modifica_esperienza, name='modifica_esperienza'),
    # URL per eliminare esperienza esistente
    path('esperienza/elimina/<int:pk>/', views.elimina_esperienza, name='elimina_esperienza'),

    path('competenza/aggiungi/', views. aggiungi_competenza, name='aggiungi_competenza'),
    path('competenza/modifica/<int:pk>/', views.modifica_competenza, name='modifica_competenza'),
    path('competenza/elimina/<int:pk>/', views. elimina_competenza, name='elimina_competenza'),

    path('lingua/aggiungi/', views.aggiungi_lingua, name='aggiungi_lingua'),
    path('lingua/modifica/<int:pk>/', views.modifica_lingua, name='modifica_lingua'),
    path('lingua/elimina/<int:pk>/', views.elimina_lingua, name='elimina_lingua'),

    path('istruzione/aggiungi/', views.aggiungi_istruzione, name='aggiungi_istruzione'),
    path('istruzione/modifica/<int:pk>/', views.modifica_istruzione, name='modifica_istruzione'),
    path('istruzione/elimina/<int:pk>/', views.elimina_istruzione, name='elimina_istruzione'),

    path('certificazione/aggiungi/', views. aggiungi_certificazione, name='aggiungi_certificazione'),
    path('certificazione/modifica/<int:pk>/', views.modifica_certificazione, name='modifica_certificazione'),
    path('certificazione/elimina/<int:pk>/', views. elimina_certificazione, name='elimina_certificazione'),

    path('progetto/aggiungi/', views.aggiungi_progetto, name='aggiungi_progetto'),
    path('progetto/modifica/<int:pk>/', views.modifica_progetto, name='modifica_progetto'),
    path('progetto/elimina/<int:pk>/', views.elimina_progetto, name='elimina_progetto'),

    path('referenza/aggiungi/', views.aggiungi_referenza, name='aggiungi_referenza'),
    path('referenza/modifica/<int:pk>/', views.modifica_referenza, name='modifica_referenza'),
    path('referenza/elimina/<int:pk>/', views.elimina_referenza, name='elimina_referenza'),

    path('extrainfo/aggiungi/', views.aggiungi_extrainfo, name='aggiungi_extrainfo'),
    path('extrainfo/modifica/<int:pk>/', views.modifica_extrainfo, name='modifica_extrainfo'),
    path('extrainfo/elimina/<int:pk>/', views.elimina_extrainfo, name='elimina_extrainfo'),
]