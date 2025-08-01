# 📝 FastAPI Notes API

A modern, high-performance REST API for managing notes built with FastAPI, SQLAlchemy, and PostgreSQL/SQLite. This project demonstrates full CRUD operations, async endpoints, data validation, and best practices for building production-ready APIs.

## ✨ Features

- **Full CRUD Operations**: Create, Read, Update, and Delete notes
- **Async/Await Support**: High-performance asynchronous endpoints
- **Data Validation**: Robust input validation using Pydantic models
- **Database Integration**: SQLAlchemy ORM with SQLite/PostgreSQL support
- **Auto-Generated Documentation**: Interactive API docs with Swagger UI
- **Type Hints**: Fully typed Python code for better development experience
- **Error Handling**: Comprehensive HTTP exception handling

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Git

### Installation

1. **Clone the repository**
git clone https://github.com/ShantanuN8/notes_api.git
cd fastapi-notes-api


2. **Create and activate virtual environment**

Windows
python -m venv venv
venv\Scripts\activate

macOS/Linux
python3 -m venv venv
source venv/bin/activate

text

3. **Install dependencies**
pip install -r requirements.txt

text

4. **Run the application**
uvicorn main:app --reload

text

5. **Access the API**
- API Documentation: http://127.0.0.1:8000/docs
- Alternative Docs: http://127.0.0.1:8000/redoc
- API Base URL: http://127.0.0.1:8000

## 📚 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/notes/` | Create a new note |
| `GET` | `/notes/{note_id}` | Retrieve a specific note |
| `PUT` | `/notes/{note_id}` | Update a specific note |
| `DELETE` | `/notes/{note_id}` | Delete a specific note |

### Example Requests

**Create a Note**
curl -X POST "http://127.0.0.1:8000/notes/"
-H "Content-Type: application/json"
-d '{"title": "My First Note", "content": "This is the content of my note"}'

text

**Get a Note**
curl -X GET "http://127.0.0.1:8000/notes/1"

text

**Update a Note**
curl -X PUT "http://127.0.0.1:8000/notes/1"
-H "Content-Type: application/json"
-d '{"title": "Updated Note", "content": "Updated content"}'

text

**Delete a Note**
curl -X DELETE "http://127.0.0.1:8000/notes/1"

text

## 🏗️ Project Structure

fastapi-notes-api/
│
├── main.py # FastAPI application and route definitions
├── models.py # SQLAlchemy database models
├── schemas.py # Pydantic models for request/response validation
├── database.py # Database configuration and connection
├── requirements.txt # Python dependencies
├── .gitignore # Git ignore file
├── README.md # Project documentation
└── notes.db # SQLite database (auto-generated)

text

## 🛠️ Technology Stack

- **[FastAPI](https://fastapi.tiangolo.com/)**: Modern, fast web framework for building APIs
- **[SQLAlchemy](https://www.sqlalchemy.org/)**: SQL toolkit and Object-Relational Mapping
- **[Pydantic](https://pydantic-docs.helpmanual.io/)**: Data validation using Python type annotations
- **[Uvicorn](https://www.uvicorn.org/)**: Lightning-fast ASGI server
- **SQLite/PostgreSQL**: Database options for data persistence

## 📖 Learning Objectives

This project covers essential backend development concepts:

- ✅ RESTful API design principles
- ✅ Database modeling and relationships
- ✅ Input validation and error handling
- ✅ Async/await patterns in Python
- ✅ API documentation with OpenAPI/Swagger
- ✅ Environment setup and dependency management
- ✅ Git version control and GitHub workflows

## 🔧 Configuration

### Database Configuration

By default, the application uses SQLite. To switch to PostgreSQL:

1. Update `database.py`:
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/dbname"

text

2. Install PostgreSQL driver:
pip install psycopg2-binary

text

## 🧪 Testing

Access the interactive API documentation at `http://127.0.0.1:8000/docs` to test all endpoints directly from your browser.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- FastAPI documentation and community
- SQLAlchemy ORM documentation
- Pydantic validation library

## 📞 Contact

Your Name - your.email@example.com
Project Link: https://github.com/yourusername/fastapi-notes-api

---

⭐ **If you found this project helpful, please give it a star!** ⭐
Also Create a requirements.txt File
Create another new file called requirements.txt and add:

text
fastapi==0.104.1
uvicorn[standard]==0.24.0
sqlalchemy==2.0.23
pydantic[dotenv]==2.5.0
psycopg2-binary==2.9.9
