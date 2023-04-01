from datetime import datetime as dt

from django.db import models


# ======{ Профиль }======
class Nationality(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Гражданство"
        verbose_name_plural = "Гражданство"

    def __str__(self):
        return self.title


class Gender(models.Model):
    title = models.CharField("Название", max_length=32, unique=True)

    class Meta:
        verbose_name = "Гендер"
        verbose_name_plural = "Гендер"

    def __str__(self):
        return self.title


class Profile(models.Model):
    # user = models.OneToOneField(verbose_name="Пользователь", to=User, on_delete=models.CASCADE)
    nationality = models.ForeignKey(to=Nationality, on_delete=models.SET_NULL, null=True, verbose_name="Гражданство")
    gender = models.ForeignKey(to=Gender, on_delete=models.SET_NULL, null=True, verbose_name="Гендер")
    birth_year = models.IntegerField()

    class Meta:
        verbose_name = "Расширенный пользователь"
        verbose_name_plural = "Расширенные пользователи"

    def __str__(self):
        return f"{self.pk}"


# ======{ Транзакции }======
class TypeTransaction(models.Model):
    title = models.CharField("Название", max_length=64, unique=True)

    class Meta:
        verbose_name = "Тип транзакции"
        verbose_name_plural = "Типы транзакции"

    def __str__(self):
        return self.title


class PaymentMethodTransaction(models.Model):
    title = models.CharField("Название", max_length=64, unique=True)

    class Meta:
        verbose_name = "Способ платежа"
        verbose_name_plural = "Способы платежа"

    def __str__(self):
        return self.title


class CategoryTransaction(models.Model):
    title = models.CharField("Название", max_length=64, unique=True)

    class Meta:
        verbose_name = "Категория платежа"
        verbose_name_plural = "Категории платежа"

    def __str__(self):
        return self.title


class Transactions(models.Model):
    time = models.DateTimeField("Время", default=dt.now)
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, verbose_name="Пользователь")
    type = models.ForeignKey(to=TypeTransaction, on_delete=models.CASCADE, verbose_name="Тип транзакции")
    payment_method = models.ForeignKey(to=PaymentMethodTransaction, on_delete=models.CASCADE,
                                       verbose_name="Способ платежа")
    category = models.ForeignKey(to=CategoryTransaction, on_delete=models.CASCADE, verbose_name="Категория платежа")
    amount = models.FloatField("Сумма платежа", help_text="В рублях")
    client_fee = models.FloatField("Комиссия клиента", default=0)
    payout_fee = models.FloatField("Комиссия за выплату", default=0)
    interchange_fee = models.FloatField("Плата за обмен", default=0)
    pay_system_fee = models.FloatField("Системная комиссия", default=0)
    paying_fee = models.FloatField("Пошлина", default=0)

    class Meta:
        verbose_name = "Транзакция"
        verbose_name_plural = "Транзакции"

    def __str__(self):
        return f"{self.time}"


# ======{ Платежные карты }======
class Card(models.Model):
    profile = models.ForeignKey(to=Profile, on_delete=models.CASCADE, verbose_name="Пользователь")
    registration_date = models.DateTimeField("Дата регистрации", blank=True, null=True, default=None)
    deletion_date = models.DateTimeField("Дата удаления", blank=True, null=True, default=None)

    class Meta:
        verbose_name = "Платежная карта"
        verbose_name_plural = "Платежные карты"

    def __str__(self):
        return f"{self.profile} - {self.pk}"
