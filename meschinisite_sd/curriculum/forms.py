from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import (
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

class RegistrazioneStudenteForm(UserCreationForm):
    nome = forms.CharField(max_length=255)
    cognome = forms.CharField(max_length=255)
    data_nascita = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    indirizzo = forms.CharField(max_length=255)
    telefono = forms.CharField(max_length=15)
    sito_web = forms.URLField(required=False)
    foto = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class EsperienzaLavorativaForm(forms.ModelForm):
    class Meta:
        model = EsperienzaLavorativa
        fields = ['titolo', 'azienda', 'data_inizio', 'data_fine', 'descrizione']
        widgets = {
            'data_inizio': forms.DateInput(attrs={'type': 'date'}),
            'data_fine': forms.DateInput(attrs={'type': 'date'}),
            'descrizione': forms.Textarea(attrs={'rows': 4}),
        }
        labels = {
            'titolo': 'Posizione/Ruolo',
            'azienda': 'Nome Azienda',
            'data_inizio': 'Data Inizio',
            'data_fine': 'Data Fine (lascia vuoto se ancora in corso)',
            'descrizione': 'Descrizione del ruolo',
        }

class CompetenzaForm(forms. ModelForm):
    """
    Form per gestire le competenze tecniche/professionali dell'utente
    Campi: competenza, livello, certificazioni (opzionale)
    """
    class Meta:
        model = Competenza
        fields = ['competenza', 'livello', 'certificazioni']
        
        widgets = {
            'certificazioni': forms.Textarea(attrs={'rows':  3}),
        }
        
        labels = {
            'competenza': 'Nome Competenza',
            'livello': 'Livello di competenza',
            'certificazioni':  'Certificazioni correlate (opzionale)',
        }
        
        help_texts = {
            'competenza':  'Es:  Python, Project Management, Adobe Photoshop',
            'livello': 'Es: Base, Intermedio, Avanzato, Esperto',
            'certificazioni':  'Elenca eventuali certificazioni che attestano questa competenza',
        }

class LinguaForm(forms.ModelForm):
    class Meta:
        model = Lingua
        fields = ['lingua', 'livello']
        labels = {
            'lingua': 'Nome Lingua',
            'livello': 'Livello di conoscenza',
        }
        help_texts = {
            'lingua': 'Es: Italiano, Inglese, Spagnolo, Francese',
            'livello': 'Es: Madrelingua, C2, C1, B2, B1, A2, A1',
        }

class IstruzioneForm(forms.ModelForm):
    class Meta:
        model = Istruzione
        fields = ['istituzione', 'corso_di_studi', 'titolo_conseguito', 'data_inizio', 'data_fine', 'voto_finale']
        widgets = {
            'data_inizio': forms.DateInput(attrs={'type': 'date'}),
            'data_fine': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'istituzione': 'Nome Istituzione',
            'corso_di_studi': 'Corso di Studi',
            'titolo_conseguito': 'Titolo Conseguito',
            'data_inizio': 'Data Inizio',
            'data_fine': 'Data Fine',
            'voto_finale':  'Voto Finale (opzionale)',
        }
        help_texts = {
            'istituzione': 'Es: Università di Bologna, Liceo Scientifico Fermi',
            'corso_di_studi': 'Es:  Informatica, Ingegneria, Scienze',
            'titolo_conseguito': 'Es: Laurea Triennale, Diploma, Master',
            'voto_finale': 'Es:  110/110, 100/100, 95/100',
        }

class CertificazioneForm(forms.ModelForm):
    class Meta:
        model = Certificazione
        fields = ['nome', 'ente_rilasciante', 'data_conseguimento']  # ← Nomi corretti
        widgets = {
            'data_conseguimento':  forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'nome':  'Nome Certificazione',
            'ente_rilasciante': 'Ente Rilasciante',
            'data_conseguimento':  'Data Conseguimento',
        }
        help_texts = {
            'nome': 'Es: AWS Certified Solutions Architect, PMP, IELTS',
            'ente_rilasciante': 'Es: Amazon Web Services, PMI, Cambridge',
        }

class ProgettoForm(forms.ModelForm):
    class Meta:
        model = Progetto
        fields = ['titolo', 'descrizione', 'link', 'data_completamento']
        widgets = {
            'data_completamento': forms.DateInput(attrs={'type':  'date'}),
        }
        labels = {
            'titolo': 'Titolo Progetto',
            'descrizione': 'Descrizione',
            'link': 'Link al progetto (opzionale)',
            'data_completamento': 'Data Completamento',
        }
        help_texts = {
            'titolo': 'Es: E-commerce in Django, App Mobile per fitness',
            'descrizione': 'Descrivi il progetto, tecnologie usate, obiettivi raggiunti',
            'link':  'Es: https://github.com/username/progetto oppure https://miosito.com',
        }

class ReferenzaForm(forms.ModelForm):
    class Meta:
        model = Referenza
        fields = ['nome', 'posizione', 'azienda', 'contatto']
        labels = {
            'nome': 'Nome Referente',
            'posizione': 'Posizione/Ruolo',
            'azienda': 'Azienda',
            'contatto': 'Contatto (email o telefono)',
        }
        help_texts = {
            'nome': 'Es: Mario Rossi',
            'posizione': 'Es: Senior Developer, Project Manager',
            'azienda': 'Es: TechCorp S.p.A.',
            'contatto': 'Es: mario.rossi@example.com o +39 123 456 7890',
        }

class ExtraInfoForm(forms. ModelForm):
    class Meta:
        model = ExtraInfo
        fields = ['tipo_informazione', 'descrizione']
        labels = {
            'tipo_informazione': 'Tipo di Informazione',
            'descrizione': 'Descrizione',
        }
        help_texts = {
            'tipo_informazione': 'Es: Hobby, Volontariato, Pubblicazioni, Premi, Patente',
            'descrizione': 'Descrivi i dettagli di questa informazione aggiuntiva',
        }