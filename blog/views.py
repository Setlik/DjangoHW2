from django.conf import settings
from django.core.mail import send_mail
from django.views import generic
from django.urls import reverse_lazy
from .models import Post


class PostListView(generic.ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        post = super().get_object(queryset)
        post.views_count += 1

        if post.views_count == 12:
            self.send_email_notification(post)

        post.save()
        return post

    def send_email_notification(self, post):
        subject = f"Поздравляем! Статья '{post.title}' достигла 100 просмотров!"
        message = f"Поздравляем! Ваша статья '{post.title}' сейчас имеет 100 просмотров."
        recipient_list = ['USER@gmail.com']

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            recipient_list,
            fail_silently=False,
        )


class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']
    success_url = reverse_lazy('post_list')


class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'blog/post_form.html'
    fields = ['title', 'content', 'preview_image', 'is_published']

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.pk})


class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')
