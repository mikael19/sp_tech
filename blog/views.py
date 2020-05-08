from django.shortcuts import render
from django.views import generic
from .models import Post, Comment
from .forms import CommentForm
from django.shortcuts import render, get_object_or_404
from .tracker import track, PAGE_VIEW, FORM_SUBMIT, STRUCT
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
# Create your views here.

def post_list(request):
    """
    View that renders the index.html page, where all the blog posts are listed and paginated.
    input: request
    output: index.html page with post list
    """
    object_list = Post.objects.filter(status=1).order_by('-created_on')
    paginator = Paginator(object_list, 3)  # 3 posts in each page
    page = request.GET.get('page')
    home_url = "http://" + request.META['HTTP_HOST'] + "/"
    if page:
        home_url = "http://" + request.META['HTTP_HOST'] + "/?page=" + page
    # Snowplow event tracker for the page view.
    track(PAGE_VIEW, home_url)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
            # If page is not an integer deliver the first page
        post_list = paginator.page(1)
    except EmptyPage:
        # If page is out of range deliver last page of results
        post_list = paginator.page(paginator.num_pages)
    return render(request,
                  'index.html',
                  {'page': page,
                   'post_list': post_list})


def post_detail(request, slug):
    """
    View that renders a single blog post at a time.
    input: request and blog post slug(url part which identifies a given post)
    output: post_detail.html page with the post text and comments
    """
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    post_url = "http://" + request.META['HTTP_HOST'] + "/" + slug + "/"
    # Snowplow event tracker for the page view.
    track(PAGE_VIEW, post_url)
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
            comment_by_user_count = Comment.objects.filter(email=new_comment.email, post=post).count()
            # Snowplow event tracker for the submission of the comments form (comment creation)
            track(FORM_SUBMIT, "postCommentForm")
            track(STRUCT, ["comment", "additional-comment", None, "comment-by-user", comment_by_user_count])
            # t.track_struct_event("comment", "additional-comment", None, "comment-by-user", comment_by_user_count)
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})