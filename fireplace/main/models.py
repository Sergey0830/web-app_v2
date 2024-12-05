from django.db import models

class Question(models.Model):
    name = models.CharField(max_length=100, verbose_name="Ім'я")
    contact_method = models.CharField(
        max_length=10,
        choices=[('email', 'Email'), ('phone', 'Телефон')],
        verbose_name="Метод контакту"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="Email")
    phone = models.CharField(max_length=15, blank=True, null=True, verbose_name="Телефон")
    question = models.TextField(verbose_name="Запитання")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")

    def __str__(self):
        return f"{self.name} - {self.contact_method}"