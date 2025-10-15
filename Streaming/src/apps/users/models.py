"""
Custom user model for Streaming project.
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user', 'User'
    MODERATOR = 'moderator', 'Moderator'
    ADMIN = 'admin', 'Admin'


class User(AbstractUser):
    """Custom user extending AbstractUser.

    Adds display_name, bio, avatar_url, is_verified and role.
    """

    display_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self) -> str:  # pragma: no cover - trivial
        return self.get_full_name() or self.username
