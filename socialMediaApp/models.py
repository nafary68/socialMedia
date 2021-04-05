from django.db import models
from django.contrib.auth.models import User as DjangoUser


# Create your models here.


class User(models.Model):
    djangoUser = models.OneToOneField(DjangoUser, on_delete=models.CASCADE,
                                  related_name='djangoUserModel')
    phoneNumber = models.CharField(max_length=255)
    firstName = models.CharField(max_length=255, blank=True, null=True)
    lastName = models.CharField(max_length=255, blank=True, null=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    verified = models.BooleanField(default=False)
    loginWithPhoneNumber = models.BooleanField(default=False)

    def __str__(self):
        return self.djangoUser.username


class UserJoin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name="following")
    accept = models.BooleanField()

    def __str__(self):
        return str(self.user) + " follows " + str(self.following)


class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title

    def likes_count(self):
        return self.likePost.count()

    def user_can_like(self, user):
        user_like = user.likeUser.all()
        qs = user_like.filter(post=self)
        if qs.exists():
            return True
        return False


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    body = models.TextField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} - {self.body[:20]}'

    class Meta:
        ordering = ('-created',)


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likePost')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likeUser')

    def __str__(self):
        return f'{self.user} liked {self.post}'
