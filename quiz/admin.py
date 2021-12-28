from django.contrib import admin
from .models import *


class AnswerInline(admin.TabularInline):
    model = Answer


class QuestionInline(admin.TabularInline):
    model = Question

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    
    
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(TelegramUser)
admin.site.register(UserResult)
admin.site.register(QuizTypes)
admin.site.register(Subscription)
admin.site.register(ReadingTopics)
admin.site.register(ListeningTest)





