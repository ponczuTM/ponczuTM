import os
import random
import string
import subprocess
import time

def generate_random_string(length=20):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def update_readme_file(file_path, random_string):
    with open(file_path, 'w') as file:
        file.write(random_string)

def git_commit_and_push():
    try:
        subprocess.run(["git", "add", "README_test.md"], check=True)
        subprocess.run(['git', 'commit', '-m', 'README_update'], check=True)
        subprocess.run(['git', 'push'], check=True)
        print("Zmiany zostały pomyślnie wysłane na GitHub.")

    except subprocess.CalledProcessError as e:
        print(f"Coś poszło nie tak z Gitem: {e}")

def run_periodically():
    file_path = "README_test.md"

    if not os.path.exists(file_path):
        print(f"Plik {file_path} nie istnieje. Tworzę nowy plik.")
        open(file_path, 'w').close()

    random_string = generate_random_string()
    update_readme_file(file_path, random_string)
    print(f"Zapisano do pliku: {random_string}")

    git_commit_and_push()


run_periodically()