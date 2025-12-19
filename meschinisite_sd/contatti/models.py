from django.db import models


class InformazioniBase(models.Model):
    email = models.CharField(max_length= 50)
    telefono = models.CharField(max_length= 20)
    indirizzo = models.CharField(max_length= 150)
    
class Social(models.Model):
    nome = models.CharField(max_length= 50)
    url = models.URLField()
    img_social = models.ImageField()
    
    
# ImageField
# Charfield
# TextField
# UrlField
# DateTimeField