from django.shortcuts import redirect, render
from .models import Contact
from addressbook.settings import TEMPLATES

from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from .forms import contactForm

def index(request):
    contacts = Contact.objects.all()
    return render(request, 'index.html', {'contacts': contacts})

# Add Contact method
def addContact(request):
    template = 'addcontact.html'

    if request.method == "POST":
        form = contactForm (request.POST)
        # saves form after validating the form
        if form.is_valid():
            form.save()
            # redirects to the index page
            return redirect('/')
    else:
        form = contactForm()

    context = {
        'form': form,
    }
    
    return render(request, template, context)

# Contact Profile Method
def contactProfile(request,pk):
    # Takes paramenter as request and primary key (pk) where pk is the ID of the contact which is assigned to each contact after being created in the database
    contact = Contact.objects.get(id = pk)
    return render(request,'contact-profile.html', {'contact': contact})

# Delete Contact Method
def deleteContact(request,pk):
    # Takes paramenter as request and primary key (pk) where pk is the ID of the contact which is assigned to each contact after being created in the database
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        # Redirects to the index page
        return redirect('/')
    return render(request, 'delete.html', {'contact': contact})

def search_contact(request):
    
    if request.method == "GET":
        # GET Request for the searched_contact in the form
        search_contact = request.GET.get('search_contact')
        if search_contact:
            # Retrieve all product that contains query_name.
            results = Contact.objects.filter(first_name__icontains=search_contact)
            #Results are saved and passed as a dictionary
            return render(request, 'search_contact.html', {"results":results} ) 
    else:
        results = Contact.objects.all()  
        results = ''
        return render(request, 'search_contact.html',{'results': results})

# Login Method
def loginPage(request):
    
	if request.user.is_authenticated:
		return redirect('/')
	else:
		if request.method == 'POST':
            # GET the username and password
			username = request.POST.get('username')
			password =request.POST.get('password')
            # Authenticates the User
			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
                # Directs to the index page
				return redirect('/')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'login.html', context)

# Logout Method
def logoutUser(request):
	logout(request)
	return redirect('login')