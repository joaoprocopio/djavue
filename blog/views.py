from http import HTTPStatus
from json import loads

from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.db.utils import IntegrityError
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST
from pydantic import ValidationError

from blog.forms import PostForm
from blog.models import Post
from blog.serializer import post_to_dict_json
from blog.service import create_post, get_post, get_posts
from user.service import get_user


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

    if not posts:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    pages = Paginator(posts, per_page)
    posts = pages.get_page(page)
    posts = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": posts})


@require_GET
def blog_get_posts(request, author_id):
    params = {
        "per_page": 15,
        "page": 1,
    }

    if not author_id:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    if request.body:
        params = loads(request.body)

    if ("per_page" and "page") not in params.keys():
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    per_page = params.get("per_page")
    page = params.get("page")

    posts = get_posts(author_id=author_id)

    if not posts:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    pages = Paginator(posts, per_page)
    posts = pages.get_page(page)
    posts = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": posts})


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
@csrf_exempt
def blog_create_post(request):
    if not request.body:
        return JsonResponse({}, status=HTTPStatus.NO_CONTENT)

    if not request.user.is_authenticated:
        return JsonResponse({}, status=HTTPStatus.METHOD_NOT_ALLOWED)

    try:
        body = PostForm.parse_raw(request.body)
        body = body.dict()
        author = get_user(id=body.get("author_id"))
        post = create_post(
            author=author,
            title=body.get("title"),
            text=body.get("text"),
        )
        post = post_to_dict_json(post)

        return JsonResponse(post)

    except ValidationError:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    except IntegrityError:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)

    except ObjectDoesNotExist:
        return JsonResponse({}, status=HTTPStatus.BAD_REQUEST)


@require_POST
def blog_publish_post(request):
    return JsonResponse({})


# TODO: deixa o usuário deletar um post

# TODO: deixa o usuário editar um post
