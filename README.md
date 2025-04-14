## 🔧 Configuration

To set up your environment for local development:

1. Locate the `.env.example` file in the root directory.
2. Make a copy of this file and rename it to `.env`.
3. Open the `.env` file and replace the placeholder values with your own:
   - `MAPBOX_TOKEN` – your Mapbox API token
   - `WEATHER_TOKEN` – your weather API token (e.g. OpenWeatherMap)
   - `SECRET_KEY` – a secret key for signing JWTs
   - `ALGORITHM` – your desired JWT algorithm (e.g. HS256)

> **Note:** Never commit your `.env` file to version control.

## ⚙️ Backend Setup Instructions

### 📦 Installing Dependencies (with Conda)

> If you have Anaconda or Miniconda installed, follow these steps to set up the backend environment.  
> If you **don't have Conda**, [download and install Miniconda](https://docs.conda.io/en/latest/miniconda.html) first.

1. Open your terminal and navigate to the project directory.
2. Run the following command to create a new environment with the required dependencies:

```bash
conda env create -f environment.yml
```

### 3. Activate the environment
```bash
conda activate react-backend
```

> If your environment has a different name, replace `react-backend` with your actual environment name from `environment.yml`.

### 4. Run the FastAPI server locally

```bash
uvicorn main:app --reload
```

This will start the backend on `http://localhost:8000`

---

### Helpful commands for running in AWS server

| Description           | Command                              |
| --------------------- | ------------------------------------ |
| Start server          | ```sudo systemctl start uvicorn```   |
| Stop server           | ```sudo systemctl stop uvicorn```    |
| See status of server  | ```sudo systemctl status uvicorn```  |

---

### Alembic commands

| Description                         | Command                                                               |
| ----------------------------------- | --------------------------------------------------------------------- |
| Create tables with message          | ```python -m alembic revision --autogenerate -m "commit message"```   |
| Push table creation files to DB     | ```python -m alembic upgrade head```                                  |

---

## 📦 Export dependencies (optional, if you've added new packages)

```bash
conda env export > environment.yml
```

---

## ✅ API is now live at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---
