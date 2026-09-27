import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
Report_Dir="FlyRank SEO Audit & Performance"
os.makedirs(Report_Dir,exist_ok=True)
def generate_pdf_job(report_id:str,seo_score:str,pages_crawled:str,issues_found:int,Backlinks_Detected:str):
    file_path=os.path.join(Report_Dir,f'report_{report_id}.pdf')
    c=canvas.Canvas(file_path,pagesize=letter)
    c.setFont("Helvetica-Bold",18)
    c.drawString(100,500,"FlyRank — Automated SEO Audit Report")
    c.setFont("Helvetica",12)
    c.drawString(40,620,f'Overall SEO Score{seo_score}')
    c.drawString(40,600,f'Total Pages Crawled{pages_crawled}')
    c.drawString(40,590,f'Critical Issues Found{issues_found}')
    c.drawString(40,580,f'Total Backlinks Detected{Backlinks_Detected}')
    c.line(140, 580, 550, 580)
    c.setFont("Helvetica-Oblique", 10)
    c.drawString(100, 610, "Status: Generated via Automated Background Pipeline")
    c.save()
    print(f"[SUCCESS] PDF successfully saved at: {file_path}")
