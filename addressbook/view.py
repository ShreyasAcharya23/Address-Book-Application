from django.shortcuts import redirect, render
from .models import Contact
from addressbook.settings import TEMPLATES



from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required

from .forms import contactForm

def index(request):
    contacts = Contact.objects.all()
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
        search_contact = request.GET.get('search_contact')
        if search_contact:
            # retrieve all product that contains query_name.
            results = Contact.objects.filter(first_name__icontains=search_contact)
            return render(request, 'search_contact.html', {"results":results} ) #results are saved and passed as a dictionary
    else:
        results = Contact.objects.all()  
        results = ''
        return render(request, 'search_contact.html',{'results': results})


def loginPage(request):
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

def logoutUser(request):
	logout(request)
	return redirect('login')