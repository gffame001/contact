from django.shortcuts import render
from rest_framework import viewsets
from .models import Contact
from .serializers import ContactUsSerializer
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ContactViewset(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactUsSerializer

    def perform_create(self, serializer):
        contact = serializer.save()

        email_subject = "Portfolio Contact Mail"
        email_body = render_to_string('contact_mail.html',{'name':contact.name,'email':contact.email,'message':contact.message})
        email = EmailMultiAlternatives(subject=email_subject,body='',to=['aintisar48@gmail.com'])
        email.attach_alternative(email_body,"text/html")
        email.send()

        return render("success.html",status=status.HTTP_200_OK)