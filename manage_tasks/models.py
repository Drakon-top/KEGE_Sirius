from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=50, verbose_name="Название")
    content = models.TextField(max_length=1500, verbose_name="Описание")
    task_1 = models.CharField(max_length=10, verbose_name="1")
    task_2 = models.CharField(max_length=10, verbose_name="2")
    task_3 = models.CharField(max_length=10, verbose_name="3")
    task_4 = models.CharField(max_length=10, verbose_name="4")
    task_5 = models.CharField(max_length=10, verbose_name="5")
    task_6 = models.CharField(max_length=10, verbose_name="6")
    task_7 = models.CharField(max_length=10, verbose_name="7")
    task_8 = models.CharField(max_length=10, verbose_name="8")
    task_9 = models.CharField(max_length=10, verbose_name="9")
    task_10 = models.CharField(max_length=10, verbose_name="10")
    task_11 = models.CharField(max_length=10, verbose_name="11")
    task_12 = models.CharField(max_length=10, verbose_name="12")
    task_13 = models.CharField(max_length=10, verbose_name="13")
    task_14 = models.CharField(max_length=10, verbose_name="14")
    task_15 = models.CharField(max_length=10, verbose_name="15")
    task_16 = models.CharField(max_length=10, verbose_name="16")
    task_17 = models.CharField(max_length=10, verbose_name="17")
    task_18 = models.CharField(max_length=10, verbose_name="18")
    task_19 = models.CharField(max_length=10, verbose_name="19")
    task_20 = models.CharField(max_length=10, verbose_name="20")
    task_21 = models.CharField(max_length=10, verbose_name="21")
    task_22 = models.CharField(max_length=10, verbose_name="22")
    task_23 = models.CharField(max_length=10, verbose_name="23")
    task_24 = models.CharField(max_length=10, verbose_name="24")
    task_25 = models.CharField(max_length=10, verbose_name="25")
    task_26 = models.CharField(max_length=10, verbose_name="26")
    task_27 = models.CharField(max_length=10, verbose_name="27")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


class Answers(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Ученик")
    task = models.ForeignKey(Task, on_delete=models.CASCADE, verbose_name='Задание')
    answer_1 = models.CharField(max_length=10, verbose_name="1")
    answer_2 = models.CharField(max_length=10, verbose_name="2")
    answer_3 = models.CharField(max_length=10, verbose_name="3")
    answer_4 = models.CharField(max_length=10, verbose_name="4")
    answer_5 = models.CharField(max_length=10, verbose_name="5")
    answer_6 = models.CharField(max_length=10, verbose_name="6")
    answer_7 = models.CharField(max_length=10, verbose_name="7")
    answer_8 = models.CharField(max_length=10, verbose_name="8")
    answer_9 = models.CharField(max_length=10, verbose_name="9")
    answer_10 = models.CharField(max_length=10, verbose_name="10")
    answer_11 = models.CharField(max_length=10, verbose_name="11")
    answer_12 = models.CharField(max_length=10, verbose_name="12")
    answer_13 = models.CharField(max_length=10, verbose_name="13")
    answer_14 = models.CharField(max_length=10, verbose_name="14")
    answer_15 = models.CharField(max_length=10, verbose_name="15")
    answer_16 = models.CharField(max_length=10, verbose_name="16")
    answer_17 = models.CharField(max_length=10, verbose_name="17")
    answer_18 = models.CharField(max_length=10, verbose_name="18")
    answer_19 = models.CharField(max_length=10, verbose_name="19")
    answer_20 = models.CharField(max_length=10, verbose_name="20")
    answer_21 = models.CharField(max_length=10, verbose_name="21")
    answer_22 = models.CharField(max_length=10, verbose_name="22")
    answer_23 = models.CharField(max_length=10, verbose_name="23")
    answer_24 = models.CharField(max_length=10, verbose_name="24")
    answer_25 = models.CharField(max_length=10, verbose_name="25")
    answer_26 = models.CharField(max_length=10, verbose_name="26")
    answer_27 = models.CharField(max_length=10, verbose_name="27")

    def get_task(self):
        return self.task

    def __str__(self):
        return str(self.author) + ' ' + str(self.task)

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'