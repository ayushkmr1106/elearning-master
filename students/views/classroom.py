from decouple import config
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from students.forms import ContactForm
from students.models import User
from django.core.mail import EmailMessage
from django.template import loader
from django.contrib import messages
from django.utils.translation import gettext as _
from azure.servicebus import ServiceBusClient, ServiceBusMessage

from datetime import datetime

class SignupView(TemplateView):
    template_name = 'registration/signup.html'


def send_single_message(sender):
    message = ServiceBusMessage("This is a test 2.")
    sender.send_messages(message)

def index(request):

    CONNECTION_STR = "Endpoint=sb://servicebus-ayush.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=JXKkAdnphEMsoSQ8GyDDEJH0nt60j5oqULNBkGJz6fM="
    QUEUE_NAME = "ayushqueue"

    servicebus_client = ServiceBusClient.from_connection_string(conn_str=CONNECTION_STR, logging_enable=True)
    if request.user.is_authenticated:
        with servicebus_client:
            sender = servicebus_client.get_queue_sender(queue_name=QUEUE_NAME)
            with sender:
                now = datetime.now()
                now = now.strftime("%d/%m/%Y %H:%M:%S")
                msg = f"{request.user} is loged in at {now}"
                message = ServiceBusMessage(msg)
                sender.send_messages(message)
        if request.user.is_teacher:
            return redirect('course_list')
        else:
            return redirect('course_list')
    else:
        return redirect('course_list')


def contact_us_view(request):
    form_class = ContactForm

    if request.method == 'POST':
        form = form_class(data=request.POST)

        if form.is_valid():
            contact_name = request.POST.get('contact_name', '')
            contact_email = request.POST.get('contact_email', '')
            form_content = request.POST.get('form_content', '')
            template = loader.get_template('students/contact/contact_template.txt')
            context = {
                'contact_name': contact_name,
                'contact_email': contact_email,
                'form_content': form_content
            }
            content = template.render(context)

            email = EmailMessage(
                _('Nouveau message de myealearning'),
                content,
                _('myealearning'),
                [config('ADMIN_EMAIL')],
                headers = { 'Reply-To': contact_email }
            )
            email.send()
            messages.success(request, _('Thank you ! We will check in as soon as possible ;-)'))
            return redirect('contact_us')
        else:
            messages.info(request, _('Oops ! Message not send...'))
    return render(request, 'students/contact/contact_form.html', { 'form': form_class })


def user_detail(request, username):
    ouser = get_object_or_404(User, username=username, is_active=True)
    return render(request, 'students/user/detail.html', {'ouser': ouser})