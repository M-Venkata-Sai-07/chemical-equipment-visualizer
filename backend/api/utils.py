import pandas as pd
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter

def analyze_csv_file(file):
    df = pd.read_csv(file)

    return {
        "total_records": len(df),
        "avg_flowrate": round(df["Flowrate"].mean(), 2),
        "avg_pressure": round(df["Pressure"].mean(), 2),
        "avg_temperature": round(df["Temperature"].mean(), 2),
        "type_distribution": df["Type"].value_counts().to_dict()
    }

def generate_pdf_report(summary, out_path):
    c = canvas.Canvas(out_path, pagesize=letter)
    c.drawString(50, 750, "Chemical Equipment Report")
    c.drawString(50, 730, f"Total Records: {summary['total_records']}")
    c.drawString(50, 710, f"Average Flowrate: {summary['avg_flowrate']}")
    c.drawString(50, 690, f"Average Pressure: {summary['avg_pressure']}")
    c.drawString(50, 670, f"Average Temperature: {summary['avg_temperature']}")
    c.drawString(50, 650, f"Type Distribution: {summary['type_distribution']}")
    c.save()
