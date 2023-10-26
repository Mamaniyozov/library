 Endpoints

| Method | Endpoint | Description |
| --- | --- | --- |
| GET | /api/users | Returns an array of all users |
| GET | /api/users/:id | Returns a user object with the specified id |
| POST | /api/create-user/ | Creates a new user |
| POST | api/login-user | Logs in a user |
| GET | /api/books | Returns an array of all books |
| POST | /api/create-book/ | Creates a new book |
| POST | /api/update_book/:id | Updates a post with the specified id |
| POST | /api/delete-book/:id | Deletes a post with the specified id |
| GET | /api/books/:id | Returns a post object with the specified id |

## User Object

| Key | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for the user |
| username | String | Username of the user |
| password | String | Password of the user |

## Book Object

| Key | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for the book |
| title | String | Title of the post |
| content | String | Content of the user|
| publication_date | String | Date of publication of the book|
| author | Integer | Author of the book |
| created_at | String | Date of creation of the book |
| updated_at | String | Date of last update of the book |

## Reaction Object

| Key | Type | Description |
| --- | --- | --- |
| id | Integer | Unique identifier for the reaction |
| post | Integer | Post that the reaction belongs to |
| user | Integer | User that the reaction belongs to |
| like | Boolean | Whether the reaction is a like or not |

# API Documentation

## Users

### Get all users

Returns an array of all [user objects](#user-object).

**URL** : `/api/users`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Response**

```json
[
    {
        "id": 1,
        "username": "user1",
        "password": "password1"
    },
    {
        "id": 2,
        "username": "user2",
        "password": "password2"
    }
]
```

### Get a user

Returns a [user object](#user-object) with the specified id.

**URL** : `/api/users/:id`

**Method** : `GET`

**Auth required** : NO

**Permissions required** : None

**Response**

```json
{
    "id": 1,
    "username": "user1",
    "password": "password1"
}
```

### Create a user

Creates a new user.

**URL** : `/api/create-user/`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Request data**

```json
{
    "username": "[username in string format]",
    "password": "[password in string format]"
}
```

**Response data**

```json
{
    "username": "user1",
    "password": "password1"
}
```

### Login a user

Logs in a user.

**URL** : `/api/login-user`

**Method** : `POST`

**Auth required** : NO

**Permissions required** : None

**Request data**

```json
{
    "username": "[username in string format]",
    "password": "[password in string format]"
}
```

**Response data**

```json
{
    "token": "[token]"
}
```
