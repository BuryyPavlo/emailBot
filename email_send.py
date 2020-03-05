from O365 import Account
from pyo365 import oauth_authentication_flow

def read_txt(name):
    data = ""
    with open(name, 'r') as file:
        data = file.read().replace('\n', '')
    return data

login_file = open('login_info.txt',  'r')
client_id =login_file.readline()[:-1]
client_secret   = login_file.readline()[:-1]

credentials = (client_id, client_secret)

scopes = ['message_all']

account = Account(credentials)
if account.authenticate(scopes=['https://graph.microsoft.com/Mail.Send']):
   print('Authenticated!')

   main_text = read_txt('main_text.txt')
   confintality_notice = read_txt('confintality_notice.txt')
   subject = read_txt('subject.txt')
   str_from = read_txt('from.txt')
   #add loop here if you want to sent to many
   to = 'pavlo.buryi@itoorer.com'
   m = account.new_message()
   m.attachments.add('1.png')
   att = m.attachments[0]
   att.is_inline = True
   att.content_id = 'image.png'
   m.attachments.add('2.png')
   att1 = m.attachments[1]
   att1.is_inline = True
   att1.content_id = 'image1.png'
   m.sender.address = (str_from)
   m.subject = subject

   body = """
    <html>
        <body>
            <strong>"""+main_text+"""</strong>
            <p>
                <img src="cid:image.png">
            </p>
            <p>
                <img src="cid:image1.png">
            </p>
            <p>"""+ confintality_notice+"""</p>
        </body>
    </html>
    """
   m.body = body
   m.to.add(to)
   m.send()

   print('done =)')
else:
   print('something went wrong =(')
