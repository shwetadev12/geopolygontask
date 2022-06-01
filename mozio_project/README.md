# geopolygontask

## Project Setup:
First take clone from repository given below:


Install python 3.8 or any latest version of python and Intall python3 virtual environment.

Create Virtual Environment:
```
python3 -m venv mozio_env
```

Activate Virtual Environment:
```
source mozio_env/bin/activate
```

Run Requirements
```
pip install -r requirements.txt 
```

Run Server:
```
python manage.py runserver
```

Run Migrations:
```
python manage.py makemigrations
python manage.py migrate
```

ReRun Server:
```
python manage.py runserver
```

### Create New Provider
URL:
http://127.0.0.1:8000/api/provider/create

Method: POST

Payload:
``` 
{
    "name": "mozio provider",
    "email": "mozioprovider@gmail.com",
    "phone_number": "+919854356345",
    "language": "English",
    "price": "7534",
    "price_currency": "USD"
}
```

### Get Provider using id
URL:
http://127.0.0.1:8000/api/provider/1

Method: GET

Response: 
```
{
    "id": 1,
    "name": "mozio provider",
    "email": "mozioprovider@gmail.com",
    "phone_number": "+919854356345",
    "language": "English",
    "price": "7534.00",
    "price_currency": "USD"
}
```

### Update Provider using id
URL:
http://127.0.0.1:8000/api/provider/update/1

Method: PUT

Payload: 
```
{
    "name": "mozio provider",
    "email": "mozioprovider@gmail.com",
    "phone_number": "+919854356345",
    "language": "Urdu",
    "price": "6324",
    "price_currency": "USD"
}
```

### Delete Provider using id
URL:
http://127.0.0.1:8000/api/provider/delete/1

Method: DELETE
Response:
```
HTTP 204 No Content
```

### Create New Service Area/Polygon
URL:
http://127.0.0.1:8000/api/service-area/create

Method: POST

Payload:
```
{
    "provider": 1,
    "polygon_name": "US Polygon",
    "polygon" : "{'type': 'Polygon', 'coordinates': [[[-128.917074,38.803008],[-122.137625,39.656880],[-118.298157,40.235316],[-112.670431,40.761033],[-110.177711,40.653055],[-107.155697,40.642007],[-103.192299,40.430138],[-98.168302,40.363524],[-94.831304,40.479175],[-84.913828,39.466651],[-81.380660,39.188551],[-77.811560,38.872542],[-72.006956,38.101733],]]}"
}
```

### Get Polygon/service-area using id
URL:
http://127.0.0.1:8000/api/service-area/1

Method: GET

Response: 
```
{
    "id": 1,
    "provider": 1,
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-128.917074,38.803008],[-122.137625,39.656880],[-118.298157,40.235316],[-112.670431,40.761033],[-110.177711,40.653055],[-107.155697,40.642007],[-103.192299,40.430138],[-98.168302,40.363524],[-94.831304,40.479175],[-84.913828,39.466651],[-81.380660,39.188551],[-77.811560,38.872542],[-72.006956,38.101733],]]}",
    "polygon_name": "US Polygon"
}
```

### Update Provider using id
URL:
http://127.0.0.1:8000/api/service-area/1

Method: PUT

Payload: 
```
{
    "provider": 1,
    "polygon": "{'type': 'Polygon', 'coordinates': [[[-128.917074,38.803008],[-122.137625,39.656880],[-118.298157,40.235316],[-112.670431,40.761033],[-110.177711,40.653055],[-107.155697,40.642007],[-103.192299,40.430138],[-98.168302,40.363524],[-94.831304,40.479175],[-84.913828,39.466651],]]}",
    "polygon_name": "US Polygon Update"
}
```

### Delete Provider using id
URL:
http://127.0.0.1:8000/api/service-area/delete/1

Method: DELETE
Response:
```
HTTP 204 No Content
```


### GET POLYGON Using LAT and LNG
URL:
http://127.0.0.1:8000/api/polygon?lat=-128.917074&lng=38.803008

Method: GET
Response:
```

```
