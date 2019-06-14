import props as props
from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from blog.forms import emailsendform
from django.core.mail import send_mail
# Create your views here.
def post_view(request):
    post_list=Post.objects.all()
    paginator=Paginator(post_list,2)
    page_number=request.GET.get('page')
    try:
        post_list=paginator.page(page_number)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
         post_list= paginator.page(1)
    except EmptyPage:
        # If page is out of range
        # Delivery last page of results
        post_list  = paginator.page(paginator.num_pages)
    return  render (request,'blog/post_list.html',{'post_list':post_list})
from blog.forms import commentform


def post_details_view(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                           status='published',
                           publish__year=year,
                           publish__month=month,
                           publish__day=day)
    comments=post.comments.filter(active=True)
    csubmit=False
    if request.method=="POST":
        form=commentform(request.POST)
        if form.is_valid():
            new_comments=form.save(commit=True)
            new_comments.post=Post
            new_comments.save()
            csubmit=True
    else:
        form=commentform()
    return render(request,'blog/post_details.html',{'post':post,'csubmit':csubmit,'comments':comments,'form':form})
from django.views.generic import ListView
class Postlist_view(ListView):
    model=Post
    paginate_by = 1

def email_send_view(request,id):
    post=get_object_or_404(Post,id=id,status='published')
    sent=False
    if request.method=="POST":
        form=emailsendform(request.POST)
        if form.is_valid():
            cd=form.cleaned_data
            subject='{}({}) recomends u to read"{}"'.format(cd['name'],cd['email'],post.tittle)
            # post_url=post.get_absolute_url()
            post_url=request.build_absolute_uri(post.get_absolute_url())
            message='read post at:\n{}\n\n{}\'s comments:\n{}'.format(post_url,cd['name'],cd['comments'])
            send_mail(subject,message,'ravis@blog.com',[cd['to']])
            sent=True

    else:
        form=emailsendform()
    # props.put("mail.smtp.starttls.enable", "true")
    return render(request,'blog/sharebymail.html',{'form':form,'post':post,'sent':sent})

# from django.core.mail import send_mail
# send_mail('haii','gd vening','ravi',['kurvaravi2@gmail.com','ravikurva9@gmail.com'],fail_silently=False)