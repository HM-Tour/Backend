from django.shortcuts import render,HttpResponseRedirect

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from post.models import Post


@login_required
def user_id(request):
    user_id = request.user.id
    return JsonResponse({"user_id": user_id})

@login_required
def create_post(request):
    post = Post.objects.create(owner=request.user)
    return HttpResponseRedirect("api/posts/")