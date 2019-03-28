from django.db import models



class Intent(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    context = models.ForeignKey('Context', on_delete=models.CASCADE, verbose_name='Контекст')

    def __str__(self): return self.name

    class Meta:
        verbose_name = 'Намерение'
        verbose_name_plural = 'Намерения'


class Context(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')

    def __str__(self): return self.name

    class Meta:
        verbose_name_plural = 'Контексты'
        verbose_name = 'Контекст'


class TrainExample(models.Model):
    intent = models.ForeignKey(Intent, on_delete=models.CASCADE, verbose_name='Намерение')
    example = models.TextField(verbose_name='Тренеровочный пример')

    def __str__(self): return self.example

    class Meta:
        verbose_name = 'Тренеровочный пример'
        verbose_name_plural = 'Тренеровочные примеры'