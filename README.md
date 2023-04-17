# Qstack Askbot Importer

Askbot Importer is a Python script that imports question and answer data from a JSON file into an Askbot Django-based forum. The data includes the question's text, answer, author, tags, and post creation timestamp. This script can be used to automate the process of adding questions and answers to your Askbot forum. The importer is used at our platform https://qstack.ai.

# Requirements
  Python
  Django
  Askbot (installed and configured)

# Installation
Clone or download the repository containing the script.

Update the script with the path to your Askbot project directory and settings module name:

```
sys.path.append('/var/www/askbot/askbot_site')  # Replace with the path to your project directory
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'askbot_site.settings')  # Replace with your project's settings module name
```

Update the script with the path to your JSON data file:

```
json_file_path = 'example.json'
```

# Usage

Make sure the JSON data file is formatted correctly. It should have the following structure:

```
{
    "items": [
        {
            "fields": {
                "question_post": {
                    "text": "Question text",
                    "added_at": "2022-01-01T00:00:00Z",
                    "score": 1
                },
                "answer_post": {
                    "text": "Answer text",
                    "added_at": "2022-01-01T00:00:00Z"
                }
            }
        },
        ...
    ]
}
```

Run the script:


python askbot_importer.py

The script will read the JSON data, create a new thread for each question and answer pair, and save them to the Askbot database.

# Note
The script currently sets the author of all imported questions and answers to a hardcoded user with the username "harut". Make sure to update the script with the desired author's username or modify the script to dynamically assign authors if needed.

The script also sets the tags of each thread to "tag1, tag2, tag3". Update the script to import tags from the JSON data file or customize the tags as needed.
