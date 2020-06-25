from django.contrib import admin

# Register your models here.
from .models import todolist

class todolistadminmodel(admin.ModelAdmin):

	list_display = ('başlık','eklenme_tarihi','durum')
	date_hierarchy = ('eklenme_tarihi')
	#list_display_links = ('başlık','eklenme_tarihi')
	list_filter = ('eklenme_tarihi','durum')
	list_editable = ['durum']
	orering = ['eklenme_tarihi']
	search_fields = ('başlık','açıklama')
	exclude = ['eklenme_tarihi']

	class meta:
		model = todolist

admin.site.register(todolist, todolistadminmodel)