# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models

class Andress(models.Model):
    STATE_CHOICES = (
		(u'AC', u'Acre'),
		(u'AL', u'Alagoas'),
		(u'AM', u'Amazonas'),
		(u'AP', u'Amapá'),
		(u'BA', u'Bahia'),
		(u'CE', u'Ceará'),
		(u'DF', u'Distrito Federal'),
		(u'ES', u'Espírito Santo'),
		(u'GO', u'Goiás'),
		(u'MA', u'Maranhão'),
		(u'MT', u'Mato Grosso'),
		(u'MS', u'Mato Grosso do Sul'),
		(u'MG', u'Minas Gerais'),
		(u'PA', u'Pará'),
		(u'PB', u'Paraíba'),
		(u'PR', u'Paraná'),
		(u'PE', u'Pernambuco'),
		(u'PI', u'Piauí'),
		(u'RJ', u'Rio de Janeiro'),
		(u'RN', u'Rio Grande do Norte'),
		(u'RO', u'Rondônia'),
		(u'RS', u'Rio Grande do Sul'),
		(u'RR', u'Roraima'),
		(u'SC', u'Santa Catarina'),
		(u'SE', u'Sergipe'),
		(u'SP', u'São Paulo'),
		(u'TO', u'Tocantins')
    )

    zip_code = models.CharField(max_length=10)
    street = models.CharField(max_length=50)
    number = models.IntegerField()
    neighborhood = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50, choices=STATE_CHOICES)
    complement = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Andress"
        verbose_name_plural = "Andresses"

class Employee(models.Model):
    GENDER_CHOICES = (
        (u'M', u'Masculino'),
        (u'F', u'Feminino'),
    )

    name = models.CharField(max_length=100)
    document = models.CharField(max_length=20)
    birthday = models.DateField()
    phone = models.CharField(max_length=20)
    salary = models.DecimalField(max_digits=20, decimal_places=2)
    gender = models.CharField(max_length=2, choices=GENDER_CHOICES)
    andress = models.ForeignKey(Andress)

    class Meta:
        verbose_name = "Employee"
        verbose_name_plural = "Employees"

    def __unicode__(self):
    	return self.name