# About Django Virtual Chat App
This is a virtual chat app made entirely using the Django Web Framework and the Django Template Language. You make rooms and users join in the chat. Only logged in users are allowed to chat. Make sure you have made accounts before starting to use the app.

## Getting Started
To get started follow these steps.
1. Head over to the command line and type the following command to install all required libraries: ```pip install -r requirements.txt```. Make sure you have opened the folder containing this file as the top level directory in you command line shell.
2. It will be best if you first start the local development server on your local machine only using the classic command ```python manage.py runserver```. This will start a local server at the URL ```127.0.0.1:8000```.
3. By default there are no user accounts nor there are rooms. To create the first ever account, head over to the command line and type the following command: ```python manage.py createsuperuser```. Follow the on-screen instructions to make a super user. This user is now able to view and edit the contents of the database.
4. Head on over to the url ```127.0.0.1/chat/``` to reach the home page of the site. If you aren't logged in here, you can now log in using the hyper link ```... log in ...``` in the header.
5. After you've logged in, create a room using the ```Create Room``` button, add a name and description to the room you're making and press enter to show it to the users for them to join!

## Notes
1. This website is a real-time chat application so all the messages that users make will be populated to all other users connected to the same room.
2. This project currently does not support private messaging but this feature is welcome to be implemented by you. With that said, I shall add my own implementation of it later, after learning deeply, the asynchronous side of Django.
3. If you find any issues in the working of this project, be sure to write an issue on GitHub.