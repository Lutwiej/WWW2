from django.contrib import admin

from .models import Question, Answer

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['pub_date','question_text']
    list_filter = ('pub_date','question_text')
    search_fields = ('pub_date','question_text')

    def get_question(self, obj):
        return obj.question.question_text



    def get_question(self,obj):
        return obj.question.question_text

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer_text','get_question']
    list_filter = ['question','answer_text']
    search_fields = ['question','answer_text']

    def get_question(self,obj):
        return obj.question.question_text

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer,AnswerAdmin)