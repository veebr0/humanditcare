
from django.db import models
from .encrypt import encrypt, decrypt


# Documentation :
# Field API reference
# https: // docs.djangoproject.com/en/3.1/ref/models/fields/

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

    # Converts a value as returned by the database to a Python object.
    # It is the reverse of get_prep_value().
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return decrypt(value, unique=True, fromdb=True)

    # Converts the value into the correct Python object.
    # It acts as the reverse of value_to_string(), and is also called in clean().
    def to_python(self, value):
        if isinstance(value, EncryptedString):
            return value

        if value is None:
            return value
        return EncryptedString(value)

    # value is the current value of the model’s attribute, and the method should return data
    # in a format that has been prepared for use as a parameter in a query.
    def get_prep_value(self, value):
        if value is None:
            return value
        return value

    # Converts value to a backend-specific value.
    # By default it returns value if prepared = True and get_prep_value() if is False.
    def get_db_prep_value(self, value, connection, prepared=False):
        if value is not None and not isinstance(value, EncryptedString):
            value = EncryptedString(encrypt(value, unique=True))
        return value

    # Same as the get_db_prep_value(), but called when the field value must be saved to the database.
    # By default returns get_db_prep_value().
    def get_db_prep_save(self, value, connection):
        if value is None:
            return value
        return encrypt(value, unique=True)

    # Returns a string naming this field for backend specific purposes.
    # By default, it returns the class name.
    def get_internal_type(self):
        return "CharField"

    # Returns the default django.forms.Field of this field for ModelForm.
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

    # this method is used when get value from a DB
    def from_db_value(self, value, expression, connection):
        if value is None:
            return value
        return decrypt(value)

    # this method is used when you write value into DB
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
