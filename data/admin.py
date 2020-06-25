from django.contrib import admin

# Register your models here.
from .models import todolist

class todolistadminmodel(admin.ModelAdmin):

	list_display = ('baslik','eklenme_tarihi','durum')
	date_hierarchy = ('eklenme_tarihi')
	#list_display_links = ('baslik','eklenme_tarihi')
	list_filter = ('eklenme_tarihi','durum')
	list_editable = ['durum']
	orering = ['eklenme_tarihi']
	search_fields = ('baslik','aciklama')
	exclude = ['eklenme_tarihi']

	class meta:
		model = todolist

admin.site.register(todolist, todolistadminmodel)