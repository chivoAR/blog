from django import forms

class PermutationForm(forms.Form):
    input_string = forms.CharField(label='String to be permutation', max_length=100)
   

class resultForm(forms.Form):
    result_string = forms.CharField(label='permutation', max_length=1000000)
   
