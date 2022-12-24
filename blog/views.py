from http import HTTPStatus

from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET

from blog.models import Post
from blog.serializer import post_to_dict_json
from blog.service import get_post, get_posts
from user.service import _get_user as get_user

# Create your views here.


@csrf_exempt
@require_GET
def blog_home_page(request: WSGIRequest) -> JsonResponse:
    posts = get_posts().order_by("posted_at").reverse()
    posts = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": posts})


@csrf_exempt
@require_GET
def blog_get_posts_by_author_id(request: WSGIRequest, author_id: int) -> JsonResponse:
    if not author_id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        """
        Procura primeiro o usuário,
        e se encontrar o usuário
        continua a chamada da função.
        O problema disso é o fato de
        estar acontecendo duas queries
        (uma pro usuário, e outra para os posts).
        O ponto positivo, é que se não encontrar
        o usuário, a função já para.
        """
        author = get_user(id=author_id)
        posts = get_posts(author=author)
        posts = [post_to_dict_json(post) for post in posts]

        return JsonResponse({"posts": posts})

    except User.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@require_GET
def blog_get_post_by_id(request: WSGIRequest, id: int) -> JsonResponse:
    if not id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        post = get_post(id=id)
        post = post_to_dict_json(post)

        return JsonResponse(post)

    except Post.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


# TODO: deixa o usuário criar um post

# TODO: deixa o usuário publicar um post criado

# TODO: deixa o usuário deletar um post

# TODO: deixa o usuário editar um post
