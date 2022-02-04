from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect

User = get_user_model()


send_mail(
    'Header Testing',
    'Hello {instance.first_name}, This is to remind you that the following drugs would soon expire,  The Expirey Team.',
    'aktakinro@gmail.com',
    ['akinroakintunde@gmail.com'],
    fail_silently=False
)

def send_email(request):
    subject = request.POST.get('subject', '')
    message = request.POST.get('message','')
    from_email = request.POST.get('from_email','')
    if subject and message and from_email:
        try:
            send_mail(subject, message, from_email, ['admin@example.com'])
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return HttpResponseRedirect('/contact/thanks/')
    else:
        return HttpResponse('Make sure all fields are entered and valid.')



# @receiver(post_save, sender=User)
# def send_epired_drug_email(sender, instance, created, **kwargs):
#     if created:
#         message = f"""
#             Hello {instance.first_name},

#             This is to remind you that the following drugs 
#             would soon expire, 

#             The Expirey Team.
#         """
#         send_mail(
#             subject="Expiry date approaching!", 
#             message=message, 
#             recipient_list=[instance.email],
#             from_email="aktakinro@gmail.com"
#             )


