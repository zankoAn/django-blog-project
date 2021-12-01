from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, UpdateView
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .models import Post
from datetime import datetime



class HomePageView(ListView):
    template_name = "post/home_page.html"
    context_object_name = "Posts"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_can_like"] = Post.user_can_like(Post, self.request.user)
        return context  

    def get_queryset(self):
        """
            Show the last 6 edited posts.
        """

        posts = Post.objects.all().order_by("-update_date", "-id")[:6]
        return posts


@method_decorator(login_required, name="dispatch")
class LikeView(UpdateView):
    model = Post
    fields = ("__all__")
    template_name = "post/home_page.html"

    def get(self, request, *args, **kwargs):
        """
            Get request and decrease or increase the number of likes.
        """

        pk = kwargs.get("pk")
        user = request.user
        post = get_object_or_404(Post, pk=pk)

        if user in post.likes.all():
            post.likes.remove(user)
            like_count = post.likes.count()
            
            return JsonResponse({
                "status": "ok",
                "like_count": like_count,
                "class": "bi bi-heart"})
        else:
            post.likes.add(user)
            like_count = post.likes.count()

            return JsonResponse({
                "status": "ok",
                "like_count": like_count,
                "class": "bi bi-heart-fill"})
  

class PostDetailView(DetailView):
    template_name = "post/post_detail.html"
    context_object_name = "post"

    # The following line is just a test and will be deleted later...
    extra_context = {"testa":["https://mdbootstrap.com/img/Photos/Avatars/img%20(33).jpg", ], "inner_comment":False, "comments_inner":[2]}

    def get_queryset(self):
        date = datetime(
            self.kwargs["year"],
            self.kwargs["month"],
            self.kwargs["day"]).date()
        
        post_id = self.kwargs["pk"]
        post = Post.objects.filter(pk=post_id, publish_date=date)
        return post
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_can_like"] = Post.user_can_like(Post, self.request.user)
        return context
