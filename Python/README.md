School Idol API - OAuth Example
===

A simple website that connects to the [School Idol API](http://schoolido.lu/api/) using OAuth and show the logged in user and their accounts.

To use it, you'll need an OAuth ID and secret. Contact the School Idol Tomodachi staff to get them:

- Using direct messages on Twitter: [@schoolidolapi](https://twitter.com/schoolidolapi/)
- By email: [contact@schoolido.lu](mailto:contact@schoolido.lu)

Try it
---

```shell
# 1. Install Python & virtualenv
apt-get install libpython-dev libffi-dev python-virtualenv
# 2. Clone the repo
git clone https://github.com/SchoolIdolTomodachi/SchoolIdolAPIOAuthExample.git && cd SchoolIdolAPIOAuthExample/Python/
# 3. Create a virtualenv
virtualenv env && source env/bin/activate
# 4. Install python packages
pip install requests django
# 5. Edit the OAuth settings with your ID and secret
$EDITOR settings.py
# 6. Start the server on http://localhost:8000/
python manage.py runserver
```
