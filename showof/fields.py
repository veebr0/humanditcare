from django.db import models
from .encrypt import encrypt, decrypt


class EncryptedString (str):
    """A subclass of string so it can be told whether a string is
       encrypted or not (if the object is an instance of this class
       then it must [well, should] be encrypted)."""
    pass


class EncryptedEmailField (models.EmailField):
    description = "Encrypted Email address"

    def __init__(self, *args, **kwargs):
        # max_length=254 to be compliant with RFCs 3696 and 5321
        kwargs.setdefault('max_length', 254)
        super().__init__(*args, **kwargs)
        models.Field.__init__(self, *args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return decrypt(value, unique=True, fromdb=True)

    def to_python(self, value):
        if isinstance(value, EncryptedString):
            return value

        if value is None:
            return value
        return EncryptedString(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return value

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is not None and not isinstance(value, EncryptedString):
            value = EncryptedString(encrypt(value, unique=True))
        return value

    def get_db_prep_save(self, value, connection):
        if value is None:
            return value
        return encrypt(value, unique=True)

    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length}
        defaults.update(kwargs)
        return super(EncryptedEmailField, self).formfield(**defaults)


class EncryptedCharField (models.CharField):
    description = "Encrypted Char address"

    def __init__(self, *args, **kwargs):
        # max_length=254 to be compliant with RFCs 3696 and 5321
        kwargs.setdefault('max_length', 254)
        super().__init__(*args, **kwargs)
        models.Field.__init__(self, *args, **kwargs)

    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return decrypt(value)

    def to_python(self, value):
        if isinstance(value, EncryptedString):
            return value

        if value is None:
            return value
        return EncryptedString(value)

    def get_prep_value(self, value):
        if value is None:
            return value
        return value

    def get_db_prep_save(self, value, connection):
        if value is None:
            return value
        return encrypt(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value is not None and not isinstance(value, EncryptedString):
            value = EncryptedString(encrypt(value))
        return value

    def get_db_prep_save(self, value, connection):

        if value is None:
            return value
        return encrypt(value)

    def get_internal_type(self):
        return "CharField"

    def formfield(self, **kwargs):
        defaults = {'max_length': self.max_length}
        defaults.update(kwargs)
        return super(EncryptedCharField, self).formfield(**defaults)
