from db import check_user_exists, create_user


def add_new_users(user_id):
    if not check_user_exists(user_id):
        create_user(user_id)