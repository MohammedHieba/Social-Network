from django.db import models
from accounts.models import User
from groups.models import Group


class PostQuerySet(models.query.QuerySet):
    def get_active_users_posts(self):
        return self.filter(author__is_active=True)

    def get_user_group_posts(self, user: User):
        return self.filter(group__in=user.group_set.all())

    def get_group_posts(self, group: Group):
        return self.filter(group=group)

    def get_friends_posts(self, user):
        return self.filter(author__in=user.friends.all())

    def get_user_posts(self, user):
        return self.filter(author=user)

    def get_group_wall_posts(self, user):
        return self.get_user_group_posts(user).union(self.get_friends_posts(user)).union(self.get_user_posts(user))


class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)

    def get_group_posts(self, group):
        return self.get_queryset().get_active_users_posts().get_group_posts(group).order_by('-created_at')

    def get_user_posts(self, user):
        return self.get_queryset().get_active_users_posts().get_user_posts(user).order_by('-created_at')

    def get_user_wall_posts(self, user):
        return self.get_queryset().get_active_users_posts().get_group_wall_posts(user).order_by('-created_at')


class Post(models.Model):
    class Meta:
        ordering = ('-created_at',)

    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='dislikes')

    objects = PostManager()

    def __str__(self):
        return f"{self.author} author | {self.created_at} created_on | body {self.body} "


class Comment(models.Model):
    class Meta:
        ordering = ('-created_at',)

    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, blank=True, related_name='comment_likes')
    dislikes = models.ManyToManyField(User, blank=True, related_name='comment_dislikes')

    def __str__(self):
        return f"{self.author} author | {self.created_at} created_at | post {self.post} | comment {self.comment} "
