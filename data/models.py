from django.db import models
from django.utils import timezone


# Create your models here.
 
class todolist(models.Model):
	
	baslik = models.CharField(max_length=144,verbose_name='başlık')
	aciklama = models.TextField(blank=True,null=True,verbose_name='açıklama')
	eklenme_tarihi = models.DateTimeField(default=timezone.now,verbose_name='eklenme_tarihi')
	durum = models.BooleanField(default=False,verbose_name='yapıldı')

	class Meta:
		verbose_name = 'Yapılacaklar'
		verbose_name_plural = 'Yapılacaklar'

	def __str__(self):
		return self.baslik
