# IntermittentServiceProvider
Python app to monitor ping

The code comprises two elements, a script to ping www.google.com (default packet size of 10) and add the data to 
a sqlite database called `data.db`. This needs to be created using the `create_tables.sql script`. The second component
is a Flask app which hosts a chart to display the data.

###Prerequistes###
Installations:
* sqlite3 (add to path on windows)
* python
* Some way of repeating tasks (CRON, task scheduler)

Python libraries:
* flask
* ping
* statistics
* sqlite3

Install python packages with 'pip install flask' etc.

Prepare the database by running `sqlite3 data.db < create_tables.sql` at the top level.

Prepare a cron job or scheduled task to run `collect_data.py` periodically, I run it once a minute. Note that this has
to be run by an administrator account to access sockets. Use `sudo crontab -e` to add the job to the root account.
