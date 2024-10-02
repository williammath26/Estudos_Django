from django.db import models

# Create your models here.
class Topic(models.Model):
    """um assunto sobre o qual o usuário está aprendendo"""
    text =  models.CharField(max_length=200)
    data_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve uma representação em string do modelo."""
        return self.text