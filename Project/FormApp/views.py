from django.shortcuts import render
from FormApp.forms import FormName
from django.http import HttpResponseRedirect
# Create your views here.


def form_view(request):
    form = FormName()

    if request.method == 'POST':
        form = FormName(request.POST)

        if form.is_valid():

            print("\n\n\n")
            print("Validation SUCCESS!!")
            print("Name: "+form.cleaned_data['name'])
            print("Email: "+form.cleaned_data['email'])
            print("Text: "+form.cleaned_data['text'])
            print("URL: "+form.cleaned_data['url'])
            return HttpResponseRedirect('http://127.0.0.1:8000/fillform/')


    dict = {'form':form}
    return render(request,'firstform.html',context=dict)
