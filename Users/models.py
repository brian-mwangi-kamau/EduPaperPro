from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None):
        if not email:
            raise ValueError("You must provide an email!")
        if not first_name:
            raise ValueError("You must provide your last name!")
        if not last_name:
            raise ValueError("You must provide your last name!")

        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.set_password(password)
        user.save(using=self._db)
        UserAccount.objects.create(user=user)
        return user

    def create_superuser(self, first_name, last_name, email, password=None):
        user = self.create_user(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            password=password,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    account_number = models.CharField(max_length=8, unique=True)
    is_subscribed = models.BooleanField(default=False)


    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_joined = models.DateTimeField(auto_now_add=True, null=True)
    last_login = models.DateTimeField(auto_now_add=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, null=True)
    modified_date = models.DateTimeField(auto_now_add=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
    



class UserAccount(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    cash_balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.user.first_name} ({self.user.phone_number})"