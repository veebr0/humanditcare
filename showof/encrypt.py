import base64
import logging
import traceback
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from django.conf import settings

from django.core.validators import EmailValidator

backend = default_backend()


def encrypt(txt, unique=False):
    try:
        # convert int an special characters etc to string first
        txt = GetValidText(str(txt))
        # txt = str ( txt )

        if unique:
            EmailValidator(txt)  # this check that that email is valid
            cipher = Cipher(algorithms.AES(
                validkey(settings.ENCRYPT_KEY[0:32])), modes.ECB(), backend=backend)
            encryptor = cipher.encryptor()
            padder = padding.PKCS7(cipher.algorithm.block_size).padder()
            padded = padder.update(txt.encode()) + padder.finalize()
            encrypted_text = base64.urlsafe_b64encode(
                encryptor.update(padded) + encryptor.finalize())
            encrypted_text = encrypted_text.decode("ascii") + '@xyz.zxy'
        else:
            # get the key from settings
            cipher_suite = Fernet(settings.ENCRYPT_KEY)  # key should be byte
            # #input should be byte, so convert the text to byte
            encrypted_text = cipher_suite.encrypt(txt.encode('ascii'))
            # encode to urlsafe base64 format
            encrypted_text = base64.urlsafe_b64encode(
                encrypted_text).decode("ascii")
        return encrypted_text
    except Exception as e:
        # log the error if any
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def decrypt(txt, unique=False, fromdb=False):
    try:
        txt = str(txt)
        EmailValidator(txt)  # this check that that email is valid
        if fromdb:
            subname, domain = txt.split('@', 1)
            ciphertext = subname
        else:
            ciphertext = txt
        if unique:
            cipher_suite = Cipher(algorithms.AES(
                validkey(settings.ENCRYPT_KEY[0:32])), modes.ECB(), backend=backend)
            decryptor = cipher_suite.decryptor()
            unpadder = padding.PKCS7(
                cipher_suite.algorithm.block_size).unpadder()
            padded = decryptor.update(base64.urlsafe_b64decode(
                ciphertext)) + decryptor.finalize()
            decoded_text = (unpadder.update(padded) +
                            unpadder.finalize()).decode("ascii")
        else:
            # base64 decode
            txt = base64.urlsafe_b64decode(txt)
            cipher_suite = Fernet(settings.ENCRYPT_KEY)
            decoded_text = cipher_suite.decrypt(txt).decode("ascii")

        return decoded_text
    except Exception as e:
        # log the error
        logging.getLogger("error_logger").error(traceback.format_exc())
        return None


def validkey(encvar):
    if isinstance(encvar, str):
        return encvar.encode()
    else:
        return encvar


# This function remove all special character into the string passed.
def GetValidText(txt):
    # Definig special characters
    a, b = 'ÁáÉéÍíÓóÚúÜüÑñ', 'AaEeIiOoUuUuÑn'
    # Line bellow create a Dict where a is the key a b is the respective
    # ASCI Code value.
    trans = str.maketrans(a, b)
    # Example:
    # {193: 65, 225: 97, 201: 69, 233: 101, 205: 73, 237: 105, 211: 79, 243: 111, 218: 85, 250: 117, 220: 85, 252: 117, 209: 209, 241: 110}
    new_text = txt.translate(trans)

    return new_text
