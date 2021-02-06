from django.contrib import messages
from django.shortcuts import render, redirect
from Profile.models import Profile
from post.models import Post, Like
from .forms import PostModelForm, CommentModelForm
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy


# Create your views here.


def post_comment_create_and_list_view(request):
    pst = Post.objects.all()
    profile = Profile.objects.get(user=request.user)

    # post and comment form

    p_form = PostModelForm()
    c_form = CommentModelForm()
    post_added = False

    profile = Profile.objects.get(user=request.user)

    p_form = PostModelForm(request.POST, request.FILES)

    if 'submit_p_form' in request.POST:
        print(request.POST)
        if p_form.is_valid():
            instance = p_form.save(commit=False)
            instance.author = profile
            instance.save()
            p_form = PostModelForm()
            post_added = True

    if 'submit_c_form' in request.POST:
        c_form = CommentModelForm(request.POST)
        if c_form.is_valid():
            instance = c_form.save(commit=False)
            instance.user = profile
            instance.post = Post.objects.get(id=request.POST.get('post_id'))
            instance.save()
            c_form = CommentModelForm()

    context = {
        'pst': pst,
        'profile': profile,
        'p_form': p_form,
        'c_form': c_form,
        'post_added': post_added,
    }

    return render(request, 'post/main.html', context)


def like_unlike_post(request):
    user = request.user
    if request.method == "POST":
        post_id = request.POST.get('post_id')
        post_obj = Post.objects.get(id=post_id)
        profile = Profile.objects.get(user=user)

        if profile in post_obj.liked.all():
            post_obj.liked.remove(profile)
        else:
            post_obj.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value == 'Like':
                like.value = 'Unlike'

            else:
                like.value = 'Like'

        else:
            like.value = 'Like'

        post_obj.save()
        like.save()

    return redirect('post:post-view')


class PostDeleteView(DeleteView):
    model = Post
    template_name = 'post/cofirm_del.html'
    success_url = reverse_lazy('post:post-view')

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        obj = Post.objects.get(pk=pk)
        if not obj.author.user == self.request.user:
            messages.warning(self.request, "you can't delete this post")
        return obj


class PostUpdateView(UpdateView):
    form_class = PostModelForm
    model = Post
    template_name = 'post/update.html'
    success_url = reverse_lazy('post:post-view')

    def form_valid(self, form):
        profile = Profile.objects.get(user=self.request.user)
        if form.instance.author == profile:
            return super().form_valid(form)
        else:
            form.add_error(None, "you are not authorized to change the post")
            return super().form_invalid(form)
