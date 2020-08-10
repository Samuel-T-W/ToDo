from django.forms import ModelForm, TextInput
from .models import Todo 

class TodoForm(ModelForm):
    class Meta:
        model = Todo 
        fields = ['todo_text']
        widgets = {'name' : TextInput(attrs={'class' : 'input', 'placeholder' : 'Todo activity'})}

       