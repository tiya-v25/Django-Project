from celery import shared_task

@shared_task
def print_username(username):
    print(f"Running background task for: {username}")
    return f"Hello {username}, background task done!"
