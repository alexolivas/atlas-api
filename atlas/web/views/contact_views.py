from django.core.mail import send_mail

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

# from validate_email import validate_email


class ContactMe(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        # https://docs.djangoproject.com/en/2.0/topics/email/
        # Throttle this endpoint to only accept 25 emails a day
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
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=from_email,
                    recipient_list=['to@example.com'],
                    fail_silently=False,
                )
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
