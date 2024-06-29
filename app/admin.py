from django.contrib import admin
from .models import Examen, Sujet, Serie,Profil

class ExamenInline(admin.TabularInline):
    model = Examen
    extra = 1

class SujetAdmin(admin.ModelAdmin):
    inlines = [ExamenInline]
admin.site.register(Examen)
admin.site.register(Sujet, SujetAdmin)
admin.site.register(Serie)
admin.site.register(Profil)