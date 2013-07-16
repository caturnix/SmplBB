# Create your views here.


from django.shortcuts import render, get_object_or_404

from core.models import Topic,Post


def index(request):
    latest_topics = Topic.objects.order_by('-pub_date')

    output = {
        'latest_topics': latest_topics,
    }

    return render(request, 'core/index.html', output)


def topic(request, topic_id):
    topic = get_object_or_404(Topic, pk=topic_id)
    post = Post.objects.filter(topic=topic_id).order_by('-pub_date')
    return render(request, 'core/topic.html', {'topic': topic,
                                               'posts_list': post,
                                               })

