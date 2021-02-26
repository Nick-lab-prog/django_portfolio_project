from django.db import models

# Create your models here.
#qui ci sono le classi che trattengono le qualità dei vari
#oggetti che vengono creati all'interno dell'applicazione 

#i models sono le classi che lavorano con il database
class Project(models.Model):
	title = models.CharField(max_length=100)
	description = models.CharField(max_length=250)
	image = models.ImageField(upload_to='portoflio/images/')#percorso da seguire
	url = models.URLField(blank=True)

