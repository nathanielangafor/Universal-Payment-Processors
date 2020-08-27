import requests
import json
import datetime
import sqlite3
from datetime import timedelta

# Lines to edit
# 62: One Sec Mail API Username
# 95: Create read.txt file
# 104/105: Should be your customers cashtag and expected amount


def cashappTable():
    conn = sqlite3.connect('definitelynotadb.db')
    c = conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS cashappPayments (sender TEXT, amount TEXT, time TEXT, status TEXT)')
    conn.close()


def delete(table, column, value):
    conn = sqlite3.connect('definitelynotadb.db')
    c = conn.cursor()
    c.execute('DELETE FROM {} WHERE {}=(?)'.format(table, column), (value,))
    conn.commit()
    conn.close()


def insertCashapp(sender, amount, time, status):
    delete('cashappPayments', 'sender', sender)
    conn = sqlite3.connect('definitelynotadb.db')
    c = conn.cursor()
    c.execute('INSERT INTO cashappPayments (sender, amount, time, status) VALUES (?, ?, ?, ?)',
              (sender, amount, time, status))
    conn.commit()
    conn.close()


def update(table, setColumn, firstValue, whereColumn, secondValue):
    conn = sqlite3.connect('definitelynotadb.db')
    c = conn.cursor()
    c.execute('UPDATE {} SET {}=(?) WHERE {}=(?)'.format(table, setColumn, whereColumn), (firstValue, secondValue,))
    conn.commit()
    conn.close()


def read(table, column, value):
    conn = sqlite3.connect('definitelynotadb.db')
    c = conn.cursor()
    c.execute('SELECT * From {} WHERE {}=(?)'.format(table, column), (value,))
    data = c.fetchall()
    conn.close
    return data


def cashApp(expected, cashtag):
    try:
        payment = read('cashappPayments', 'sender', cashtag)[0]
        amount = float(payment[1])
        return amount >= float(expected)
    except:
        return False


def check():
    arg1 = '0JONutOZP11AItKM6R1'  # Your one sec mail username
    mails = requests.get(
        'https://www.1secmail.com/api/v1/?action=getMessages&login=' + arg1 + '&domain=1secmail.com').json()
    for mail in mails:
        mid = mail['id']
        parent_mailinfo = requests.get(
            'https://www.1secmail.com/api/v1/?action=readMessage&login={}&domain=1secmail.com&id={}'.format(arg1,
                                                                                                            mid)).json()
        From = parent_mailinfo['from']
        body = parent_mailinfo['textBody']
        if str(From[60:]) == '@amazonses.square.com' and str(body).__contains__('https://cash.app/payments/'):
            receipt = str(body).split('visit: ')[1].strip()
            with open('read.txt', 'r+') as f:
                read = f.read()
            if receipt not in read:
                r = requests.get(receipt)
                data = json.loads(str(r.text).splitlines()[6].replace('paymentHistoryData: ', ''))
                sender = str(data['header_subtext']).replace('Payment from ', '').strip().lower()
                amount = float(str(data['amount_formatted']).replace('$', ''))
                try:
                    g_parent_t = data['details_view_content']['rows'][1]
                except:
                    g_parent_t = data['details_view_content']['rows'][0]
                if g_parent_t.__contains__('Today at ') or g_parent_t.__contains__('Yesterday at '):
                    receiptTime = g_parent_t.replace('Today at ', '').replace('Yesterday at ', '')
                    parentTime = datetime.datetime.strptime(receiptTime, "%I:%M %p")
                    time = datetime.datetime.strftime(parentTime + timedelta(hours=3), "%D %H:%M")
                    if str(data['activity_section']) == 'COMPLETE' and str(data['is_action_required']) == 'False':
                        insertCashapp(str(sender).strip().lower(), amount, time, 'complete')
                    else:
                        pass
                with open('read.txt', 'a') as f:
                    f.write(receipt + '\n')


cashappTable()

expected = 10  # $10 Obviously :)
address = '$someCashtag'

if cashApp(expected, address) == True:
    delete('cashappPayments', 'sender', address)  # Deletes the transaction after it has been used
    pass  # Send user item instead of pass
