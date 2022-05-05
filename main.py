import pywhatkit
import os


def send_message_inst():
    mobile = input("Введите номер получателя: ")
    message = input("Введите текст сообщения: ")
    pywhatkit.sendwhatmsg(phone_no=mobile, message=message, time_hour=20, time_min=14)

def main():
    send_message_inst()

if __name__ == '__main__':
    main()