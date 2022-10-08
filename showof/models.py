from .fields import EncryptedCharField, EncryptedEmailField


class User (AbstractUser):  # Extendind the User django model
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = None
    first_name = EncryptedCharField(max_length=254, default=None, null=True)
    email = EncryptedEmailField('email address', unique=True)
    observation = models.CharField(
        max_length=230,  blank=True, default='ninguna')
    is_account = models.BooleanField(default=False)
    is_signup = models.BooleanField(default=False)
    first_login = models.BooleanField(default=True)
    is_eula = models.BooleanField(default=False)  # End User License Agreement
    # Cliente aceptó Términos y Condiciones
    is_agreeterm = models.BooleanField(default=False)
    password_date = models.DateTimeField(
        null=True, verbose_name="último cambio de clave")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    login_failed = models.PositiveSmallIntegerField(null=True, default=0)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    class Meta:
        db_table = 'auth_user'

    def __str__(self):
        return self.first_name
