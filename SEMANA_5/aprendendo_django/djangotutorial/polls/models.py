from django.db import models
import datetime
from django.utils import timezone
# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200) # models.charField é um campo de texto com tamanho limitado a 200 caracteres
    pub_date = models.DateTimeField('data de publicação') # models.DateTimeField é um campo de data e hora, com o parâmetro 'data de publicação' como descrição do campo
    def __str__(self):
        return self.question_text # retorna o texto da pergunta como representação do objeto Question
    def foi_publicada_recentemente(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1) # retorna True se a pergunta foi publicada recentemente, ou seja, se a data de publicação é maior ou igual a 1 dia atrás
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0) # models.IntegerField é um campo de número inteiro, com o parâmetro default=0 como valor padrão do campo
    
    def __str__(self):
        return self.choice_text # retorna o texto da escolha como representação do objeto Choice