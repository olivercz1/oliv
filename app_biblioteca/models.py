from django.db import models

# Create your models here.
class Livro(models.Model):
    Nome_do_Livro = models.CharField(max_length=200)
    Departamento = models.CharField(max_length=200)
    Autor = models.CharField(max_length=200)
    Quantidade_páginas =models.PositiveSmallIntegerField()
    idioma =models.CharField(max_length=200)


    def __str__(self):
      return self.Nome_do_Livro