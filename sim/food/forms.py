from django.forms import inlineformset_factory
from .models import *
foodInlineFormSet = inlineformset_factory(zip, food,fields= ['image', 'title', 'description'], extra =3 ) 