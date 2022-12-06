from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=20, verbose_name='ФИО')
    citizenship = models.CharField(max_length=20, default='Кыргызстан', verbose_name='Гражданство')
    birth_year = models.DateField(verbose_name='Год рождения')
    work_place = models.CharField(max_length=30, verbose_name='Место работы', null=True, blank=True)
    update_date = models.DateField(verbose_name='Дата последнего обновления', auto_now=True)

    class Meta:
        db_table = 'customers'

    def __str__(self):
        return self.name


class Account(models.Model):
    number = models.CharField(max_length=16, unique=True, verbose_name='Номер аккаунта')
    account_type = models.IntegerField(default=1)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    class Meta:
        db_table = 'accounts'

    def __str__(self):
        return self.number


class Credit(models.Model):
    sum = models.IntegerField(verbose_name='Сумма кредита')
    date = models.DateField(verbose_name='Дата получения кредита', auto_now_add=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='credits')

    class Meta:
        db_table = 'loans'

