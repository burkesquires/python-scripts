# Created by @advaitasaha
# Imports
import requests

# Variables
global apiKey
global SID
global senderID
apiKey = ""  # enter your api key
SID = ""  # enter your SID number
senderID = ""  # enter the senderID registered

# Functions for semding SMS


def send_sms(number):

    headers_sms = {
        "api-key": apiKey,
    }

    data_sms = {
        "type": "TXN",
        "to": f"+91{str(number)}",
        "sender": senderID,
        "source": "API",
        "body": 'Thank you name for using this software.',
        "template_id": "1207161891861378858",
    }


    response = requests.post(
        f"https://api.kaleyra.io/v1/{SID}/messages",
        headers=headers_sms,
        data=data_sms,
    )

    return response.json()


def number_val(number):

    headers = {
        "Content-Type": "json",
        "api-key": apiKey,
    }

    response = requests.get(
        f"https://api.kaleyra.io/v1/{SID}/lookup/+91{str(number)}",
        headers=headers,
    )

    if response.json()["invalid_count"]:
        return False, response.json()
    else:
        return True, response.json()


def send_flash_sms(number):

    headers = {
        "api-key": apiKey,
    }

    data = {
        "to": f"+91{str(number)}",
        "type": "TXN",
        "sender": senderID,
        "body": 'Thank you name for using this software.',
        "flash": "1",
    }


    response = requests.post(
        f"https://api.kaleyra.io/v1/{SID}/messages", headers=headers, data=data
    )

    return response.json()


while True:
    print("------------------------------------------------------------------")
    print("Welcome to Kaleyra SMS sending software, created by @Advaita Saha")
    print("------------------------------------------------------------------")
    print("1: Send SMS")
    print("2: Send flash SMS")
    print("3: Check Number Validity")
    print("0: Exit Program")
    print("------------------------------------------------------------------")
    userInput = int(input("Enter the option number you want to perform: "))

    if userInput == 0:
        break
    elif userInput == 1:
        number = int(input("Enter the phone number to which you want to send: "))
        out = send_sms(number)
        print("------------------------------------------------------------------")
        print("SMS sent, below is the JSON output")
        print(out)

    elif userInput == 2:
        number = int(input("Enter the phone number to which you want to send: "))
        out = send_flash_sms(number)
        print("------------------------------------------------------------------")
        print("Flash SMS sent, below is the JSON output")
        print(out)

    elif userInput == 3:
        number = int(input("Enter the phone number to which you want to send: "))
        out = number_val(number)
        if out[0]:
            print("------------------------------------------------------------------")
            print("Valid Number, details below")
        else:
            print("------------------------------------------------------------------")
            print("Invalid Number")
        print(out[1])