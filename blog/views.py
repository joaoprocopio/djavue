from http import HTTPStatus
from json import loads

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from blog.models import Post
from blog.serializer import post_to_dict_json
from blog.service import get_post, get_posts


@csrf_exempt
@require_GET
def blog_home_page(request):
    params = {
        "per_page": 15,
        "page": 1,
    }

    if request.body:
        params = loads(request.body)

    if ("per_page" and "page") not in params.keys():
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    per_page = params.get("per_page")
    page = params.get("page")

    posts = get_posts().order_by("published_at").reverse()
    pages = Paginator(posts, per_page)
    posts = pages.get_page(page)
    posts = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": posts})


@csrf_exempt
@require_GET
def blog_get_posts(request, author_id):
    if not author_id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        posts = get_posts(author_id=author_id)
        posts = [post_to_dict_json(post) for post in posts]

        return JsonResponse({"posts": posts})

    except User.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@require_GET
def blog_get_post(request, id):
    if not id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    try:
        post = get_post(id=id)
        post = post_to_dict_json(post)

        return JsonResponse(post)

    except Post.DoesNotExist:
        return JsonResponse({}, status=HTTPStatus.NOT_FOUND)


@require_POST
def blog_create_post(request):
    return JsonResponse({})


@require_POST
def blog_publish_post(request):
    return JsonResponse({})


# TODO: deixa o usuário deletar um post

# TODO: deixa o usuário editar um post
