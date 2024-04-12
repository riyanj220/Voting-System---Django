from django.contrib import admin
from .models import *

admin.site.site_header = 'The Poll Mall'
admin.site.site_title = 'Voting admin area'
admin.site.index_title = 'Welcome to our voting admin area'

class ChoiceInLine(admin.TabularInline):
    model = Choice 
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}),
                 ('Date Information', {'fields':['publishing_date'] ,'classes':['collapse']}),
                 ]
    
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)
