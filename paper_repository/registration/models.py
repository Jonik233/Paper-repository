from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class CustomUserManager(BaseUserManager):
    def create_user(self, email, full_name, institution, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not full_name:
            raise ValueError("Users must have a full name")
        if not institution:
            raise ValueError("Users must have an institution")
        user = self.model(
            email=self.normalize_email(email),
            full_name=full_name,
            institution=institution,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, full_name, institution, password):
        user = self.create_user(
            email=self.normalize_email(email),
            full_name=full_name,
            institution=institution,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user
class CustomUser(AbstractBaseUser):
    email = models.EmailField(_("email address"), unique=True)
    full_name = models.CharField(_("full name"), max_length=150)
    institution = models.CharField(_("institution"), max_length=150)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["full_name", "institution"]

    objects = CustomUserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin
