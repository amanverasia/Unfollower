import os
import json
import time
from datetime import datetime
from instagrapi import Client
import getpass

def get_user_credentials():
    username = input("Enter your Instagram username: ")
    password = getpass.getpass("Enter your Instagram password: ")
    return username, password

def load_followers(client, username):
    user_id = client.user_id_from_username(username)
    followers = client.user_followers(user_id)
    return {user.username: user.full_name for user in followers.values()}

def compare_followers(old_followers, new_followers):
    gained = set(new_followers.keys()) - set(old_followers.keys())
    lost = set(old_followers.keys()) - set(new_followers.keys())
    return gained, lost

def save_followers(followers, target_username):
    folder_path = os.path.join(os.getcwd(), target_username)
    os.makedirs(folder_path, exist_ok=True)
    file_path = os.path.join(folder_path, 'followers.json')
    with open(file_path, 'w') as f:
        json.dump(followers, f)

def load_saved_followers(target_username):
    folder_path = os.path.join(os.getcwd(), target_username)
    file_path = os.path.join(folder_path, 'followers.json')
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            return json.load(f)
    return {}

def print_changes(gained, lost, new_followers):
    print(f"Followers gained ({len(gained)}):")
    for username in gained:
        print(f"- {username} ({new_followers[username]})")
    
    print(f"\nFollowers lost ({len(lost)}):")
    for username in lost:
        print(f"- {username}")

def run_check(client, username, target_username):
    old_followers = load_saved_followers(target_username)
    new_followers = load_followers(client, target_username)
    
    gained, lost = compare_followers(old_followers, new_followers)
    print_changes(gained, lost, new_followers)
    
    save_followers(new_followers, target_username)
    print(f"\nCheck completed at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

def main():
    username, password = get_user_credentials()
    
    client = Client()
    try:
        client.login(username, password)
    except Exception as e:
        if "two-factor authentication" in str(e).lower():
            otp = input("Enter the OTP sent to your device: ")
            client.login(username, password, verification_code=otp)
        else:
            raise e
    
    print("Login successful!")
    
    target_username = input("Enter the Instagram username to track: ")
    interval = input("Enter the interval in minutes for automatic checks (leave blank for a single check): ")
    
    if interval:
        interval = int(interval)
        print(f"Running automatic checks every {interval} minutes. Press Ctrl+C to stop.")
        while True:
            run_check(client, username, target_username)
            time.sleep(interval * 60)
    else:
        run_check(client, username, target_username)

if __name__ == "__main__":
    main()