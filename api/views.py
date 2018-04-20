from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt

from blog.models import Post


@csrf_exempt
def post_list(request):
  if request.method == "GET":
    posts = Post.objects.all()
    posts_json = [p.to_json() for p in posts]
    return JsonResponse(posts_json, safe=False)
  elif request.method == "POST":
    data = request.POST
    post = Post()
    post.title = data.get('title', '')
    post.text = data.get('text', '')
    post.published_date = data.get('published_date', '')
    post.save()
    
    return JsonResponse(post.to_json(), status=201)


@csrf_exempt
def post_detail(request, post_id):

  try:
    post = Post.objects.get(pk=post_id)
  except Exception as e:
    return JsonResponse({"error": str(e)}, status=404)

  if request.method == "GET":
    return JsonResponse(post.to_json())
  elif request.method == "PUT":
    data = QueryDict(request.body)
    post.title = data.get('title', post.title)
    post.text = data.get('text', post.text)
    post.published_date = data.get('published_date', post.published_date)
    post.save()
    return JsonResponse(post.to_json())
  elif request.method == "DELETE":
    post.delete()
    return JsonResponse(post.to_json())