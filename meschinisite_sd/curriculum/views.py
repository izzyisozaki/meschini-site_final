from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import (
    DatiPersonali,
    EsperienzaLavorativa,
    Competenza,
    Lingua,
    Istruzione,
    Certificazione,
    Progetto,
    Referenza,
    ExtraInfo
)
from .forms import (
    EsperienzaLavorativaForm,
    CompetenzaForm,
    LinguaForm,
    IstruzioneForm,
    CertificazioneForm,
    ProgettoForm,
    ReferenzaForm,
    ExtraInfoForm
)



@login_required
def aggiungi_esperienza(request):
    """
    Permette all'utente loggato di aggiungere una nuova esperienza lavorativa
    """
    try:
        # Recupera i DatiPersonali dell'utente loggato
        dati_personali = DatiPersonali. objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages. error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST': 
        form = EsperienzaLavorativaForm(request.POST)
        
        if form.is_valid():
            # Salva il form ma non ancora nel database
            esperienza = form. save(commit=False)
            
            # Collega l'esperienza ai DatiPersonali dell'utente
            esperienza. candidato = dati_personali
            
            # Ora salva nel database
            esperienza.save()
            
            messages.success(request, "Esperienza lavorativa aggiunta con successo!")
            return redirect('area_riservata')
    else:
        # GET request:  mostra il form vuoto
        form = EsperienzaLavorativaForm()
    
    return render(request, 'main/curriculum/esperienza_form.html', {'form': form})

@login_required
def modifica_esperienza(request, pk):
    """
    Permette all'utente loggato di modificare una sua esperienza lavorativa esistente
    pk = Primary Key (ID) dell'esperienza da modificare
    """
    try: 
        # Recupera i DatiPersonali dell'utente loggato
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    # Recupera l'esperienza con quell'ID, MA solo se appartiene all'utente loggato
    # Se non esiste o non è sua → 404
    esperienza = get_object_or_404(EsperienzaLavorativa, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        # Form popolato con i dati inviati dall'utente + l'istanza esistente
        form = EsperienzaLavorativaForm(request.POST, instance=esperienza)
        
        if form. is_valid():
            # Salva le modifiche (non serve commit=False perché candidato è già impostato)
            form.save()
            
            messages.success(request, "Esperienza lavorativa modificata con successo!")
            return redirect('area_riservata')
    else:
        # GET request: mostra il form pre-compilato con i dati attuali
        form = EsperienzaLavorativaForm(instance=esperienza)
    
    return render(request, 'main/curriculum/esperienza_form.html', {
        'form': form,
        'modifica':  True,  # Flag per distinguere "aggiungi" da "modifica" nel template
    })

@login_required
def elimina_esperienza(request, pk):
    """
    Permette all'utente loggato di eliminare una sua esperienza lavorativa
    pk = Primary Key (ID) dell'esperienza da eliminare
    
    GET request:  Mostra pagina di conferma "Sei sicuro?"
    POST request: Esegue l'eliminazione definitiva dal database
    """
    try: 
        # Recupera i DatiPersonali dell'utente loggato
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    # Recupera l'esperienza con quell'ID, MA solo se appartiene all'utente loggato
    # Se non esiste o non è sua → 404 (sicurezza!)
    esperienza = get_object_or_404(EsperienzaLavorativa, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':  
        # POST request: conferma eliminazione
        # Salva il titolo prima di eliminare (dopo . delete() l'oggetto non esiste più)
        titolo = esperienza.titolo
        azienda = esperienza.azienda
        
        # Elimina definitivamente dal database
        esperienza.delete()
        
        # Messaggio di conferma con dettagli dell'esperienza eliminata
        messages.success(request, f"Esperienza '{titolo}' presso {azienda} eliminata con successo!")
        return redirect('area_riservata')
    
    # GET request: mostra pagina di conferma
    # Passa l'oggetto esperienza al template per mostrare i dettagli
    return render(request, 'main/curriculum/esperienza_conferma_elimina.html', {
        'esperienza': esperienza,
    })



@login_required
def aggiungi_competenza(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST': 
        form = CompetenzaForm(request.POST)
        
        if form.is_valid():
            competenza = form.save(commit=False)
            competenza.candidato = dati_personali
            competenza.save()
            
            messages.success(request, "Competenza aggiunta con successo!")
            return redirect('area_riservata')
    else:
        form = CompetenzaForm()
    
    return render(request, 'main/curriculum/competenza_form.html', {'form': form})

@login_required
def modifica_competenza(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    competenza = get_object_or_404(Competenza, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        form = CompetenzaForm(request.POST, instance=competenza)
        
        if form. is_valid():
            form.save()
            
            messages.success(request, "Competenza modificata con successo!")
            return redirect('area_riservata')
    else:
        form = CompetenzaForm(instance=competenza)
    
    return render(request, 'main/curriculum/competenza_form.html', {
        'form': form,
        'modifica':  True,
    })

@login_required
def elimina_competenza(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    competenza = get_object_or_404(Competenza, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':
        nome_competenza = competenza.competenza
        competenza.delete()
        
        messages.success(request, f"Competenza '{nome_competenza}' eliminata con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/competenza_conferma_elimina.html', {
        'competenza': competenza,
    })



@login_required
def aggiungi_lingua(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST':
        form = LinguaForm(request.POST)
        
        if form.is_valid():
            lingua = form.save(commit=False)
            lingua.candidato = dati_personali
            lingua.save()
            
            messages.success(request, "Lingua aggiunta con successo!")
            return redirect('area_riservata')
    else:
        form = LinguaForm()
    
    return render(request, 'main/curriculum/lingua_form.html', {'form': form})

@login_required
def modifica_lingua(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    lingua = get_object_or_404(Lingua, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        form = LinguaForm(request.POST, instance=lingua)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Lingua modificata con successo!")
            return redirect('area_riservata')
    else:
        form = LinguaForm(instance=lingua)
    
    return render(request, 'main/curriculum/lingua_form.html', {
        'form': form,
        'modifica': True,
    })

@login_required
def elimina_lingua(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    lingua = get_object_or_404(Lingua, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST': 
        nome_lingua = lingua.lingua
        lingua.delete()
        
        messages.success(request, f"Lingua '{nome_lingua}' eliminata con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/lingua_conferma_elimina.html', {
        'lingua': lingua,
    })



@login_required
def aggiungi_istruzione(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST':
        form = IstruzioneForm(request.POST)
        
        if form.is_valid():
            istruzione = form.save(commit=False)
            istruzione.candidato = dati_personali
            istruzione.save()
            
            messages.success(request, "Istruzione aggiunta con successo!")
            return redirect('area_riservata')
    else:
        form = IstruzioneForm()
    
    return render(request, 'main/curriculum/istruzione_form.html', {'form': form})

@login_required
def modifica_istruzione(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    istruzione = get_object_or_404(Istruzione, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':
        form = IstruzioneForm(request.POST, instance=istruzione)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Istruzione modificata con successo!")
            return redirect('area_riservata')
    else:
        form = IstruzioneForm(instance=istruzione)
    
    return render(request, 'main/curriculum/istruzione_form.html', {
        'form': form,
        'modifica': True,
    })

@login_required
def elimina_istruzione(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    istruzione = get_object_or_404(Istruzione, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':
        titolo = istruzione.titolo_conseguito
        istituzione = istruzione.istituzione
        istruzione.delete()
        
        messages.success(request, f"Istruzione '{titolo}' presso {istituzione} eliminata con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/istruzione_conferma_elimina.html', {
        'istruzione':  istruzione,
    })



@login_required
def aggiungi_certificazione(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST':
        form = CertificazioneForm(request. POST)
        
        if form.is_valid():
            certificazione = form.save(commit=False)
            certificazione.candidato = dati_personali
            certificazione.save()
            
            messages.success(request, "Certificazione aggiunta con successo!")
            return redirect('area_riservata')
    else:
        form = CertificazioneForm()
    
    return render(request, 'main/curriculum/certificazione_form.html', {'form': form})

@login_required
def modifica_certificazione(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    certificazione = get_object_or_404(Certificazione, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        form = CertificazioneForm(request.POST, instance=certificazione)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Certificazione modificata con successo!")
            return redirect('area_riservata')
    else:
        form = CertificazioneForm(instance=certificazione)
    
    return render(request, 'main/curriculum/certificazione_form.html', {
        'form': form,
        'modifica':  True,
    })

@login_required
def elimina_certificazione(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    certificazione = get_object_or_404(Certificazione, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':
        nome = certificazione.nome
        certificazione.delete()
        
        messages.success(request, f"Certificazione '{nome}' eliminata con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/certificazione_conferma_elimina.html', {
        'certificazione': certificazione,
    })



@login_required
def aggiungi_progetto(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST': 
        form = ProgettoForm(request.POST)
        
        if form.is_valid():
            progetto = form.save(commit=False)
            progetto.candidato = dati_personali
            progetto.save()
            
            messages.success(request, "Progetto aggiunto con successo!")
            return redirect('area_riservata')
    else:
        form = ProgettoForm()
    
    return render(request, 'main/curriculum/progetto_form.html', {'form': form})

@login_required
def modifica_progetto(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    progetto = get_object_or_404(Progetto, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        form = ProgettoForm(request.POST, instance=progetto)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Progetto modificato con successo!")
            return redirect('area_riservata')
    else:
        form = ProgettoForm(instance=progetto)
    
    return render(request, 'main/curriculum/progetto_form.html', {
        'form': form,
        'modifica':  True,
    })

@login_required
def elimina_progetto(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    progetto = get_object_or_404(Progetto, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':
        titolo = progetto.titolo
        progetto.delete()
        
        messages.success(request, f"Progetto '{titolo}' eliminato con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/progetto_conferma_elimina.html', {
        'progetto': progetto,
    })



@login_required
def aggiungi_referenza(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST': 
        form = ReferenzaForm(request.POST)
        
        if form.is_valid():
            referenza = form.save(commit=False)
            referenza.candidato = dati_personali
            referenza.save()
            
            messages.success(request, "Referenza aggiunta con successo!")
            return redirect('area_riservata')
    else:
        form = ReferenzaForm()
    
    return render(request, 'main/curriculum/referenza_form.html', {'form': form})

@login_required
def modifica_referenza(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    referenza = get_object_or_404(Referenza, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        form = ReferenzaForm(request.POST, instance=referenza)
        
        if form. is_valid():
            form.save()
            
            messages.success(request, "Referenza modificata con successo!")
            return redirect('area_riservata')
    else:
        form = ReferenzaForm(instance=referenza)
    
    return render(request, 'main/curriculum/referenza_form.html', {
        'form': form,
        'modifica':  True,
    })

@login_required
def elimina_referenza(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    referenza = get_object_or_404(Referenza, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST':
        nome = referenza.nome
        referenza.delete()
        
        messages.success(request, f"Referenza di '{nome}' eliminata con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/referenza_conferma_elimina.html', {
        'referenza': referenza,
    })



@login_required
def aggiungi_extrainfo(request):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    if request.method == 'POST':
        form = ExtraInfoForm(request.POST)
        
        if form.is_valid():
            extrainfo = form.save(commit=False)
            extrainfo.candidato = dati_personali
            extrainfo.save()
            
            messages.success(request, "Informazione aggiuntiva aggiunta con successo!")
            return redirect('area_riservata')
    else:
        form = ExtraInfoForm()
    
    return render(request, 'main/curriculum/extrainfo_form.html', {'form': form})

@login_required
def modifica_extrainfo(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    extrainfo = get_object_or_404(ExtraInfo, pk=pk, candidato=dati_personali)
    
    if request. method == 'POST':
        form = ExtraInfoForm(request.POST, instance=extrainfo)
        
        if form.is_valid():
            form.save()
            
            messages.success(request, "Informazione aggiuntiva modificata con successo!")
            return redirect('area_riservata')
    else:
        form = ExtraInfoForm(instance=extrainfo)
    
    return render(request, 'main/curriculum/extrainfo_form.html', {
        'form': form,
        'modifica': True,
    })

@login_required
def elimina_extrainfo(request, pk):
    try:
        dati_personali = DatiPersonali.objects.get(user=request.user)
    except DatiPersonali.DoesNotExist:
        messages.error(request, "Devi completare prima i tuoi dati personali.")
        return redirect('area_riservata')
    
    extrainfo = get_object_or_404(ExtraInfo, pk=pk, candidato=dati_personali)
    
    if request.method == 'POST': 
        tipo = extrainfo.tipo_informazione
        extrainfo.delete()
        
        messages.success(request, f"Informazione '{tipo}' eliminata con successo!")
        return redirect('area_riservata')
    
    return render(request, 'main/curriculum/extrainfo_conferma_elimina.html', {
        'extrainfo': extrainfo,
    })