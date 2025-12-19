from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout  # Aggiungi authenticate e logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from curriculum.models import *
from aziende.models import *
from footer.models import *
from contatti.models import *
from django.contrib.auth.forms import UserCreationForm
from curriculum.forms import RegistrazioneStudenteForm

def home(request):
    footer = Footer_info.objects.first()
    contatti = InformazioniBase.objects.first()
    return render(request, 'main/home.html', { "footer": footer, "contatti": contatti})

def contatti(request):
    return render(request, 'main/contatti.html')
    
def chisiamo(request):
    return render(request, 'main/chi_siamo.html')
    
def offerte_lavoro(request):
    footer = Footer_info.objects.first()
    contatti = InformazioniBase.objects.first()
    return render(request, 'main/offerte-lavoro.html',{ "footer": footer, "contatti": contatti})

def area_aziende(request):
    footer = Footer_info.objects.first()
    contatti = InformazioniBase.objects.first()
    return render(request, 'main/area-aziende.html',{ "footer": footer, "contatti": contatti})

def error_404_view(request, exception):
    footer = Footer_info.objects.first()
    contatti = InformazioniBase.objects.first()
    return render(request, 'main/404.html', status=404)

# === AGGIUNGI QUI LE NUOVE FUNZIONI ===
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, f"Benvenuto/a {username}!")
            return redirect('area_riservata')
        else:
            messages.error(request, "Username o password non corretti.")
    
    return render(request, 'main/login.html')

def logout_view(request):
    logout(request)
    messages.success(request, "Logout effettuato con successo!")
    return redirect('home')
# === FINE AGGIUNTE ===

def register(request):
    if request.method == "POST":
        form = RegistrazioneStudenteForm(request.POST, request.FILES)
        if form.is_valid():
            # 1. Salva l'utente
            user = form.save(commit=False)
            user.email = form.cleaned_data["email"]
            user.save()

            # 2. Salva DatiPersonali collegato all'utente
            DatiPersonali.objects.create(
                user=user,
                nome=form.cleaned_data["nome"],
                cognome=form.cleaned_data["cognome"],
                data_nascita=form.cleaned_data["data_nascita"],
                indirizzo=form.cleaned_data["indirizzo"],
                telefono=form.cleaned_data["telefono"],
                email=form.cleaned_data["email"],
                sito_web=form.cleaned_data["sito_web"],
                foto=form.cleaned_data.get("foto")
            )

            # 3. Login automatico
            login(request, user)
            messages.success(request, "Registrazione completata con successo!")
            return redirect("area_riservata")

    else:
        form = RegistrazioneStudenteForm()

    return render(request, "main/register.html", {"form": form})

@login_required
def area_riservata(request):
    try:
        dati = DatiPersonali.objects.get(user=request.user)
        esperienze = EsperienzaLavorativa.objects.filter(candidato=dati)
        competenze = Competenza.objects.filter(candidato=dati)
        
        return render(request, "main/area_riservata.html", {
            "dati": dati,
            "esperienze": esperienze,
            "competenze": competenze,
        })
    except DatiPersonali.DoesNotExist:
        return render(request, "main/area_riservata.html", {
            "dati": None,
            "esperienze": [],
          })