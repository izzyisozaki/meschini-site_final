from django.db import models
from contatti.models import *


class Footer_info(models.Model):
     Info = models.ForeignKey(InformazioniBase, on_delete=models.SET_NULL, null=True)
     logo = models.ImageField(null=True)    
    
    
    
    
# ImageField
# Charfield
# TextField
# UrlField
# DateTimeField