from django.shortcuts import render


def post_list(request):
    return render(request, '../templates/blog_app/post_list.html', {})
