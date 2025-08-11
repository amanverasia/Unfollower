import os
import getpass
from instagrapi import Client

def get_user_credentials():
    """Prompts the user for their Instagram username and password."""
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    return username, password

def get_non_followers(client, username):
    """
    Returns a list of users that the given user follows but who do not follow back.
    """
    user_id = client.user_id_from_username(username)
    following = client.user_following(user_id)
    followers = client.user_followers(user_id)

    following_pks = set(following.keys())
    follower_pks = set(followers.keys())

    non_follower_pks = following_pks - follower_pks
    return [following[pk] for pk in non_follower_pks]

def unfollow_user(client, user):
    """Unfollows a single user."""
    try:
        client.user_unfollow(user.pk)
        print(f"Unfollowed {user.username} ({user.full_name})")
    except Exception as e:
        print(f"Could not unfollow {user.username}: {e}")

def main():
    """
    Logs into Instagram, gets the list of non-followers, and unfollows them after confirmation.
    """
    session_file = "session.json"
    client = Client()

    try:
        if os.path.exists(session_file):
            client.load_settings(session_file)
            client.login_by_sessionid(client.sessionid)
            print("Login successful from session!")
            username = client.username
        else:
            username, password = get_user_credentials()
            client.login(username, password)
            client.dump_settings(session_file)
            print("Login successful and session saved!")

    except Exception as e:
        if "two-factor authentication" in str(e).lower():
            otp = input("Enter the OTP sent to your device: ")
            username, password = get_user_credentials()
            client.login(username, password, verification_code=otp)
            client.dump_settings(session_file)
            print("Login successful and session saved!")
        else:
            raise e

    non_followers = get_non_followers(client, username)

    if not non_followers:
        print("You have no users to unfollow.")
        return

    print(f"Found {len(non_followers)} users that you follow but they don't follow you back.")
    print("Users to unfollow:")
    for user in non_followers:
        print(f"- {user.username} ({user.full_name})")

    for user in non_followers:
        confirm = input(f"Unfollow {user.username}? (y/n): ")
        if confirm.lower() == 'y':
            unfollow_user(client, user)

    print("Unfollowing process completed.")

if __name__ == "__main__":
    main()
