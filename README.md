### python
all of the three lines of code can work
```
python dal.py 'if(1=1,create_time,username)'
python dal.py 'if(1=2,create_time,username)'
python dal.py 'create_time'
```
### go
all of the three lines of code can work
```
go run dal.go 'if(1=1,create_time,username)'
go run dal.go 'if(1=2,create_time,username)'
go run dal.go 'create_time'
```

### flask
all of the three lines of code can work
```
export FLASK_APP='flask'
export FLASK_ENV='development'
flask run
curl http://127.0.0.1:5000/api/list?order_by=if(1=2,username,create_time)
curl http://127.0.0.1:5000/api/list?order_by=if(1=2,create_time,username)
```
