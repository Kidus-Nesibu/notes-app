from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required




def note(request):

    if request.method == "POST":

        title = request.POST.get("title")
        content = request.POST.get("content")

        Note.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        return redirect("dashboard")

    return render(request, "take_note.html")


def delete_note(request, pk):
    note = get_object_or_404(
    Note,
    pk=pk,
    user=request.user
)

    if request.method == "POST":
        note.delete()
        return redirect("dashboard")

    return render(request, "delete_note.html")

def edit_note(request, pk):

    note = get_object_or_404(
    Note,
    pk=pk,
    user=request.user
)

    if request.method == "POST":

        note.title = request.POST.get("title")
        note.content = request.POST.get("content")

        note.save()

        return redirect("dashboard")

    return render(
        request,
        "edit_note.html",
        {"note": note}
    )

def view_note(request, pk):

    note = get_object_or_404(
    Note,
    pk=pk,
    user=request.user
)
    return render(
        request,
        "view_note.html",
        {"note": note}
    )

def signup(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "signup.html", {"form": form})

def login_view(request):

    if request.user.is_authenticated:
        return redirect("dashboard")

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

    return render(request, "login.html")\

def logout_view(request):
    logout(request)
    return redirect("login")

