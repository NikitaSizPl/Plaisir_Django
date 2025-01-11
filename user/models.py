from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50,
                            verbose_name='Имя покупателя'
                            )
    instagram = models.CharField(max_length=50,
                                 verbose_name='Instagram покупателя'
                                 )
    phone = models.IntegerField(blank=True,
                                verbose_name='Номер покупателя'
                                )
    adress = models.CharField(max_length=100,
                              blank=True,
                              verbose_name='Адрес покупателя'
                              )
    creat_at = models.DateTimeField(auto_now_add=True,
                                    verbose_name='Дата создания'
                                    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
