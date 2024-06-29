from django.shortcuts import render,redirect, get_object_or_404
from .models import Examen, Profil, Sujet
from .forms import ProfilForm, SignUpForm, UserProfilForm
from django.contrib.auth import authenticate, login 
from django.contrib.auth.decorators import login_required
from django.db.models import Q

@login_required
def home (request):
    user = request.user.profil.sujet
    posts = Examen.objects.filter(sujet=user)
    context = {'user':user, 'posts':posts}
    return render (request, 'home.html', context)
@login_required
def profile (request):
    profil, created = Profil.objects.get_or_create(user=request.user)
    profil = Profil.objects.all()
    return render (request, 'profile.html', {'profil':profil, 'user':request.user})

def edit_profil (request):
    profil, created = Profil.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = ProfilForm( request.POST, request.FILES, instance=profil)
        user_form = UserProfilForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid() and user_form.is_valid():
            form.save()
            user_form.save()
            return redirect ('profile')
    else :
        form = ProfilForm()
        user_form = UserProfilForm(instance=request.user)
    return render (request, 'edit_profil.html', {'form':form, 'user_form':user_form})
def signup (request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect ('edit profil')
    else :
        form = SignUpForm()
    return render (request, 'signup.html', {'form':form})
#here that's the part of detail post 
def post_detail (request, pk):
    examen = get_object_or_404(Examen, pk=pk)
    recommendation = Examen.objects.order_by('-titre').exclude(pk=pk)[:8]
    return render (request, 'post_detail.html', {'examen':examen, 'recommendation':recommendation})

#here the part of search yups i comment in english sorry :)
def search (request):
    query = request.GET.get('q')
    resultats = []
    if query :
        resultats =  Examen.objects.filter(Q(titre__icontains=query))
    return render (request, 'search.html',{'resultats':resultats, 'query':query})

