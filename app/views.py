from app.models import Blog
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, FormView
from .models import Blog, Comment
from .forms import CommentForm, ContactForm
from django.urls import reverse_lazy

# Create your views here.

class Index(ListView):
    model = Blog
    template_name = 'app/index.html'
    paginate_by = 3


def detail(request, pk):
    obj = Blog.objects.get(pk=pk)
    comments = Comment.objects.filter(blog=obj)
    context = {
        'blog': obj,
        'comments': comments,
    }
    if request.method =='POST':
        if request.POST.get('like_count', None):
            obj.count += 1
            obj.save()
        # like_countのnameが入ったものにpostが実行されたときに
        # countが１増加するようになる

        form = CommentForm(request.POST)
        if form.is_valid():
            text = form.save(commit=False)
            text.blog = obj
            text.save()

        # POSTを受け取った場合,formsのCommentFormを呼び出す
        # htmlのnameとformsの変数があっているのを確認する
        # validationを行って問題なければdbに保存する

    # Blogの個別ページをobjに代入
    # それをcontext内にkey=blog, value:model変数になっている
    # ロードするときは{{blog.title}}で出力可能

    return render(request, 'app/detail.html', context)

    # コメント反映のコピー
    # obj = Blog.objects.get(pk=pk)
    # comments = Comment.objects.filter(blog=obj)
    # context = {
    #     'blog': obj,
    #     'comments': comments,
    # }
    # if request.method =='POST':
    #     form = CommentForm(request.POST)
    #     if form.is_valid():
    #         text = form.save(commit=False)
    #         text.blog = obj
    #         text.save()


class BlogListView(ListView):
    model = Blog
    template_name = 'app/blog_list.html'


class ContactView(FormView):
    template_name = 'app/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy("contact")

    def form_valid(self, form):
        form.send_mail()
        return super().form_valid(form)