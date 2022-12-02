from django.http import JsonResponse

from blog.models import Post
from blog.serializer import post_to_dict_json

# Create your views here.


def posts_fetch_all(request):
    posts = Post.objects.select_related("author").all().order_by("posted_at").reverse()

    response = [post_to_dict_json(post) for post in posts]

    return JsonResponse({"posts": response})


def post_fetch(request, id):
    post = Post.objects.select_related("author").get(id=id)

    response = post_to_dict_json(post)

    return JsonResponse(response)
