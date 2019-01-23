from django.shortcuts import render_to_response, get_object_or_404
from django.core.paginator import Paginator
from .models import Blog, BlogType
from django.conf import settings

blog_number_of_each_page = 5

def blog_list(request):

    blogs_all_list = Blog.objects.all()
    paginator = Paginator(blogs_all_list, settings.BLOG_NUMBER_OF_EACH_PAGE) #每2页进行分页
    page_num = request.GET.get('page', 1)  # 获取url的页面参数
    page_of_blogs = paginator.get_page(page_num)
    currenter_page_num = page_of_blogs.number #获取当前页码
    #获取当前页码前后两页的页码范围
    page_range = list(range(max(currenter_page_num-2, 1), currenter_page_num)) + \
                 list(range(currenter_page_num, min(currenter_page_num+2, paginator.num_pages)+1))
    #加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    #加上首页和页尾
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blog_list.html', context)

def blog_detail(request, blog_pk):
    context = {}
    context['blog'] = get_object_or_404(Blog, pk=blog_pk)
    return render_to_response('blog/blog_detail.html', context)

def blogs_with_type(request, blog_type_pk):
    blog_type = get_object_or_404(BlogType, pk=blog_type_pk)
    blogs_all_list = Blog.objects.filter(blog_type=blog_type)
    paginator = Paginator(blogs_all_list, settings.BLOG_NUMBER_OF_EACH_PAGE)  # 每2页进行分页
    page_num = request.GET.get('page', 1)  # 获取url的页面参数
    page_of_blogs = paginator.get_page(page_num)
    currenter_page_num = page_of_blogs.number  # 获取当前页码
    # 获取当前页码前后两页的页码范围
    page_range = list(range(max(currenter_page_num - 2, 1), currenter_page_num)) + \
                 list(range(currenter_page_num, min(currenter_page_num + 2, paginator.num_pages) + 1))
    # 加上省略号
    if page_range[0] - 1 >= 2:
        page_range.insert(0, '...')
    if paginator.num_pages - page_range[-1] >= 2:
        page_range.append('...')

    # 加上首页和页尾
    if page_range[0] != 1:
        page_range.insert(0, 1)
    if page_range[-1] != paginator.num_pages:
        page_range.append(paginator.num_pages)

    context = {}
    context['blog_type'] = blog_type
    context['blogs'] = page_of_blogs.object_list
    context['page_of_blogs'] = page_of_blogs
    context['page_range'] = page_range
    context['blog_types'] = BlogType.objects.all()
    return render_to_response('blog/blogs_with_type.html', context)