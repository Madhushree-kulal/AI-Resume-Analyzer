import streamlit as st
import pdfplumber
import re

st.set_page_config(
    page_title="AI Resume Analyzer",
    layout="wide"
)

st.markdown("""
<style>
.stApp{
    background-color:#0E1117;
    color:white;
}

h1,h2,h3{
    color:#BB86FC;
}
div[data-testid="stmetric"]{
    background:#1B1F2A;
    padding:15px;
    border-radius:15px;
    border:1px solid #BB86FC;
}
textarea{
    background:#1B1F2A !important;
    color:white !important;
}
.stButton>button{
    background:#BB86FC;
    color:white;
    border-radius:10px;
}
.stProgress > div > div > div {
    background-color:#BB86FC;
}
.card{
    background-color:#1B1F2A;
    padding:20px;
    border-radius:18px;
    border:1px solid #BB86FC;
    margin-bottom:20px;
    box-shadow:0px 0px 15px rgba(187,134,252,0.3);
}
</style> 
""",unsafe_allow_html=True)

st.markdown("""<h1 style='text-align:center;color:#BB86FC;font-size=48px;'>🤖 AI Resume Analyzer 🚀</h1>
            <p style='text-align:center;color=white;font-size=18px;'>Upload your resume and get instant AI feedback!🗒️⭐</p>""",unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div style="
    text-align:center;
    padding:20px;
    background:#1B1F2A;
    border-radius:15px;
    border:1px solid #BB86FC;
    margin-top:20px;
    ">

    <h3 style="color:#BB86FC;">🤖 AI Resume Analyzer</h3>

    <p style="color:white;">
    Made with ❤️ using Python, Streamlit & PDFPlumber
    </p>

    <p style="color:#AAAAAA;">
    © 2026 All Rights Reserved
    </p>

    </div>
    """, unsafe_allow_html=True)
st.info("👋 Welcome! Upload your resume and receive an instant AI-powered analysis with resume score, detected skills, and career recommendations.")
uploaded_file = st.file_uploader(
    "📄 Upload Your Resume (PDF)",
    type=["pdf"],
    help="Upload your resume to get AI analysis."
)
if uploaded_file is not None:

    


    st.success("Resume uploaded successfully")

    st.balloons()

    st.markdown("""<h2 style='text-align:center;
        background:#1B1F2A;
        padding:15px;
        border-radius:12px;
        color:#BB86FC;'>
        📊 Resume Analysis Dashboard
        </h2>
        """, unsafe_allow_html=True)

    with pdfplumber.open(uploaded_file) as pdf:
        text=""

        for page in pdf.pages:
            page_text=page.extract_text()

            if page_text:
                text+=page_text+"\n"

                email=re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2}",text)
                phone=re.findall(r"\d{10}",text)
                name=text.split("\n")[0]

                education=[]
                education_keywords=[
                    "Bachelor",
                    "B.E",
                    "B.Tech",
                    "Engineering",
                    "Master",
                    "M.Tech",
                    "Degree",
                    "University",
                    "College",
                    "Artificial Intelligence",
                    "Machine Learning"
                ]

                for line in text.split("\n"):
                    for keyword in education_keywords:
                        if keyword.lower() in line.lower():
                            if line not in education:
                                education.append(line)
                            break
                
                experience=[]

                experience_keywords=[
                    "Experience",
                    "Work Experience",
                    "Intern",
                    "Internship",
                    "Software Engineer",
                    "Associate Software Engineer",
                    "Developer",
                    "Project",
                    "Worked",
                    "Present",
                    "Company",
                    "Present",
                    "Organization",
                    "Engineer"
                    "Tech"
                ]
                for line in text.split("\n"):
                    line=line.strip()
                    for keyword in experience_keywords:
                        for keyword in experience_keywords:
                            if keyword.lower() in line.lower():
                                if line not in experience:
                                    experience.append(line)
                                break
                


                project_keywords=[
                    "Project",
                    "Projects",
                    "AI Resume Analyzer",
                    "ChatHub",
                    "Expense Tracker",
                    "URL Shortener",
                    "E-Commerce",
                    "Resume Analyzer"
                ]

                projects=[]
                project_section=False

                for line in text.split("\n"):
                    line=line.strip()

                    if "PROJECTS" in line.upper():
                        project_section=True
                        continue

                    if project_section:
                        if "EXPERIENCE" in line.upper() or "EDUCATION" in line.upper():
                            break
                        if line:
                            projects.append(line)
                certifications=[]

                certificate_keywords=[
                    "Certificate",
                    "Certification",
                    "Certified",
                    "Coursera",
                    "Udemy",
                    "NPTEL",
                    "AWS",
                    "Google",
                    "Microsoft",
                    "Cisco"
                ]

                for line in text.split("\n"):
                    line=line.strip()

                    for keyword in certificate_keywords:
                        if keyword.lower() in line.lower():
                            if line not in certifications:
                                certifications.append(line)
                            break



    # st.subheader("📂Projects")

    # if projects:
    #     for project in projects:
    #         st.write("",project)
    # else:
    #     st.write("No projects found")
    
    # st.subheader("📝Certifications")

    # if certifications:
    #     for cert in certifications:
    #         st.write(" ",cert)
    # else:
    #     st.write("No certifications found")


    # st.subheader("💼Experience")

    # if experience:
    #     for exp in experience:
    #         st.write("",exp)
    # else:
    #     st.write("No experinece found")

    # st.subheader("🎓Education")
    # if education:
    #     for edu in education:
    #         st.write(" ",edu)
    # else:
    #     st.write("Education details not found")


    # st.subheader("Candidate Details")
    # st.write("**Name:**",name)

    # if email:
    #     st.write("**Email:**",email[0])
    # if phone:
    #     st.write("**Phone:**",phone[0])

    # # st.subheader("Resume content")
    # st.code(text)

    skills_list=[
        "Python",
        "Java",
        "C++",
        "C",
        "Machine Learning",
        "Deep Learning",
        "HTML",
        "CSS",
        "JavaScript",
        "SQL",
        "Git",
        "React",
        "Node.js",
        "PHP",
        "MongoDB",
        "MySQL"
    ]
    found_skills=[]
    
    for skill in skills_list:
        if skill.lower() in text.lower():
            found_skills.append(skill)
    # st.subheader("Skills Found")
    # if found_skills:
    #     for skill in found_skills:
    #         st.write(" ",skill)
    # else:
    #     st.write("No skills detected")
    # st.subheader("✨Resume Score")
    score=len(found_skills)*10

    if score>100:
        score=100
    # st.write(f"Your Resume Score: {score}/100")
    # st.progress(score/100)

    if score >= 80:
        strength = "🟢 Excellent"
    elif score >= 60:
        strength = "🟡 Good"
    elif score >= 40:
        strength = "🟠 Average"
    else:
        strength = "🔴 Needs Improvement"

    # st.markdown(f"### 💪 Resume Strength: {strength}")
    st.write(f"Skills Detected:{len(found_skills)}")
    st.subheader("💡Suggested Skills")
    missing_skills=[]

    for skill in skills_list:
        if skill not in found_skills:
            missing_skills.append(skill)
    
    col1,col2=st.columns([2, 1])

    with col1:

        st.markdown("## 👤 Candidate Profile")

        st.markdown("""
        <div style="
            background:#1B1F2A;
            padding:20px;
            border-radius:20px;
            border:2px solid #BB86FC;
        ">
        """, unsafe_allow_html=True)

        st.markdown("<h3 style='color:#BB86FC;'>👨‍💻 Resume Details</h3>", unsafe_allow_html=True)

        st.write(f"**👤 Name:** {name}")

        if email:
            st.write(f"**📧 Email:** {email[0]}")

        if phone:
            st.write(f"**📱 Phone:** {phone[0]}")

        st.markdown("###🎓Education")
        for edu in education:
            st.info(edu)

        st.markdown("###💼Experience")
        for exp in experience:
            st.info(exp)

        st.markdown("###📂Projects")
        for project in projects:
            st.info(project)

        st.markdown("###📝Certifications")
        for cert in certifications:
            st.info(cert)

        st.markdown("### 💻 Skills")

        if found_skills:
            for skill in found_skills:
                st.success(skill)
        else:
            st.warning("No skills found")

        st.markdown("</div>", unsafe_allow_html=True)
    with col2:

        st.markdown("## 📊 Resume Analysis")

        st.markdown("""
        <div style="
            background:#1B1F2A;
            padding:20px;
            border-radius:20px;
            border:2px solid #BB86FC;
        ">
        """, unsafe_allow_html=True)

        st.markdown(f"<h1 style='text-align:center;color:#00FF99;'>{score}/100</h1>",unsafe_allow_html=True)

        st.markdown(
            "<h3 style='text-align:center;color:white;'>Overall Resume Score</h3>",
            unsafe_allow_html=True
        )

        st.progress(score/100)

        st.markdown("### 📊 Breakdown")

        st.write("Skills")
        st.progress(min(len(found_skills)/10, 1.0))

        st.write("Education")
        st.progress(min(len(education)/3, 1.0))

        st.write("Experience")
        st.progress(min(len(experience)/5, 1.0))

        st.write("Projects")
        st.progress(min(len(projects)/5, 1.0))

        st.write("Certifications")
        st.progress(min(len(certifications)/3, 1.0))

        st.markdown("</div>", unsafe_allow_html=True)

        report = f"""
        AI Resume Analyzer Report

        Name: {name}
        Email: {email[0] if email else "Not Found"}
        Phone: {phone[0] if phone else "Not Found"}

        Resume Score: {score}/100

        Skills Found:
        {', '.join(found_skills)}

        Education Found: {len(education)}
        Experience Found: {len(experience)}
        Projects Found: {len(projects)}
        Certifications Found: {len(certifications)}

        Recommended Role:
        """

        if "Machine Learning" in found_skills or "Python" in found_skills:
            report += "AI / ML Engineer"
        elif "HTML" in found_skills or "CSS" in found_skills or "JavaScript" in found_skills:
            report += "Web Developer"
        elif "SQL" in found_skills:
            report += "Data Analyst"
        else:
            report += "Improve Technical Skills"

        st.download_button(
            "📥 Download Resume Report",
            data=report,
            file_name="Resume_Report.txt",
            mime="text/plain"
        )

        st.markdown("### 🎯 Career Recommendation")

        if "Machine Learning" in found_skills or "Python" in found_skills:
            st.success("🤖 AI / ML Engineer")

        elif "HTML" in found_skills or "CSS" in found_skills or "JavaScript" in found_skills:
            st.success("🌐 Web Developer")

        elif "SQL" in found_skills:
            st.success("📊 Data Analyst")

        else:
            st.warning("📚 Learn more technical skills")

        st.subheader("📋Resume Summary")
        st.markdown("</div>",unsafe_allow_html=True)

        st.subheader("🎤 Interview Readiness")

        if score >= 80:
            st.success("✅ Ready for Interviews")

        elif score >= 60:
            st.info("👍 Almost Ready")

        else:
            st.warning("📚 Improve your resume before attending interviews.")

        st.subheader("💡 Resume Improvement Tips")

        tips = []

        if "Python" not in found_skills:
            tips.append("✔ Learn Python")

        if "SQL" not in found_skills:
            tips.append("✔ Add SQL skills")

        if len(projects) < 2:
            tips.append("✔ Add more projects")

        if len(certifications) == 0:
            tips.append("✔ Complete certifications from Coursera, NPTEL or Udemy")

        if len(experience) == 0:
            tips.append("✔ Gain internship or work experience")

        if tips:
            for tip in tips:
                st.warning(tip)
        else:
            st.success("🎉 Excellent Resume! Keep it updated.")

        st.markdown('<div class="card">',unsafe_allow_html=True)

        st.metric("Candidate Name:",name)
        st.metric("💻Skill Found:",len(found_skills))
        st.metric("🎓Education Found:",len(education))
        st.metric("💼Experience Found:",len(experience))
        st.metric("📂Projects Found:",len(projects))
        st.metric("📝Certifications Found:",len(certifications))
        st.metric("⭐Resume Score",f"{score}/100")
        # st.metric(f"**✨Overall Resume Score:**",f"{score}/100")
        st.markdown(f"<h1 style='text-align:center;color:#00FF99;'>{score}/100</h1>",
                    unsafe_allow_html=True)

        st.markdown("</div>",unsafe_allow_html=True)



                