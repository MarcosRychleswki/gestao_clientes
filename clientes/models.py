from django.db import models
from django.core.mail import send_mail, mail_admins

class Person(models.Model):
    objects = None
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    bio = models.TextField()
    photo = models.ImageField(upload_to='clients_photos', null=True, blank=True)


    class Meta:
        permissions = (
            ('deletar_clientes', 'Deletar_clientes'),
        )


    @property
    def nome_completo(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super(Person, self).save(*args, **kwargs)

        send_mail(
            'Novo cliente cadastrado',
            'o cliente %s foi cadastrado' % self.first_name,
            'vinirychlewski@gmail.com',
            ['vinirychlewski@gmail.com'],
            fail_silently=False,
        )

        mail_admins(
            'Novo cliente cadastrado',
            'o cliente %s foi cadastrado' % self.first_name,
            fail_silently=False,
        )


    def __str__(self):
        return self.first_name + ' ' + self.last_name





