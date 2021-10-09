# Siglo coding Challenge


### Getting started

create the file "sigloChallenge/.env" with the credentals for your mysql 
'''
DB_USER="root"
DB_PASSWORD="yourSuperSecretPassword"
DB_HOST="127.0.0.1"
DB_PORT="3306"
'''

then just run the clean-run command

'''
make clean-run
'''
this command will 
- install the requirements
- create a DB for the project
- run migrations
- start the django application 

if you have done the setup before just run 

'''
make run
'''