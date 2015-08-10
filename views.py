from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
from itertools import permutations
from .forms import PermutationForm
from .forms import resultForm

def PermutatenString(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PermutationForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
         input_string = form.cleaned_data['input_string']
        
         if (' ' in input_string):
              itemslist = list(permutations(input_string))
         else :
              itemslist = list(permutations(input_string[:10]))
   
         converted = ['']
         for item1 in itemslist:
            converted.append(''.join(item1))
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
         response = HttpResponse() 
        
         response.write( '<div> <h1> All Permutations for this string : \' '+input_string+' \' is  </h1> </br>')
         response.write(converted)        
         response.write('</div>') 
         return HttpResponse(response)
         #request.session['input'] = input_string
         #return HttpResponseRedirect('resultpage')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = PermutationForm()

    return render(request, 'name.html', {'form': form})
# Create your views here.

def resultPage(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = resultForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
         result_string = form.cleaned_data['result_string']
         input_string = request.session.get('input')
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
        
         

    # if a GET (or any other method) we'll create a blank form
    else:
        form = resultForm()

    return render(request, 'result.html', {'form': form})
