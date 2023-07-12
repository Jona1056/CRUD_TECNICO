from django.forms import ModelForm 
from .models import Usuarios
class UseForm(ModelForm):
    class Meta:
        model = Usuarios
        fields = ['nombre', 'apellido', 'fecha_de_nacimiento','Genero','direccion','estado_civil','dpi']