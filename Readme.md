# FlyRank — Automated SEO Audit & Performance Report Generation Pipeline

An asynchronous backend pipeline built with **FastAPI** and **ReportLab** that decouples heavy PDF report generation from the main API request-response cycle.

## 🚀 Key Features

- **Non-blocking API Design:** Uses FastAPI's `BackgroundTasks` to enqueue heavy PDF rendering jobs without blocking HTTP responses.
- **Dynamic Artifact Storage:** Automatically creates, saves, and serves PDF audit reports.
- **SQL Aggregation Logic:** Integrates summary statistics (SEO scores, crawled pages, issues, and backlinks) into structured reports.
- **Artifact Download Endpoint:** Serves generated PDF artifacts via a secure download endpoint using unique job IDs.

---

## 🛠️ Tech Stack & Dependencies

- **Framework:** FastAPI
- **ASGI Server:** Uvicorn
- **PDF Engine:** ReportLab
- **Form/File Support:** Python-Multipart

---

## 💻 Installation & Setup

1. **Clone or Open the Project Directory**
   ```bash
   cd path/to/your/project
   ```

2. **Install Required Libraries**
   ```bash
   pip install fastapi uvicorn reportlab python-multipart
   ```

3. **Directory Structure**
   Ensure your project folder is organized as follows:
   ```text
   .
   ├── FlyRank SEO Audit & Performance/   # Auto-created directory for PDFs
   ├── report_generator.py                # ReportLab PDF logic
   ├── main.py                            # FastAPI app & background tasks
   └── README.md                          # Documentation
   ```

---

## ⚡ Running the Application

Start the local development server using `uvicorn`:

```bash
uvicorn main:app --reload
```

The server will start at `http://127.0.0.1:8000`.

---

## 📍 API Endpoints & Usage

Interactive API documentation (Swagger UI) is available at:
👉 **`http://127.0.0.1:8000/docs`**

### 1. Trigger Report Generation
- **Endpoint:** `POST /api/reports/generate`
- **Description:** Enqueues a report generation job and returns immediately with a tracking ID and download link.
- **Sample Response:**
  ```json
  {
    "status": "Job Enqueued",
    "message": "Report generation has started in the background.",
    "report_id": "61d1",
    "download_url": "/api/reports/download/61d1"
  }
  ```

### 2. Download Report Artifact
- **Endpoint:** `GET /api/reports/download/{report_id}`
- **Description:** Retrieves and downloads the generated PDF file corresponding to the given `report_id`.
- **Response:** PDF Binary File Download (`FlyRank_SEO_Audit_{report_id}.pdf`).

---

## 🛡️ Architecture & Execution Flow

1. **Client Request:** User triggers a `POST` request to `/api/reports/generate`.
2. **Immediate Acknowledgment:** API generates a unique `report_id` (via `uuid`), fetches aggregated stats, registers the PDF job in `BackgroundTasks`, and returns a `200 OK` response.
3. **Background Worker:** `generate_pdf_job` renders the PDF on disk using ReportLab's `canvas`.
4. **Artifact Retrieval:** Client accesses `GET /api/reports/download/{report_id}` to download the completed PDF file.