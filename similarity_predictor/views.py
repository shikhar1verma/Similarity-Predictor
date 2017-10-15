from django.shortcuts import render
from .forms import TextForm
import requests
import json
# Create your views here.

def data(request):
    text1=''
    similarity=''
    if request.method == 'POST':
        form = TextForm(request.POST)
        text1 = form.data['text1']
        text2 = form.data['text2']
        params = {'token':'807f0def2bf54ca0acba229cc8da7ec6','text1':text1,'text2':text2}
        response = requests.get('https://api.dandelion.eu/datatxt/sim/v1',params=params)
        response = response.json()
        similarity = response['similarity']*100
    else:
        form = TextForm()

    return render(request,'main.html',{'form':form,'text1':similarity})
