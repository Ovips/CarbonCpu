from django.db import models


class Cpu(models.Model):
    load = models.FloatField('Загрузка CPU')
    date = models.DateTimeField('Дата добавления', auto_now_add=True, db_index=True)

    def __str__(self):
        date = self.date.strftime('%Y-%m-%d %H:%M:%S')
        return f'{date} нагрузка была {self.load} id = {self.id}'
