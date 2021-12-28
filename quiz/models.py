import os
from django.db import models


class QuizTypes(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'quiz_types'


class Quiz(models.Model):
    name = models.CharField(max_length=120)
    topic = models.CharField(max_length=120)
    level = models.ForeignKey('Subscription', on_delete=models.DO_NOTHING, null=True)
    type = models.ForeignKey(QuizTypes, on_delete=models.DO_NOTHING, default=1, null=True)


    def __str__(self):
        return f"{self.name}-{self.name}"

    def get_questions(self):
        return self.question_set.all()

    class Meta:
        db_table = 'quiz'
        verbose_name_plural = 'Quizes'


class Question(models.Model):
    text = models.CharField(max_length=200)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    weight = models.IntegerField(default=1)

    def __str__(self):
        return str(self.text)

    def get_answers(self):
        return self.answer_set.all()

    class Meta:
        db_table = 'quiz_question'


class Answer(models.Model):
    text = models.CharField(max_length=200)
    correct = models.BooleanField(default=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)

    class Meta:
        db_table = 'quiz_answer'

    def __str__(self):
        return f"question: {self.question.text}, answer: {self.text}, correct: {self.correct}"


class TelegramUser(models.Model):
    user_id = models.IntegerField(primary_key=True, blank=False, null=False)
    nickname = models.CharField(max_length=100, blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    subscriptions = models.ManyToManyField('Subscription')

    class Meta:
        db_table = 'telegram_user'


class UserResult(models.Model):
    quiz = models.ForeignKey(Quiz, models.SET_NULL, blank=True, null=True)
    user = models.ForeignKey(TelegramUser, models.SET_NULL, blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'user_result'


class Subscription(models.Model):
    name = models.CharField(max_length=10)
    price = models.IntegerField()

    def __str__(self):
        return f'{self.name}  {self.price}'

    class Meta:
        db_table = 'subscription'


class ReadingTopics(models.Model):
    name = models.CharField(max_length=50)
    text_url = models.URLField()
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        db_table = 'reading_topics'



class ListeningTest(models.Model):
    name = models.CharField(max_length=50)
    text_url = models.URLField()
    audio_file = models.FileField()
    audio_file_abs_path = models.CharField(max_length=200, blank=True)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING, null=True, blank=True)

    def save(self, *args, **kwargs):
        # super(self.__class__, self).save(*args, **kwargs)
        audio_path = os.path.abspath(self.audio_file.path)
        self.audio_file_abs_path = audio_path
        super(self.__class__, self).save(*args, **kwargs)
