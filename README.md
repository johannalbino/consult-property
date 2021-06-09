
# Consult Property

The purpose of this API is to query a neighborhood and property transaction available in external API.
## Authors

- [@johannalbino](https://www.github.com/johannalbino)

  
## API Reference

#### Search Property

```http
  POST /consult-property/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `neighborhood` | `string` | **Required**. |
| `transaction` | `string` | **Required**. SALE or RENTAL |

#### Verify API

```http
  GET /heart-check
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `id`      | `string` | **Required**. Id of item to fetch |

  
## Installation 

Install project with pipenv

```bash 
  pip install pipenv
  pipenv install # Installation of the requirements Pipfile
  pipenv shell
  python3 app.py
```


Install project with Docker

```bash 
  docker-compose build
  docker-compose run
```
## Running Tests

To run tests, run the following command

```bash
  python test
```

  