# Create your views here.


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from core.models import Topic, Post
from datetime import datetime


def index(request):
    latest_topics = Topic.objects.order_by('-pub_date')

    output = {
        'latest_topics': latest_topics,
    }

    return render(request, 'core/index.html', output)


def topic(request, topic_id):
    displayed_topic = get_object_or_404(Topic, pk=topic_id)
    displayed_post = Post.objects.filter(topic=topic_id).order_by('pub_date')
    return render(request, 'core/topic.html', {'topic': displayed_topic,
                                               'post_list': displayed_post,
    })


def reply(request, topic_id):
    displayed_topic = get_object_or_404(Topic, pk=topic_id)
    displayed_posts = Post.objects.filter(topic=topic_id).order_by('pub_date')
    newreply_content = request.POST['reply_content']
    if not newreply_content:
        error = "Please enter text"
        return render(request, 'core/topic.html', {'topic': displayed_topic,
                                                   'post_list': displayed_posts,
                                                   'error_message': error,
        })
    else:
        newreply = Post(author=displayed_posts[0].author, topic=displayed_topic, content=newreply_content,
                        pub_date=datetime.now())
        newreply.save()
        return HttpResponseRedirect(reverse('core:topic', args=topic_id))

