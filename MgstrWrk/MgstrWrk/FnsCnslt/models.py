from django.db import models
from django import forms

# Create your models here.

class FinForm(forms.Form):              # Ввод данных для нейронной сети

    VVP_all = forms.FloatField(label='Валовой внутренний продукт, всего, млрд. руб.') # 

    VVP_one = forms.FloatField(label='Валовой внутренний продукт, на душу населения, руб.') 

    Fonds_in_economics = forms.FloatField(label='Основные фонды в экономике (по полной учетной стоимости;  на конец года), млрд. руб') 

    Rozn_torg = forms.FloatField(label='Оборот розничной торговли, млн. руб.')

    Konsolid_money = forms.FloatField(label='Профицит, дефицит консолидированного бюджета, млн. руб') 

    Saldir_result = forms.FloatField(label='Сальдированный финансовый результат (прибыль минус убыток) в экономике, млн. руб')  

    Rezerv = forms.FloatField(label='Международные резервы Российской Федерации (на конец года), млрд. долл. США')  

    Invest = forms.FloatField(label='Инвестиции в основной капитал, млн. руб')

    Eksport = forms.FloatField(label='Экспорт внешнеторгового оборота, млрд. долл. США')

    Import2 = forms.FloatField(label='Импорт внешнеторгового оборота, млрд. долл. США')