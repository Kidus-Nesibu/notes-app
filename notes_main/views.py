from django.http import HttpResponse
from django.shortcuts import render
from notes.models import Note
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, "landing.html")

@login_required
def dashboard(request):

    notes = Note.objects.filter(
        user=request.user
    )

    return render(
        request,
        'dashboard.html',
        {'notes': notes}
    )

def note(request):
    return render(request, "take_note.html")

