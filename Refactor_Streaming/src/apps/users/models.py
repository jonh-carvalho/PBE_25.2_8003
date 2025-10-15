"""
Custom user model for Refactor_Streaming (Fase1).
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class UserRole(models.TextChoices):
    USER = 'user', 'User'
    MODERATOR = 'moderator', 'Moderator'
    ADMIN = 'admin', 'Admin'


class User(AbstractUser):
    display_name = models.CharField(max_length=150, blank=True)
    bio = models.TextField(blank=True)
    avatar_url = models.URLField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    role = models.CharField(max_length=20, choices=UserRole.choices, default=UserRole.USER)
    # Override related fields to avoid reverse accessor conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='users_user_set',
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='users_user_permissions_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'

    def __str__(self):
        return self.get_full_name() or self.username
