from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from . import models
from . import forms

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class BlogCreateView(View):
    template_name = 'blogger/blog_create.html'

    def get(self, request, *args, **kwargs):
        form = forms.BlogModelForm()

        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = forms.BlogModelForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return JsonResponse({"status":"success", "redirect_url":"/blog/read/%s"%(obj.id)})
        else:
            return JsonResponse({"status":"failure", "message": ""})

@method_decorator(login_required, name='dispatch')
class BlogListView(View):
    template_name = 'blogger/blog_list.html'

    def get(self, request, *args, **kwargs):
        blogs = models.Blog.objects.filter(author=request.user)
        #for blog in blogs:
        #    blog.content = blog.content[:200]
        return render(request, self.template_name, {'blogs': blogs})

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class BlogEditView(View):
    template_name = 'blogger/blog_edit.html'

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(models.Blog, id=kwargs['pk'])
        form = forms.BlogModelForm(instance=obj)
        return render(request, self.template_name, {'form': form, 'blog_id': kwargs['pk']})

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(models.Blog, id=kwargs['pk'])
        form = forms.BlogModelForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return JsonResponse({"status":"success", "redirect_url":"/blog/read/%s"%(kwargs['pk'])})
        else:
            return JsonResponse({"status":"failure", "message": ""})

@method_decorator(csrf_exempt, name='dispatch')
@method_decorator(login_required, name='dispatch')
class BlogDeleteView(View):

    def post(self, request, *args, **kwargs):
        obj = get_object_or_404(models.Blog, id=request.POST.get("blog_id"))
        obj.delete()
        return JsonResponse({"status":"success", "redirect_url":"/blogs"})

@method_decorator(login_required, name='dispatch')
class BlogDetailView(View):
    template_name = 'blogger/blog_read.html'

    def get(self, request, *args, **kwargs):
        obj = get_object_or_404(models.Blog, id=kwargs['pk'])
        comments = obj.comment_set.all()
        return render(request, self.template_name, {'blog': obj, 'comments': comments})

@method_decorator(login_required, name='dispatch')
class BlogAddCommentView(View):

    def post(self, request, *args, **kwargs):
        if request.POST.get('comment'):
            comment = models.Comment(
                        blog_id = kwargs['pk'],
                        content = request.POST.get('comment'),
                        commenter = request.user
                    )
            comment.save()
        return HttpResponseRedirect('/blog/read/%s'%(kwargs['pk']))

