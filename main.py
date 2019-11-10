import requests
from bs4 import BeautifulSoup
from twilio.rest import Client

#requests for question number, and other twilio requirements
user_question=int(input("What question on projecteuler, do you want?\n"))
account_sid = input("What is your twilio account_sid?\n")
auth_token= input("What is your auth_token?\n")
your_twilio_num = input("What is your twilio number?\n")
reciever = input("What is the reciever number? \n")

client = Client(account_sid, auth_token)

#scrap the question
url = 'https://projecteuler.net/problem={}'.format(user_question)
response = requests.get(url)
web_page = response.content

#get text of question
soup = BeautifulSoup(web_page, 'html.parser')
euler_problem = soup.find(class_="problem_content").get_text()

#write message
message = client.messages.create(
    to =reciever,
    from_=your_twilio_num,
    body=euler_problem
)

#print(message.sid)

