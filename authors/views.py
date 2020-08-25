from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from mysite.models import user_posts,user_details
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models import Q


@login_required(login_url="/login")
def author_home(request):
    user = request.user
    if request.method == 'POST':
        if request.POST.get('create_new_post'):
            new_post_created = user_posts.objects.create(user_id=user)
            new_post_created.author = user.first_name +' '+ user.last_name
            new_post_created.save()
            return redirect('/login/author/')
        else:
            post_id = request.POST.get('post_id')
            n = user_posts.objects.get(id=post_id)
            n.date_posted = timezone.now()
            if request.POST.get('edit'):
                n.state = request.POST.get('edit')
            elif request.POST.get('defer'):
                n.state = request.POST.get('defer')
            elif request.POST.get('delete'):
                n.state = request.POST.get('delete')
            else:
                if request.POST.get('draft_text'):
                    n.content = request.POST.get('draft_text')
                    n.state = request.POST.get('save')
                else:
                    n.state = request.POST.get('save')
            n.save()
            return redirect('/login/author/')
    else:
        if request.GET.get('view') == 'published':
            resp = user_posts.objects.filter(user_id=user,state='published').order_by('-date_posted')
            state = 'published'
        elif request.GET.get('view') == 'pending':
            resp = user_posts.objects.filter(user_id=user,state='pending').order_by('-date_posted')
            state = 'pending'
        else:
            resp = user_posts.objects.filter(Q(user_id=user, state='draft') | Q(user_id=user, state='saved')).order_by('-date_posted')
            state = 'inprogress'
        context = {'user': user, 'resp': resp, 'state' : state}
        return render(request, 'authors/author.html', context)

def author_logout(request):
    logout(request)
    messages.success(request, 'You have been logged out Successfully!')
    return redirect('/')
