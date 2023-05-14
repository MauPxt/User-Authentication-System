import bcrypt

from src.utils.encryption_utils import encrypt_password, decrypt_password


class TestEncryptionUtils:
    def test_encrypt_password(self):
        password = 'password123'
        encrypted_password = encrypt_password(password)

        assert bcrypt.checkpw(
            password.encode('utf-8'), encrypted_password.encode('utf-8')
        )

    def test_decrypt_password(self):
        password = 'password123'
        encrypted_password = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt()
        )

        assert (
            decrypt_password(encrypted_password.decode('utf-8'), password)
            is True
        )
