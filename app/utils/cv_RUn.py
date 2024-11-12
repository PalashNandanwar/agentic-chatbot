import fitz  # PyMuPDF

# Function to extract text from PDF
def extract_text_from_pdf(pdf_file):
    doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Function to generate career insights based on resume content
def generate_career_insights(resume_text):
    # Basic keyword-based analysis (can expand with NLP or regex)
    skills = ["Python", "Data Analysis", "Machine Learning", "Project Management", "Data Science", "AI", "Leadership", "Communication", "Cloud Computing",
              "React", "Java", "JavaScript", "Frontend Development", "Backend Development", "Full Stack Development", "DevOps", "Cybersecurity", "SQL", "HTML", "CSS"]
    identified_skills = [skill for skill in skills if skill.lower() in resume_text.lower()]
    
    # Additional insights based on experience or education (this is just a mock-up, can be expanded further)
    experience_keywords = ["years of experience", "experience", "worked at", "leadership", "managed"]
    experience_mentioned = any(keyword.lower() in resume_text.lower() for keyword in experience_keywords)
    
    # Education-related keywords (if applicable)
    education_keywords = ["bachelor", "master", "phd", "university", "degree"]
    education_mentioned = any(keyword.lower() in resume_text.lower() for keyword in education_keywords)

    # Start of the insights message
    insights = "Hello! Based on the information provided in your resume, here are some career insights tailored to your profile:\n\n"
    
    # Provide insights based on the identified skills
    if "Python" in identified_skills:
        insights += "- **Python**: A versatile skill with opportunities in **Data Science**, **Backend Development**, and **Software Engineering**.\n"
        insights += "  To further enhance your profile, consider exploring **Machine Learning** or **Data Engineering**.\n"
    
    if "Data Analysis" in identified_skills:
        insights += "- **Data Analysis**: You are well-positioned for roles like **Data Analyst**, **Business Intelligence Analyst**, or **Data Scientist**.\n"
        insights += "  Additional expertise in **SQL**, **Excel**, and data visualization tools like **Power BI** or **Tableau** could set you apart.\n"
    
    if "Machine Learning" in identified_skills:
        insights += "- **Machine Learning**: A highly sought-after skill. Explore opportunities as a **Machine Learning Engineer**, **Data Scientist**, or **AI Researcher**.\n"
        insights += "  Familiarity with tools like **TensorFlow** or **PyTorch** will increase your marketability.\n"
    
    if "Project Management" in identified_skills:
        insights += "- **Project Management**: If you have leadership experience, roles such as **Project Manager**, **Product Manager**, or **Scrum Master** could be a great fit.\n"
        insights += "  Proficiency in project management tools like **JIRA**, **Asana**, or **Trello** is also recommended.\n"
    
    if "Data Science" in identified_skills:
        insights += "- **Data Science**: With a background in **Data Science**, consider roles like **Data Scientist**, **Quantitative Analyst**, or **Data Engineer**.\n"
        insights += "  Specializing in **Deep Learning** or **Big Data Technologies** could greatly enhance your career prospects.\n"
    
    if "AI" in identified_skills:
        insights += "- **AI**: Roles like **AI Engineer**, **AI Researcher**, or **Automation Engineer** are worth considering.\n"
        insights += "  Further developing expertise in **Natural Language Processing (NLP)** or **Computer Vision** could be highly rewarding.\n"
    
    if "Cloud Computing" in identified_skills:
        insights += "- **Cloud Computing**: A rapidly growing field with roles like **Cloud Engineer**, **Cloud Solutions Architect**, or **DevOps Engineer**.\n"
        insights += "  Knowledge of platforms like **AWS**, **Azure**, or **Google Cloud** will greatly enhance your qualifications.\n"
    
    # React, Java, and other relevant skills
    if "React" in identified_skills:
        insights += "- **React**: As a powerful JavaScript library, consider roles like **Frontend Developer**, **React Developer**, or **Full Stack Developer**.\n"
        insights += "  To further your React expertise, explore **Redux** for state management, **React Router** for routing, and **Next.js** for server-side rendering.\n"
    
    if "Java" in identified_skills:
        insights += "- **Java**: A strong language for **Enterprise Applications**. Roles such as **Java Developer**, **Software Engineer**, or **Backend Developer** would be ideal.\n"
        insights += "  Knowledge of frameworks like **Spring** and **Hibernate**, as well as familiarity with **Microservices** and containerization tools like **Docker**, would be beneficial.\n"
    
    if "JavaScript" in identified_skills:
        insights += "- **JavaScript**: Essential for both **Frontend** and **Backend Development**. Consider roles like **Frontend Developer**, **Backend Developer**, or **Full Stack Developer**.\n"
        insights += "  Learning frameworks like **Vue.js**, **Angular**, or backend technologies like **Node.js** will enhance your JavaScript expertise.\n"
    
    if "Frontend Development" in identified_skills:
        insights += "- **Frontend Development**: Pursue roles such as **Frontend Developer**, **UI Developer**, or **UX/UI Designer**.\n"
        insights += "  Strong knowledge of **HTML**, **CSS**, and frameworks like **React**, **Vue.js**, or **Angular** is essential.\n"
    
    if "Backend Development" in identified_skills:
        insights += "- **Backend Development**: Explore roles like **Backend Developer**, **API Developer**, or **Software Engineer**.\n"
        insights += "  Mastering frameworks like **Node.js**, **Spring Boot**, **Django**, or **Flask** will enhance your backend expertise.\n"
    
    if "Full Stack Development" in identified_skills:
        insights += "- **Full Stack Development**: Well-versed in both frontend and backend, roles like **Full Stack Developer**, **Software Engineer**, or **Technical Lead** would be a great fit.\n"
        insights += "  A balance of **React**, **Node.js**, or **Spring** is key for Full Stack success.\n"
    
    if "DevOps" in identified_skills:
        insights += "- **DevOps**: Critical for streamlining development and deployment. Consider roles like **DevOps Engineer**, **Site Reliability Engineer**, or **Cloud Engineer**.\n"
        insights += "  Knowledge of **CI/CD pipelines**, **Docker**, **Kubernetes**, and cloud platforms like **AWS** or **Azure** would be highly valuable.\n"
    
    if "Cybersecurity" in identified_skills:
        insights += "- **Cybersecurity**: A rapidly growing field with opportunities as a **Security Engineer**, **Penetration Tester**, or **Cybersecurity Analyst**.\n"
        insights += "  Consider gaining certifications like **CISSP** or **CEH** to further your career in cybersecurity.\n"
    
    # Experience-based insights
    if experience_mentioned:
        insights += "\nIt appears you have valuable industry experience. Based on your experience, consider aiming for the following:\n"
        insights += "- For a few years of experience, mid-level positions such as **Senior Developer** or **Lead Data Analyst** could be ideal.\n"
        insights += "- With more extensive experience, roles like **Engineering Manager**, **Data Science Lead**, or **Product Director** might be the next step.\n"
    
    # Education-based insights
    if education_mentioned:
        insights += "\nYour educational background also plays a vital role in your career path:\n"
        insights += "- A **Bachelor’s** or **Master’s Degree** positions you well for entry-level to mid-level roles.\n"
        insights += "- A **PhD** opens doors for research roles or positions in academia.\n"

    # If no specific skills are identified
    if not identified_skills:
        insights += "It seems we couldn't identify any specific skills in your resume. We recommend including more details on your technical and soft skills, such as programming languages, leadership experiences, or domain expertise.\n"
    
    return insights
