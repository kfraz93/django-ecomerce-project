from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from item.models import Category, Item
from .forms import SignupForm, UserProfileEditForm

def index(request):
    """
    This view will be used inside the puddle/urls.py file
    :param request:
    :return:
    """
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

@login_required
def profile_edit(request):
    if request.method == 'POST':
        form = UserProfileEditForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Your profile is successfully updated")
            return redirect('core:profile_edit')
    else:
        form = UserProfileEditForm(instance=request.user)
    return render(request, 'core/profile_edit.html', {
        'form': form,
        'title': 'Edit Profile',
    })
