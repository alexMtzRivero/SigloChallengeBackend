# :globe_with_meridians: Siglo coding Challenge
Small coding task to complete the interview process for [Siglo](https://www.siglo.com)

⚠ This repository is the backend part of a full stack task, to have the full project running also clone [this repo](https://github.com/alexMtzRivero/SigloCallengeFrontend) 
### Getting started

create the file "sigloChallenge/.env" with the credentials for your mysql, the file should look like the following: 
```
DB_USER="root"
DB_PASSWORD="yourSuperSecretPassword"
DB_HOST="127.0.0.1"
DB_PORT="3306"
```

then just run the clean-run command

`make clean-run `

This command will: 
- install the requirements
- create a DB for the project
- run migrations
- start the django application 

if you have done the setup before just run 

`make run`

