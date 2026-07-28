import streamlit as st
from parser import extract_text_from_pdf
from llm import review_resume
from ats import calculate_skill_match, compare_all_roles
from pdf_report import generate_report

st.set_page_config(
    page_title="AI Resume Reviewer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Reviewer")
st.write("Upload your resume and get an AI-powered ATS analysis.")

# -----------------------------
# Job Role Selection
# -----------------------------
job_role = st.selectbox(
    "Select Target Job Role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Generative AI Engineer",
        "Data Scientist",
        "Data Analyst",
        "Python Developer"
    ]
)

# -----------------------------
# Resume Upload
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# -----------------------------
# Resume Analysis
# -----------------------------
if uploaded_file is not None:

    if st.button("Analyze Resume", use_container_width=True):

        with st.spinner("Analyzing Resume..."):

            resume_text = extract_text_from_pdf(uploaded_file)

            ats_result = calculate_skill_match(
                resume_text,
                job_role
            )
            all_role_scores = compare_all_roles(
                 resume_text
            )

            result = review_resume(
                resume_text,
                job_role
            )

        st.success("✅ Analysis Completed!")

        # ============================================
        # ATS SCORE
        # ============================================

        st.subheader("📊 ATS Skill Match")

        st.metric(
            label="Overall Match",
            value=f"{ats_result['score']}%"
        )

        st.progress(ats_result["score"] / 100)

        if ats_result["score"] >= 80:
            st.success("Excellent ATS Match")

        elif ats_result["score"] >= 60:
            st.warning("Good ATS Match")

        else:
            st.error("Low ATS Match. Improve your resume by adding the missing skills.")

        st.divider()

        # ============================================
        # Skills Section
        # ============================================

        col1, col2 = st.columns(2)

        with col1:

            st.divider()

            st.subheader("📊 Resume Match Across Roles")

            for role, score in all_role_scores.items():

                st.write(f"**{role}**")

                st.progress(score / 100)

                st.write(f"{score}% Match")
            
            st.subheader("✅ Skills Found")

            if ats_result["found"]:

                for skill in ats_result["found"]:
                    st.success(skill)

            else:
                st.info("No matching skills found.")

        with col2:

            st.subheader("❌ Missing Skills")

            if ats_result["missing"]:

                for skill in ats_result["missing"]:
                    st.error(skill)

            else:
                st.success("No missing skills.")

        st.divider()

        # ============================================
        # AI ANALYSIS
        # ============================================

        st.subheader("🤖 AI Resume Analysis")

        st.markdown(result)
        generate_report(
            "ATS_Report.pdf",
            job_role,
            ats_result,
            result
        )

        with open("ATS_Report.pdf", "rb") as file:

            st.download_button(
                label="📥 Download ATS Report",
                data=file,
                file_name="ATS_Report.pdf",
                mime="application/pdf"
            )
    