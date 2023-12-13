from django.shortcuts import render
from .models import Blog_Content,Blog1_Details_conent,Blog1_Details_desc,Blog2_Details_conent,Blog2_Details_desc,Blog3_Details_conent,Latest_Post
from django.shortcuts import render, get_object_or_404

# Create your views here.

def Blog(request):
    blogs = Blog_Content.objects.all()
    return render(request, 'myapp/blog.html', {'blogs':blogs})

def Blog_detail(request, blog_id):
    blog = get_object_or_404(Blog_Content, id=blog_id)
    blog1_details_conent = Blog1_Details_conent.objects.first()
    blog1_details_desc = Blog1_Details_desc.objects.all()
    blog2_details_conent = Blog2_Details_conent.objects.first()
    blog2_details_desc = Blog2_Details_desc.objects.all()
    blog3_details_conent = Blog3_Details_conent.objects.first()
    latest_post = Latest_Post.objects.all()
   
    if blog_id == 1:
        template_name = 'myapp/BlogDetails.html'
    elif blog_id == 2:
        template_name = 'myapp/BlogDetails2.html'
    elif blog_id == 3:
        template_name = 'myapp/BlogDetails3.html'
        
    context = {
        'blog': blog,
        'blog1_details_conent':blog1_details_conent,
        'blog1_details_descs':blog1_details_desc,
        'blog2_details_conent':blog2_details_conent,
        'blog2_details_descs':blog2_details_desc,
        'blog3_details_conent':blog3_details_conent,
        'latest_posts':latest_post
        
    }
        
    return render(request, template_name, context)












