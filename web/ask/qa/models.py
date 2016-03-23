#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)    #заголовок вопроса
    text = models.TextField(null=False)                     #полный текст вопроса
    added_at = models.DateTimeField(auto_now_add=True, blank=True)  #дата добавления вопроса
    rating = models.IntegerField(default=0)     #рейтинг вопроса (число)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name='question_author_set')   #автор вопроса
    likes = models.ManyToManyField(User, related_name='question_like_set')        #список пользователей, поставивших "лайк"


class Answer(models.Model):
    text = models.TextField(null=False) #текст ответа
    added_at = models.DateTimeField(auto_now_add=True, blank=True)#дата добавления ответа
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)#вопрос, к которому относится ответ
    author = models.ForeignKey(User, on_delete=models.CASCADE)      #автор ответа
