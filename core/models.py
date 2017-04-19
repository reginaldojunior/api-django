# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    department = models.CharField(max_length=100)

    class Meta:
        verbose_name = "employee"
        verbose_name_plural = "employees"

    def __unicode__(self):
        return self.name
