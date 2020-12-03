from django.shortcuts import render, HttpResponse, render

# Create your views here.
def root(req):
    return redirect('/blogs')

def index(req):
    return HttpResponse("Placeholder to display all blogs!")

def showBlog(req, blog_id):
    print(blog_id)
    return HttpResponse(f"Placeholder to display one blog!! ID: {blog_id}")