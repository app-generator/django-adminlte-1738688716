# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    nom = models.TextField(max_length=255, null=True, blank=True)
    prénom = models.TextField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Entete_Document(models.Model):

    #__Entete_Document_FIELDS__
    rédacteur = models.TextField(max_length=255, null=True, blank=True)
    vérificateur = models.TextField(max_length=255, null=True, blank=True)
    date de maj = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Entete_Document_FIELDS__END

    class Meta:
        verbose_name        = _("Entete_Document")
        verbose_name_plural = _("Entete_Document")


class Entete_Projet(models.Model):

    #__Entete_Projet_FIELDS__
    id projet = models.IntegerField(null=True, blank=True)
    nom projet = models.TextField(max_length=255, null=True, blank=True)

    #__Entete_Projet_FIELDS__END

    class Meta:
        verbose_name        = _("Entete_Projet")
        verbose_name_plural = _("Entete_Projet")


class Entete_Plateform(models.Model):

    #__Entete_Plateform_FIELDS__
    code plateforme = models.CharField(max_length=255, null=True, blank=True)
    hébergement = models.TextField(max_length=255, null=True, blank=True)

    #__Entete_Plateform_FIELDS__END

    class Meta:
        verbose_name        = _("Entete_Plateform")
        verbose_name_plural = _("Entete_Plateform")


class Param_Domains(models.Model):

    #__Param_Domains_FIELDS__
    domaine = models.TextField(max_length=255, null=True, blank=True)

    #__Param_Domains_FIELDS__END

    class Meta:
        verbose_name        = _("Param_Domains")
        verbose_name_plural = _("Param_Domains")


class Param_Hebergement(models.Model):

    #__Param_Hebergement_FIELDS__
    hebergement = models.TextField(max_length=255, null=True, blank=True)

    #__Param_Hebergement_FIELDS__END

    class Meta:
        verbose_name        = _("Param_Hebergement")
        verbose_name_plural = _("Param_Hebergement")



#__MODELS__END
