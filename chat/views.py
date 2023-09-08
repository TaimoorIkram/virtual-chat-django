from django.shortcuts import render, redirect
from .models import Message, Room, Villa
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RoomForm, SignupForm
from django.contrib import messages

# Create your views here.

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('chat:home')
        else:
            return redirect('chat:login')

    user = request.user
    return render(request, 'chat/login.html', {'user': user})

def logout_user(request):
    logout(request)
    return redirect('chat:home')

def home(request):
    rooms = Room.objects.all().order_by('name')
    user = request.user
    return render(request, 'chat/home.html', {'rooms': rooms, 'user': user})

def room(request, room_name):
    room_id = Room.objects.get(name=room_name).id
    previous_chat = Message.objects.filter(room=room_id).order_by('send_time')
    return render(request, 'chat/room.html', {'room': room_name, 'old_chat': previous_chat})

def create_room(request):

    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            try:
                target_room = Room.objects.get(name=name)
                if target_room:
                    messages.add_message(request, messages.ERROR, "This room already exists!")
                
            except Exception:
                Room.objects.create(name=name, created_by=request.user, description=description)
            
            return redirect('chat:home')
            

    room_form = RoomForm()
    
    return render(request, 'chat/add_room.html', {'form': room_form})
    
def delete_room(request):
    if request.method == 'POST':
        target_id = request.POST['id']

        target_room = Room.objects.get(id=target_id)
        if target_room.created_by.username == request.user.username:
            target_room.delete()
        else:
            messages.add_message(request, messages.ERROR, 'You must be the owner of the room you\'re trying to delete.')
        
    return redirect('chat:home')

def edit_room(request, id):

    if request.method == 'POST':
        form = RoomForm(request.POST)

        if form.is_valid() :
            name = form.cleaned_data['name']
            description = form.cleaned_data['description']

            try:
                target_room = Room.objects.get(name=name)

                if target_room.created_by.username == request.user.username:
                    target_room.description = description
                    target_room.save()
                    messages.add_message(request, messages.SUCCESS, 'Changes saved successfully!')
                else: messages.add_message(request, messages.ERROR, 'You must be the owner of the room you\'re trying to edit.')
                
            except Exception:
                messages.add_message(request, messages.ERROR, 'Room does not exist.')        
            
            return redirect('chat:home')
    
    target_room = Room.objects.get(id=id)
    
    room_form = RoomForm(initial={'name':target_room.name, 'description':target_room.description})

    return render(request, 'chat/edit_room.html', {'form': room_form})


def signup_user(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('chat:home')

    signup_form = SignupForm()

    return render(request, 'chat/signup.html', {'form': signup_form})

def villa(request, villa_name):
    villa = Villa.objects.get(name=villa_name)
    rooms = Room.objects.filter(villa=villa.id)
    # previous_chat = Message.objects.filter(room=villa_id).order_by('send_time')

    return render(request, 'chat/villa.html', {'villa': villa, 'rooms': rooms})

def villa_room(request, villa_name, room_name):
    villa = Villa.objects.get(name=villa_name)
    rooms =  Room.objects.filter(villa=villa.id)
    room_current = rooms.get(name=room_name)
    previous_chat = Message.objects.filter(room=room_current.id).order_by('send_time')
    return render(request, 'chat/villa_room.html', {'villa': villa, 'room_current': room_current.name, 'rooms': rooms, 'old_chat': previous_chat})

def home_main(request):
    return render(request, 'chat/home_main.html')