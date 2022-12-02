from http import HTTPStatus

from django.http import JsonResponse

from blog.models import Post
from blog.serializer import post_to_dict_json

# Create your views here.


def posts_fetch_all(request):
    posts = Post.objects.select_related("author").all()

    response = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": response}, status=HTTPStatus.OK)
