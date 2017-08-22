from django.db import models


# Create your models here.
class Evento(models.Model):
    titulo_text = models.CharField('Titulo', max_length=200)
    date_date = models.DateTimeField('Data do Evento')
    local_text = models.CharField('Local', max_length=200)
    description_text = models.CharField('Descricao', max_length=500)
    image_src_text = models.CharField('Caminho da imagem', max_length=100,
                                      blank=True)

    def __str__(self):
        return self.titulo_text


class DonateItem(models.Model):
    name_text = models.CharField('Nome', max_length=100)
    image_src_text = models.CharField('Caminho da imagem', max_length=100,
                                      blank=True)
    amount = models.IntegerField('Quantidade', default=1)

    def __str__(self):
        return self.name_text
