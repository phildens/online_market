import smtplib
import string
from email.mime.text import MIMEText
from email.header import Header
import random

from resetpassword.mail_information import login, password, test_mail


def send_reset_mail(to: str):
    code = randomword()
    msg = MIMEText(f'{code}', 'plain', 'utf-8')
    msg['Subject'] = Header('Восстановление пароля сайта', 'utf-8')
    msg['From'] = login
    msg['To'] = to

    s = smtplib.SMTP('smtp.yandex.ru', 587, timeout=10)
    try:
        s.starttls()
        s.login(login, password)
        s.sendmail(msg['From'], msg['To'], msg.as_string())
    except Exception as ex:
        print(ex)
        return 'something went wrong'
    finally:
        s.quit()
    return code


def randomword():
    letters = string.digits
    return ''.join(random.choice(letters) for i in range(6))


def main():
    send_reset_mail(to=test_mail)


if __name__ == '__main__':
    main()
