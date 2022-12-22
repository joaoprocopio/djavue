from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from blog.models import Post
from blog.serializer import post_to_dict_json
from blog.service import get_post, get_posts

# Create your views here.


@csrf_exempt
@require_GET
def blog_home_page(request: WSGIRequest) -> JsonResponse:
    posts = get_posts()
    posts = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": posts})


@require_GET
def blog_get_post_by_id(request: WSGIRequest, id: str) -> JsonResponse:
    if not id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        post = get_post(id=id)
        post = post_to_dict_json(post)

        return JsonResponse(post)

    except Post.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


# TODO: retorna posts por usuário

# TODO: deixa o usuário criar um post

# TODO: deixa o usuário publicar um post criado

# TODO: deixa o usuário deletar um post

# TODO: deixa o usuário editar um post
