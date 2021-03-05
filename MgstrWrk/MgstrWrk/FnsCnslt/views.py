from django.shortcuts import render
from django.shortcuts import redirect
from FnsCnslt.LoadNeiron import NrFnRes, mean1, std1
from .models import FinForm
import numpy as np
import tensorflow as tf
import os.path, time
global graph

graph = tf.compat.v1.get_default_graph()

# Create your views here.

def FinConsul (request): # Обработка формы ввода
    global Result
    if request.POST:
        form=FinForm(request.POST)
        if form.is_valid():
  
            VVP_all = form.cleaned_data.get("VVP_all")
            VVP_one = form.cleaned_data.get("VVP_one")
            Fonds_in_economics = form.cleaned_data.get("Fonds_in_economics")
            Rozn_torg = form.cleaned_data.get("Rozn_torg")
            Konsolid_money = form.cleaned_data.get("Konsolid_money")
            Saldir_result = form.cleaned_data.get("Saldir_result")
            Rezerv = form.cleaned_data.get("Rezerv")
            Invest = form.cleaned_data.get("Invest")
            Eksport = form.cleaned_data.get("Eksport")
            Import2 = form.cleaned_data.get("Import2")
            Matrix1 = np.array([VVP_all, VVP_one, Fonds_in_economics, Rozn_torg, 
                                Konsolid_money, Saldir_result, Rezerv, Invest, Eksport, Import2])
            Matrix1 = Matrix1.reshape(1,10)
            Matrix1 = (Matrix1 - mean1)/std1

            with graph.as_default():
                WrkNrn = np.array([NrFnRes.predict_on_batch(Matrix1)])
                WrkNrn = WrkNrn.reshape(2,10)
                WrkNrn = (WrkNrn * std1) + mean1
            Result = WrkNrn
            return redirect('finresult/')

    else:
        form=FinForm()
    return render(request, 'FnsCnslt/finform.html', {'form':form})


def ResultNeiron (request): # Отоброжение результата обработки
    filePath = 'FnsCnslt/static/img/model.png'
    time_model = time.ctime(os.path.getmtime(filePath))
    return render(request, 'FnsCnslt/finresult.html', 
                  {'Result':Result, 'TimeModel':time_model})