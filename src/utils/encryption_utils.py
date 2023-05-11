import bcrypt


def encrypt_password(password):
    # Generate a salt for bcrypt
    salt = bcrypt.gensalt()

    # Hash the password with bcrypt and the generated salt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)

    # Return the hashed password as a string
    return hashed_password.decode('utf-8')


def decrypt_password(hashed_password, password):
    # Verify the password by checking if it matches the stored hashed password
    is_password_valid = bcrypt.checkpw(
        password.encode('utf-8'), hashed_password.encode('utf-8')
    )

    # Return the result of the password verification as a boolean
    return is_password_valid
