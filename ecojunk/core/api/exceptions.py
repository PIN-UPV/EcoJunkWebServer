from django.db.utils import IntegrityError
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def _handle_generic_error(exc, context, response):
    response.data = {"errors": response.data}
    return response


def extra_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)
    handlers = {"ValidationError": _handle_generic_error}
    # This is how we identify the type of the current exception. We will use
    # this in a moment to see whether we should handle this exception or let
    # Django REST Framework do its thing.
    exception_class = exc.__class__.__name__

    if exception_class in handlers:
        # If this exception is one that we can handle, handle it. Otherwise,
        # return the response generated earlier by the default exception
        # handler.
        return handlers[exception_class](exc, context, response)
    # If response is None, add more cases to the exception handler.
    elif response is None:
        if isinstance(exc, IntegrityError):
            data = {"error": str(exc)}
            return Response(data, status=status.HTTP_400_BAD_REQUEST)

    return response
