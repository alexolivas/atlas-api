from django.conf import settings
from django.core.mail import send_mail

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.throttling import AnonRateThrottle
from rest_framework.views import APIView


class ContactMe(APIView):
    permission_classes = (AllowAny,)
    throttle_classes = (AnonRateThrottle,)

    def post(self, request):
        name = request.POST.get('name', '')
        subject = request.POST.get('subject', '')
        from_email = request.POST.get('from', '')
        message = request.POST.get('message', '')

        errors = []
        if str(name).strip() == '':
            errors.append('Name is required')
        if str(subject).strip() == '':
            errors.append('Subject is required')
        if str(from_email).strip() == '':
            errors.append('Email is required')
        if str(message).strip() == '':
            errors.append('Message body is required')

        if not errors:
            try:
                email_to = settings.DEFAULT_CONTACT_EMAIL_ADDRESS
                if email_to is not None:
                    send_mail(
                        subject=subject,
                        message=message,
                        from_email=from_email,
                        recipient_list=['to@example.com'],
                        fail_silently=False,
                    )
                else:
                    return Response({
                        'details': 'Encountered a problem sending this message. This is temporary and will '
                                   'be resolved shortly. Please try again later or send me a message via LinkedIn',
                        'success': False
                    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            except Exception as e:
                # Something went wrong sending this message
                return Response({
                    'details': str(e),
                    'success': False
                }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            # Message successfully sent
            return Response({
                'details': 'Message sent!',
                'success': True
            })
        else:
            return Response({
                'details': errors
            }, status=status.HTTP_400_BAD_REQUEST)
