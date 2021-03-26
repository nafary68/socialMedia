from django.db import models
from account.models import MyUser
from django_extensions.db.fields import AutoSlugField
from django.urls import reverse


class Post(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
	title = models.CharField(max_length=100)
	body = models.TextField(max_length=500)
	slug = AutoSlugField(populate_from=['title'], unique=True)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user} - {self.title}'


	def likes_count(self):
		return self.plike.count()

	def user_can_like(self, user):
		user_like = user.ulike.all()
		qs = user_like.filter(post=self)
		if qs.exists():
			return True
		return False


class Comment(models.Model):
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ucomment')
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='pcomment')
	reply = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='rcomment')
	is_reply = models.BooleanField(default=False)
	body = models.TextField(max_length=400)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'{self.user} - {self.body[:30]}'

	class Meta:
		ordering = ('-created',)


class Like(models.Model):
	post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='plike')
	user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='ulike')

	def __str__(self):
		return f'{self.user} liked {self.post}'