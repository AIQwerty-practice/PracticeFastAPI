# ✅ Task Manager: Full-Stack FastAPI & Streamlit

A lightweight, full-stack Task Management application featuring a **FastAPI** REST backend and a **Streamlit** interactive frontend.

## 🏗️ Project Architecture

This project follows a decoupled architecture where the Frontend communicates with the Backend via a RESTful API.

```mermaid
graph LR
    User((User)) <--> Streamlit[Streamlit Frontend]
    Streamlit <-- REST API --> FastAPI[FastAPI Backend]
    FastAPI <--> DB[(In-Memory Store)]
``` 
🛠️ Prerequisites <br> <br>
Python 3.12.x (Required for package compatibility) <br>
Git (For cloning the repository) <br>
🚀 Quick Start Guide <br> <br> <br
1. Clone & Setup Environment <br>
powershell
# Clone the project (or just enter your folder) <br>
cd your-project-folder

# Create a virtual environment using Python 3.12 <br>
python -m venv .venv <br>

# Activate the environment <br>
# On Windows:
.venv\Scripts\activate <br>
# On Mac/Linux: <br>
source .venv/bin/activate <br>

# Install dependencies <br>
pip install -r requirements.txt
Use code with caution.

2. Run the Application <br> <br>
You will need two separate terminals running at the same time: <br><br>
Terminal 1: The Backend (FastAPI) <br>
powershell <br>
uvicorn main:app --reload <br>
Use code with caution. <br>

API URL: http://127.0.0.1/8000/tasks <br>
Interactive Docs (Swagger): http://127.0.0.1/8000/docs <br><br>
Terminal 2: The Frontend (Streamlit) <br>
powershell<br>
streamlit run frontend.py <br>
Use code with caution. <br>

Web UI: Usually opens at http://localhost:8501
📝 API Endpoints <br> <br>
Method	Endpoint	Description <br>
GET	/tasks	List all tasks (includes filters) <br>
POST	/tasks	Create a new task <br>
PATCH	/tasks/{id}	Partially update a task (e.g., mark Done) <br>
DELETE	/tasks/{id}	Remove a task permanently <br>
📂 Project Structure <br> <br>
main.py - FastAPI application logic and Pydantic models. <br>
frontend.py - Streamlit UI and API request handling. <br>
requirements.txt - Project dependencies (FastAPI, Streamlit, Pydantic, etc.). <br>
