from django.conf import settings
from django.shortcuts import redirect

class LoginRequiredMiddleware:
    """
    Middleware that requires a user to be authenticated to access any view
    except for paths defined in EXEMPT_URLS.
    """
    EXEMPT_URLS = [settings.LOGIN_URL, '/registration/', '/admin/']

    def __init__(self, get_response):
        self.get_response = get_response

    # def __call__(self, request):
    #     if not request.user.is_authenticated:
    #         if not any(request.path.startswith(url) for url in self.EXEMPT_URLS):
    #             return redirect(settings.LOGIN_URL)
    #     return self.get_response(request)
    def __call__(self, request):
        print("Request path:", request.path)
        print("User authenticated:", request.user.is_authenticated)
        if not request.user.is_authenticated:
            exempt = any(request.path.startswith(url) for url in self.EXEMPT_URLS)
            print("Is path exempt?", exempt)
            if not exempt:
                return redirect(settings.LOGIN_URL)
        return self.get_response(request)