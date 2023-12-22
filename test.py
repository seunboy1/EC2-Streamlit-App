import os
OPENAI_API_KEY= os.environ.get('OPENAI_API_KEY')
REMOTE_HOST= os.environ.get('REMOTE_HOST')
REMOTE_USER= os.environ.get('REMOTE_USER')
print(OPENAI_API_KEY)
print(REMOTE_HOST)
print(REMOTE_USER)