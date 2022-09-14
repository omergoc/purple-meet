# purple-meet
 Purple Meet Project

# Index

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/token | `POST` | { username: 'USERNAME', password:'PASSWORD' } | Token Üretir ve Giriş Yapar |

# User

| Route | HTTP Verb	 | POST body	 | Description	 |
| --- | --- | --- | --- |
| /api/user/me | `GET` | Empty | Kullanıcı Bilgisini Döndürür |
| /api/user/me | `UPDATE` | { "is_superuser": true, "username": "user", "first_name":"first_name", "last_name": "last_name", "email": "email@purplemeet.com", "is_staff": true, "is_active": true, "date_joined": "", "birthday": "", "gender": "MALE", "description": "UNVAM", "image": "/", "facebook": "/", "linkedin": null, "slug": "user", "twitter": "/", "instagram": "/", "youtube": "/", "github": "/", "website": "/", "groups": [], "user_permissions": [] } | Kullanıcı Bilgisini Günceller |
| /api/user/change-password | `POST` | {'old_password':'OLD PASSWORD','new_password':'NEW PASSWORD'} | Şifre Günceller |
