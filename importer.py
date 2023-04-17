import json
import os
import sys
import django

sys.path.append('/var/www/askbot/askbot_site')  # Replace with the path to your project directory
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askbot_site.settings')  # Replace with your project's settings module name
django.setup()

from askbot.models import Thread, Post, User
from askbot.models.post import PostManager

# Replace with the path to your JSON data file
json_file_path = 'example.json'

with open(json_file_path, 'r') as f:
    data = json.load(f)

# ... previous import statements ...

for item in data['items']:
    fields = item['fields']
    print(fields)
    author = User.objects.get(username="harut") # the registered user name

    thread = Thread(title=f"Sample question from_file123", last_activity_by=author)
    thread.save()

    question_post_data = fields['question_post']
    postManager = Post.objects # PostManager class that is used to create posts and answers
    
    post = postManager.create_new(post_type='question',
                  thread=thread,
                  author=author,
                  text=question_post_data['text'],
                  added_at=question_post_data['added_at'],
                  )
    post.score = question_post_data['score']
    post.save()
    answer_post_data = fields['answer_post']
    postManager.create_new_answer(thread=thread,
                         author=author,
                         text=answer_post_data["text"],
                         added_at=answer_post_data["added_at"])
    
    thread.update_tags("tag1, tag2, tag3", user=author)
    thread.save()
