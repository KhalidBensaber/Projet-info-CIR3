class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"Requête reçue mid: {request.method} {request.path}")
        response = self.get_response(request)
        return response
