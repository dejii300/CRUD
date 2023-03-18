from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import Post

def user_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='user')
        instance.groups.add(group)
        Post.objects.create(
                user=instance,
                name=instance.username,
                email=instance.email,
        )

post_save.connect(user_profile, sender=User) 