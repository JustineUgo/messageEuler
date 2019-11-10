# messageEuler
Python project to send text message of a desired programming problem on projecteuler.net

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You need the python interpreter, get it by visiting
```
https//python.org
```
or click [here](https://python.org/) and install it

### Setting Up Environment

Fork this repo and clone it to your local machine.
Navigate into messagEuler folder and run the following commands

```
pip install pipenv
```
This is to create a virtual environment for the project.

```
pipenv shell
```
To activate the virtual environment

```
pipenv install -r requirements.txt
```
To install the python dependencies used in this project

```
easy_install twilio
```
This command ensures you have the lastest version of twilio, and installs it if not already installed properply.


### More
To use this program, you need to have an account with [Twilio](https://www.twilio.com/), so you would recieve messages from python :smiley:
When you create an account, the wizard will help you set up your twilio phone number which will be used, and also your Account sid and Auth Token, which is needed.

## Running the tests
Return to the messageEuler folder and run
```
python main.py
```
to start the program.
Give valid inputs to the questions asked and you should recieve a message from your twilio number in within some minutes. 

### Note
The time taken to recieve a message, varies!

## Future
Hoping to make it a desktop app, which pops up on starting the computer everyday, so we can code everyday. :computer::computer::computer:

