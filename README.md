# 📝 Django Blog App

A fully functional **Blog Application** built with **Django** that supports user **registration, login/logout**, and **CRUD operations** (Create, Read, Update, Delete) on blog posts. Each user can manage **only their own posts**, ensuring a personalized blogging experience.

---

## 🚀 Features

- 🔐 **User Authentication**
  - Sign Up, Login, Logout
  - Passwords securely hashed
- 📝 **Post Management**
  - Create, view, edit, and delete blog posts
  - Posts are user-specific: each user sees only their own
- 🗓️ **Timestamps**
  - Posts are automatically time-stamped
- 🌐 **Responsive UI**
  - Styled using Bootstrap for clean and mobile-friendly layout
- 🔄 **Server-Rendered Views**
  - All views rendered on the server using Django templating engine

---

## 📸 Screenshots

| Home Page (Logged In) | Create Post | Edit Post |
|-----------------------|-------------|-----------|
| ![Home](screenshots/home.png) | ![Create](screenshots/create.png) | ![Edit](screenshots/edit.png) |

> 🧠 Note: Add your screenshots in a `screenshots/` folder

---

## 🛠️ Tech Stack

- **Backend**: Django 5.x
- **Frontend**: HTML5, Bootstrap 5
- **Database**: SQLite (default Django DB)
- **Auth**: Django built-in `User` model
- **Templating**: Django Template Language (DTL)

---

## 📁 Project Structure

myblog/
├── accounts/ # Handles registration, login, logout
├── blog/ # Blog app for post CRUD
├── templates/ # Shared HTML templates
├── static/ # Bootstrap and static files
├── db.sqlite3
├── manage.py
└── README.md

---

## ⚙️ Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/django-blog-app.git
cd django-blog-app

# Create virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start development server
python manage.py runserver


👤 User Guide
Sign up for a new account

Log in to your dashboard

Create new blog posts

Edit or delete your posts

Log out when done

🔒 Authentication
All routes for creating, editing, and viewing posts are protected using Django’s @login_required decorator.

Each post is linked to the user who created it via:

python
Copy
Edit
user = models.ForeignKey(User, on_delete=models.CASCADE)
📦 Requirements
Use the following to generate requirements.txt:

bash
Copy
Edit
pip freeze > requirements.txt
Sample (minimal):

text
Copy
Edit
Django>=5.0,<6.0
📌 TODO (Optional Enhancements)
🔍 Add search functionality

🗂️ Add categories/tags

📄 Add pagination

🌙 Dark mode toggle

🧑‍💻 Author
👋 Developed by Your Name

📬 Feel free to reach out for collaboration or feedback!

⭐️ Show your support
If you like this project, don’t forget to ⭐ the repo and share it with your friends.

📃 License
This project is licensed under the MIT License.

---

### ✅ Want me to help you create a `requirements.txt`, or improve your folder structure before publishing?  
Let me know and I’ll guide you before you push it live!
