from django.utils import timezone


class UpdateLastLoginMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.user.is_authenticated:
            request.user.last_login = timezone.now()
            request.user.save()

        return response
