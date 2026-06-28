import os
import pandas as pd


def generate_report(score, matched, missing, resume_skills):

    os.makedirs("reports", exist_ok=True)

    report = pd.DataFrame({
        "ATS Score (%)": [score],
        "Matched Skills": [", ".join(matched)],
        "Missing Skills": [", ".join(missing)],
        "Resume Skills": [", ".join(resume_skills)]
    })

    report_path = "reports/ATS_Report.csv"

    report.to_csv(report_path, index=False)

    return report_path