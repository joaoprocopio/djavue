from django.http import JsonResponse


def current_user_view(request):
    return JsonResponse(
        {
            "is_authenticated": request.user.is_authenticated,
        }
    )
