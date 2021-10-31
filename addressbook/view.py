from django.shortcuts import redirect, render
from .models import Contact
from addressbook.settings import TEMPLATES

from .forms import contactForm

def index(request):
    contacts = Contact.objects.all()
    # search_input = request.GET.get('search-area')
    # if search_input:
    #     contacts = Contact.objects.filter(first_name__contains = search_input)
    # else:
    #     contacts = Contact.objects.all()
    #     search_input = ''
    return render(request, 'index.html', {'contacts': contacts})


def addContact(request):
    template = 'addcontact.html'

    if request.method == "POST":
        form = contactForm (request.POST)

        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = contactForm()

    context = {
        'form': form,
    }
    
    return render(request, template, context)


def contactProfile(request,pk):
    contact = Contact.objects.get(id = pk)
    return render(request,'contact-profile.html', {'contact': contact})

def deleteContact(request,pk):
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})

def search_contact(request):
    if request.method == "GET":
        query_name = request.GET.get('first_name', None)
        if query_name:
            # retrieve all product that contains query_name.
            results = Contact.objects.filter(first_name__icontains=query_name)
            return render(request, 'search_contact.html', {"results":results})
        else:
            results = Contact.objects.all()
            search_contact = ''
    return render(request, 'search_contact.html',{'results':results})
