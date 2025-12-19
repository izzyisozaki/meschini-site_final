from django.db import models
from django.contrib.auth.models import User

class DatiPersonali(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nome = models.CharField(max_length=255)
    cognome = models.CharField(max_length=255)
    data_nascita = models.DateField()
    indirizzo = models.CharField(max_length=255)
    telefono = models.CharField(max_length=15)
    email = models.EmailField(max_length=254)
    sito_web = models.URLField(max_length=200, null=True, blank=True)
    foto = models.ImageField(upload_to="foto_profili/", null=True, blank=True)

    def __str__(self):
        return f"{self.nome} {self.cognome}"

class EsperienzaLavorativa(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=255)
    azienda = models.CharField(max_length=255)
    data_inizio = models.DateField()
    data_fine = models.DateField(null=True, blank=True)
    descrizione = models.TextField()

class Lingua(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    lingua = models.CharField(max_length=100)
    livello = models.CharField(max_length=50)

class Istruzione(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    istituzione = models.CharField(max_length=255)
    corso_di_studi = models.CharField(max_length=255)
    titolo_conseguito = models.CharField(max_length=255)
    data_inizio = models.DateField()
    data_fine = models.DateField()
    voto_finale = models.CharField(max_length=50, null=True, blank=True)

class Competenza(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    competenza = models.CharField(max_length=255)
    livello = models.CharField(max_length=50)
    certificazioni = models.TextField(null=True, blank=True)

class Certificazione(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    data_conseguimento = models.DateField()
    ente_rilasciante = models.CharField(max_length=255)

class Progetto(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    titolo = models.CharField(max_length=255)
    descrizione = models.TextField()
    link = models.URLField(null=True, blank=True)
    data_completamento = models.DateField()

class Referenza(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    posizione = models.CharField(max_length=255)
    azienda = models.CharField(max_length=255)
    contatto = models.CharField(max_length=255)

class ExtraInfo(models.Model):
    candidato = models.ForeignKey(DatiPersonali, on_delete=models.CASCADE)
    tipo_informazione = models.CharField(max_length=255)
    descrizione = models.TextField()