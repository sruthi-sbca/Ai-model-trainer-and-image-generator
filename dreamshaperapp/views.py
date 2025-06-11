import subprocess
import os
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Path to store the progress
LOG_FILE_PATH = "progress.log"

# ----------------------------
# Auth Views
# ----------------------------

def register_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', {'form': form})

# ----------------------------
# Trainer Views (Protected)
# ----------------------------

@login_required
def run_bat_stream(request):
    bat_file_path = r'I:\onetrainer2.bat'  # Path to your batch file

    def generate():
        process = subprocess.Popen([bat_file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        with open(LOG_FILE_PATH, 'w') as log_file:
            for stdout_line in iter(process.stdout.readline, ""):
                log_file.write(stdout_line)
                log_file.flush()

            for stderr_line in iter(process.stderr.readline, ""):
                log_file.write(stderr_line)
                log_file.flush()

        process.stdout.close()
        process.stderr.close()
        process.wait()

    generate()
    return JsonResponse({"status": "Command started!"})

@login_required
def get_progress(request):
    if os.path.exists(LOG_FILE_PATH):
        with open(LOG_FILE_PATH, "r") as f:
            progress = f.read()
    else:
        progress = "No progress yet."

    return JsonResponse({"progress": progress})

# ----------------------------
# Pages (Protected)
# ----------------------------

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def index(request):
    return render(request, 'template.html')


def signup_view(request):
    if request.user.is_authenticated:
        return redirect('homepage')  # already logged in

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in immediately
            return redirect('homepage')
    else:
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})