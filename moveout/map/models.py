from django.db import models

# Create your models here.
class Regiune(models.Model):
    nume=models.CharField(max_length = 20, default="Nevalidat")

class Point(models.Model):
    INTERES="I"
    REGIUNE="R"
    ALEGERE_DET = [
    (INTERES, 'Interes'),
    (REGIUNE, 'Regiune'),
    ]
    x = models.IntegerField(default=0)
    y = models.IntegerField(default=0)
    det = models.CharField(choices = ALEGERE_DET, max_length = 20,
    default="N/A")
    regiune = models.ForeignKey(Regiune, on_delete=models.CASCADE)
