import os
import urlparse
import smtplib

from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect
from werkzeug.formparser import parse_form_data
from email.mime.text import MIMEText

def get_request(request):
    if request.method == 'POST':
        form_data = request.form

        send_email(form_data)

def send_email(form_data):
    msg = MIMEText(form_data)
    msg['Subject'] = 'Data from a form'
    msg['From'] = 'The form'
    msg['To'] = goossenm@osuosl.org
    s = smtplib.SMTP('localhost')
    s.sendmail('the form', goossenm@osuosl.org, msg.as_string())
    s.quit()

if __name__ == '__main__':
