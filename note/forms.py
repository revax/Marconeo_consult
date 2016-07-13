# -*- coding: utf-8 -*-
from django import forms
from captcha.fields import ReCaptchaField
from django.utils.safestring import mark_safe
class NameForm(forms.Form):
    your_name = forms.IntegerField(label="Numéro ", max_value=9999999999, required=True)
    captcha = ReCaptchaField(label=mark_safe('<br />Captcha'), attrs={'lang' : 'fr'})
