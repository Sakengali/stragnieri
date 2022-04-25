from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms

#form for request submission
class NewBookForm(forms.Form):
    book_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'book name'}))
    book_url = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'book url aws/abebooks'}))


#list-database
requests_info = []

def index(request):
    return render(request, "main/main.html", {
        "form": NewBookForm
    })

def requests(request):
    if request.method == 'POST':
        #a form object; request.POST - gives all values of form
        form = NewBookForm(request.POST)        

        if form.is_valid():
            #cleaned.data is a way to access data
            book_name = form.cleaned_data['book_name']   
            book_url = form.cleaned_data['book_url']   

            #append a dict of data to the list 
            requests_info.append({"book_name": book_name, "book_url" : book_url})            
        else:
            #if form is invalid, load main again
            render(request, "main/main.html", {
                "form": NewBookForm
            })
    print(f"requests: {requests_info}")
    return render(request, "main/requests.html",{
        "requests_info": requests_info
    })


#TODO: urlfield; ...