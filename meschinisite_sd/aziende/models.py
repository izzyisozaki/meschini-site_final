from django.db import models

class Azienda(models.Model):
    nome = models.CharField(max_length=255)
    indirizzo = models.CharField(max_length=255)
    logo = models.ImageField(null=True)
    partita_iva = models.CharField(max_length=20)
    email = models.EmailField(max_length=254)
    telefono = models.CharField(max_length=15)
    descrizione = models.TextField()
    sito_web = models.URLField(max_length=200)
    
    def _str_(self):  #  SOLO QUESTA RIGA IN PIÙ
        return self.nome

class Annuncio(models.Model):
    azienda = models.ForeignKey(Azienda, on_delete=models.CASCADE)  #  CORRETTO
    titolo = models.CharField(max_length=255)
    descrizione = models.TextField()
    requisiti = models.TextField()
    stipendio = models.CharField(max_length=50)
    localita = models.CharField(max_length=255)
    tipo_contratto = models.CharField(max_length=100)
    data_pubblicazione = models.DateField(auto_now_add=True)
    data_scadenza = models.DateField()
    
    def _str_(self):  # SOLO QUESTA RIGA IN PIÙ
        return self.titolo

class Candidatura(models.Model):
    annuncio = models.ForeignKey(Annuncio, on_delete=models.CASCADE)  #  CORRETTO
    utente_id = models.IntegerField()  # MEGLIO DI TextField
    data_candidatura = models.DateTimeField(auto_now_add=True)
    stato = models.TextField()
    messaggio = models.TextField()
    
   
    def _str_(self):  # SOLO QUESTA RIGA IN PIÙ
        return f"Candidatura per {self.annuncio.titolo} da utente {self.utente_id}"      


