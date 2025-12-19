from django.contrib import admin
from main.models import *
from footer.models import *
from contatti.models import *
from aziende.models import *
from curriculum.models import *


#######################################AZIENDE
admin.site.register(Azienda)
admin.site.register(Annuncio)
admin.site.register(Candidatura)
#######################################CURRICULUM
admin.site.register(DatiPersonali)
admin.site.register(EsperienzaLavorativa)
admin.site.register(Lingua)
admin.site.register(Istruzione)
admin.site.register(Competenza)
admin.site.register(Certificazione)
admin.site.register(Progetto)
admin.site.register(Referenza)
admin.site.register(ExtraInfo)
#######################################FOOTER
admin.site.register(Footer_info)

#######################################CONTATTI
admin.site.register(InformazioniBase)
admin.site.register(Social)


