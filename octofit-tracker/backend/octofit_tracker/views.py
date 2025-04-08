from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the OctoFit Tracker API!",
        "codespace_url": "https://ominous-parakeet-jj94rrrjwxqp29j7-8000.app.github.dev",
        "localhost_url": "http://localhost:8000"
    })