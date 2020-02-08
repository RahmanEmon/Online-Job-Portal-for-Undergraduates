from django.shortcuts import render
from .models import Post


def job_post(request):
    post_list = Post.objects.all().order_by('date')
    return render(request,'jobPost/job_post.html',{'post_lists':post_list})


