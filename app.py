import os
import pandas as pd
import streamlit as st

from utils.parser import extract_text_from_pdf
from utils.preprocess import preprocess_text
from utils.skill_extractor import extract_skills
from utils.similarity import calculate_similarity
from utils.job_parser import extract_job_skills
from utils.matcher import compare_skills
from utils.ranker import rank_candidates
from utils.report_generator import generate_report

# -----------------------------
# Streamlit Page
# -----------------------------

st.set_page_config(
    page_title="HireSense AI",
    page_icon="📄",
    layout="wide"
)

st.title("📄 HireSense AI")
st.subheader("AI Resume Screening & Candidate Ranking System")

# -----------------------------
# Upload Multiple Resumes
# -----------------------------

uploaded_resumes = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# -----------------------------
# Process Resumes
# -----------------------------

if uploaded_resumes:

    candidate_list = []

    # Read Job Description
    job_text, job_skills = extract_job_skills(
        "data/job_description.txt"
    )

    for uploaded_resume in uploaded_resumes:

        resume_path = os.path.join(
            "resumes",
            uploaded_resume.name
        )

        with open(resume_path, "wb") as file:
            file.write(uploaded_resume.getbuffer())

        # Resume Text
        resume_text = extract_text_from_pdf(
            resume_path
        )

        clean_resume = preprocess_text(
            resume_text
        )

        resume_skills = extract_skills(
            clean_resume
        )

        score = calculate_similarity(
            clean_resume,
            job_text
        )

        matched, missing = compare_skills(
            resume_skills,
            job_skills
        )

        candidate_list.append({

            "Candidate": uploaded_resume.name,

            "ATS Score": score,

            "Matched Skills": len(matched),

            "Missing Skills": len(missing),

            "Resume Skills": ", ".join(resume_skills)

        })

    # -----------------------------
    # Ranking
    # -----------------------------

    ranked = rank_candidates(candidate_list)

    st.divider()

    st.header("🏆 Candidate Ranking")

    ranking_df = pd.DataFrame(ranked)

    st.dataframe(
        ranking_df,
        use_container_width=True
    )

    # -----------------------------
    # Best Candidate
    # -----------------------------

    best = ranked[0]

    st.success(
        f"🥇 Best Candidate : {best['Candidate']} ({best['ATS Score']}%)"
    )

    # -----------------------------
    # Progress Bar
    # -----------------------------

    st.subheader("📊 Best Candidate ATS Score")

    st.progress(best["ATS Score"] / 100)

    st.metric(
        "Overall Match",
        f"{best['ATS Score']}%"
    )

    # -----------------------------
    # Generate CSV
    # -----------------------------

    csv_path = "reports/Candidate_Ranking.csv"

    os.makedirs("reports", exist_ok=True)

    ranking_df.to_csv(
        csv_path,
        index=False
    )

    with open(csv_path, "rb") as file:

        st.download_button(

            label="📥 Download Ranking Report",

            data=file,

            file_name="Candidate_Ranking.csv",

            mime="text/csv"

        )
            # -----------------------------
    # Project Statistics
    # -----------------------------

    st.divider()

    st.header("📈 Project Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Total Candidates", len(ranked))

    with col2:
        st.metric("Highest ATS Score", f"{best['ATS Score']}%")

    with col3:
        avg_score = round(ranking_df["ATS Score"].mean(), 2)
        st.metric("Average ATS Score", f"{avg_score}%")

    # -----------------------------
    # Top 3 Candidates
    # -----------------------------

    st.divider()

    st.header("🥇 Top Candidates")

    for i, candidate in enumerate(ranked[:3], start=1):
        st.write(
            f"**{i}. {candidate['Candidate']}** — {candidate['ATS Score']}%"
        )

    # -----------------------------
    # Download Report
    # -----------------------------

    os.makedirs("reports", exist_ok=True)

    report_path = generate_report(
        best["ATS Score"],
        [],
        [],
        best["Resume Skills"].split(", ")
    )

    with open(report_path, "rb") as file:

        st.download_button(
            label="📥 Download ATS Report",
            data=file,
            file_name="ATS_Report.csv",
            mime="text/csv"
        )

    # -----------------------------
    # Download Ranking CSV
    # -----------------------------

    csv_path = "reports/Candidate_Ranking.csv"

    ranking_df.to_csv(csv_path, index=False)

    with open(csv_path, "rb") as file:

        st.download_button(
            label="📥 Download Candidate Ranking",
            data=file,
            file_name="Candidate_Ranking.csv",
            mime="text/csv"
        )