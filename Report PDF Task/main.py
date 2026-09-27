import os
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.responses import FileResponse
from report_generator import Report_Dir,generate_pdf_job
import uuid
app = FastAPI(title="Report Generation Pipeline API")
def fetch_aggregated_sql_data():
    return{
        "Overall SEO Score": "90/100",
        "Total Pages Crawled" : "1,250",
        "Critical Issues Found": 5,
        "Total Backlinks Detected":"4,789"
    }
@app.post("/api/report/generate")
def trigger_report_generation(backgroundtasks:BackgroundTasks):
    report_id=str(uuid.uuid4())[:4]
    dbs=fetch_aggregated_sql_data()
    backgroundtasks.add_task(
        generate_pdf_job,
        report_id,
        dbs["Overall SEO Score"],
        dbs["Total Pages Crawled"],
        dbs["Critical Issues Found"],
        dbs["Total Backlinks Detected"]
    )
    return{
        "status": "Job Enqueued",
        "message": "Report generation has started in the background.",
        "report_id": report_id,
        "download_url": f"/api/reports/download/{report_id}"
    }
@app.get("/api/reports/download/{report_id}")
def download_report(report_id:str):
    file_path=os.path.join(Report_Dir,f'report_{report_id}.pdf')
    if not os.path.exists(file_path):
        raise HTTPException(
            status_code=404, 
            detail="Report is still processing or does not exist. Please try again in a few seconds."
        )
    return FileResponse(
        filename=f"FlyRank_SEO_Audit_{report_id}.pdf",
        media_type="application/pdf",
        path=file_path
    )