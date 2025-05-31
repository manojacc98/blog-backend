#  Blog Backend (Django + MySQL)

This is the backend API for the Blog Application built using **Django** and **Django REST Framework**,
 with **JWT authentication** and **MySQL** as the database.

---

##  Features

- User Registration & Login (with JWT auth)
- Create, Read, Update, Delete (CRUD) for blogs
- Authenticated endpoints for user-specific blogs
- Public access to view blog list and details
- Pagination for public blog listing
- Slug-based blog URLs
- CORS enabled for frontend integration

---

##  Tech Stack

- **Python 3.11**
- **Django**
- **Django REST Framework**
- **MySQL** (hosted on Railway or local)
- **JWT Authentication** via `SimpleJWT`
- **CORS Handling** via `django-cors-headers`

---

## ️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/manojacc98/blog-backend
cd blog-backend

2. Create and activate virtual environment
python3 -m venv env
source env/bin/activate   # Mac/Linux
env\Scripts\activate      # Windows

3. Install dependencies
pip install -r requirements.txt

4. Create .env file
Create a .env file in the root directory and add:

DB_NAME=your_db_name
DB_USER=your_username
DB_PASSWORD=your_password
DB_HOST=your_host_url
DB_PORT=3306
SECRET_KEY=your_django_secret

5. Apply migrations

python manage.py migrate

6. Run the server
python manage.py runserver

 API Endpoints

Method	Endpoint	Description
POST	/api/register/	Register new user
POST	/api/login/	Login user (returns JWT tokens)
GET	/api/blog/	List all public blogs
GET	/api/blog/:slug/	Retrieve single blog detail
POST	/api/blog/	Create blog (auth required)
PUT	/api/blog/:slug/	Update blog (author only)
DELETE	/api/blog/:slug/	Delete blog (author only)
GET	/api/my-blogs/	Get blogs created by user
GET	/api/get_user_info/	Get current logged-in user info

 Setup Notes
Ensure CORS is enabled for the frontend domain.

Use .env to store all secret and database credentials.

JWT token should be stored in localStorage on the frontend and sent in the Authorization header.

##  Deployment

- **Backend**: Currently running on localhost during development.
               Ready for deployment to cloud platforms such as **AWS EC2**, **Render**,
               or **Railway** if needed.

- **Database**:  Hosted on **Railway (Cloud-based MySQL)** to meet the cloud hosting requirement.

          Note:  While the backend server is currently running locally,
                 the project is structured and ready to be deployed on any cloud platform.
                 Environment variables are managed via `.env` for easy deployment transition.


Author
Developed by: manoj
Email: r.manojacc@gmail.com
GitHub: https://github.com/manojacc98/blog-backend
