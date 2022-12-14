from django.forms import inlineformset_factory
from .models import *
homeInlineFormSet = inlineformset_factory(town, home,fields= ['image', 'title', 'description'], extra =3 ) 