# Sweet Shop Management System

A full-stack application for managing a traditional sweet shop inventory.

* **Backend:** Python (FastAPI) + SQLite
* **Frontend:** Vue.js + Tailwind CSS
* **Authentication:** JWT (JSON Web Tokens)

## 🚀 Setup & Installation

### 1. Backend Setup
```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Mac/Linux: source venv/bin/activate

pip install -r requirements.txt
uvicorn main:app --reload
2. Frontend Setup
Open frontend/index.html in your browser.

✅ Features
Authentication: Secure Login/Register with password hashing.

Inventory Control: Logic prevents purchasing items with zero stock.

TDD: Built using Red-Green-Refactor cycles.

UI: Responsive design.

🤖 My AI Usage
Tools Used: Gemini / ChatGPT

How I used them:

Code Scaffolding: I used AI to generate the initial boilerplate for FastAPI, including the standard CRUD operations and Pydantic schemas.

Frontend Development: Used AI to scaffold the Vue.js structure and Tailwind CSS styling to accelerate the UI development process.

Unit Testing: Leveraged AI to brainstorm test cases and generate initial test structures for the TDD cycle.

Reflection:

I treated AI as a "Pair Programmer" to handle repetitive setup tasks and standard code patterns.

This allowed me to focus my effort on verifying the business logic (specifically the purchase/inventory rules) and ensuring the application met the strict TDD requirements.