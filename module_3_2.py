def send_email(message, recipient, *, sender='university.help@gmail.com'):
    suffixes = ('.com', '.ru', '.net')
    if ('@' not in recipient
            or '@' not in sender
            or not recipient.endswith(suffixes)
            or not sender.endswith(suffixes)):
        print(f'Невозможно отправить письмо с адреса {sender} на'
              f' адрес {recipient}')
    elif recipient == sender:
        print('Нельзя отправить письмо самому себе!')
    elif sender == 'university.help@gmail.com':
        print(f'Письмо успешно отправлено с адреса {sender} на'
              f' адрес {recipient}.')
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса'
              f' {sender} на адрес {recipient}.')


send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!',
           'urban.fan@mail.ru',
           sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание',
           'urban.student@mail.ru',
           sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре',
           'urban.teacher@mail.ru',
           sender='urban.teacher@mail.ru')
