from http import HTTPStatus
from json import loads

from django.contrib.auth.models import User
from django.core.handlers.wsgi import WSGIRequest
from django.core.paginator import Paginator
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
    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    body = loads(request.body)

    form = body.get("paginator")

    if not form:
        per_page = 15
        page = 1

    else:
        per_page = form.get("per_page")
        page = form.get("page")

    qs = get_posts().order_by("posted_at").reverse()
    paginator = Paginator(object_list=qs, per_page=per_page)
    page = paginator.get_page(page)
    posts = [post_to_dict_json(post) for post in page]

    return JsonResponse({"posts": posts})


@csrf_exempt
@require_GET
def blog_get_posts_by_author_id(request: WSGIRequest, author_id: int) -> JsonResponse:
    if not author_id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
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
