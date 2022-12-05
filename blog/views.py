from http import HTTPStatus

from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post
from blog.serializer import post_to_dict_json
from blog.service import _get_post, _get_posts

# Create your views here.


@csrf_exempt
def blog_posts(request: WSGIRequest) -> object:
    posts = _get_posts()
    posts = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": posts})


def blog_post(request: WSGIRequest, id: str) -> object:
    if not id:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    if not id.isdigit():
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        post = _get_post(id=id)
        post = post_to_dict_json(post)

        return JsonResponse(post)

    except Post.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


# TODO: retorna posts por usuário

# TODO: deixa o usuário criar um post

# TODO: deixa o usuário publicar um post criado

# TODO: deixa o usuário deletar um post

# TODO: deixa o usuário editar um post
