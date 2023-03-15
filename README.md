# Python Notification Decorator

## Installation
Just clone the repo and replace {event} and {key} with the IFTT applet name and key
If you don't have an IFTT account, follow the website steps to create an applet, generate a webhook and send a push notification.
Then install on your phone the IFTT app.
Other than that, maybe run `pip install requests` for http requests in Python.

## Usage
The code gives a "notify" decorator that will notify the user on his phone if the function finishes or crashes
Just decorate your functions
