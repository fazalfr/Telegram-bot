# Telegram-bot
Django Telegram Bot with User Call Counts
This is a simple Django project that includes a Telegram bot interface with three buttons ("stupid", "fat", and "dumb") that display jokes to users. The project also includes a model that records the number of times each button is clicked on a per-user basis, and a web page that displays a table of users and their call counts.

# Dependencies
Python 3.x
Django 3.x
PostgreSQL
python-telegram-bot

# Installation
Clone the repository to your local machine.
Install Python 3.x and PostgreSQL if they are not already installed.
Install Django and python-telegram-bot by running the command pip install Django python-telegram-bot in your terminal/command prompt.
Set up your PostgreSQL database settings in settings.py.
Run python manage.py migrate to create the necessary database tables.
Create a superuser account by running python manage.py createsuperuser.
Run the Django development server by running python manage.py runserver.


# Configuration
In order to run the Telegram bot, you will need to obtain a bot token from the BotFather on Telegram. Once you have the bot token, add it to settings.py:

python
Copy code
TELEGRAM_BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE'
Usage
Navigate to http://localhost:8000/admin and log in with your superuser credentials to add some users to the database.
Navigate to http://localhost:8000/telegram-bot/ to access the Telegram bot interface. Click on the "stupid", "fat", or "dumb" buttons to display jokes.
Navigate to http://localhost:8000/user_call_counts/ to view the table of users and their call counts.


