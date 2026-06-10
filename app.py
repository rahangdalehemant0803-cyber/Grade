import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="Grade Calculator Pro",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');

html, body, [class*="css"] {
    font-family: 'Poppins', sans-serif;
}

.stApp{
    background: linear-gradient(
    135deg,
    #0f172a,
    #111827,
    #1e293b
    );
}

.main-title{
    text-align:center;
    font-size:55px;
    font-weight:700;
    color:#38bdf8;
}

.subtitle{
    text-align:center;
    color:#cbd5e1;
    font-size:18px;
    margin-bottom:30px;
}

.card{
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    backdrop-filter: blur(12px);
    border:1px solid rgba(255,255,255,0.1);
}

.metric-card{
    background: rgba(255,255,255,0.05);
    padding:20px;
    border-radius:20px;
    text-align:center;
}

.big-number{
    font-size:40px;
    font-weight:bold;
    color:#38bdf8;
}

.badge{
    text-align:center;
    font-size:24px;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------

st.markdown(
"""
<div class='main-title'>
🎓 Grade Calculator Pro
</div>
<div class='subtitle'>
Smart Student Performance Dashboard
</div>
""",
unsafe_allow_html=True
)

# ---------------- SUBJECT INPUT ----------------

st.sidebar.header("📚 Enter Subjects")

num_subjects = st.sidebar.slider(
    "Number of Subjects",
    1,
    15,
    5
)

subjects = []
marks = []

for i in range(num_subjects):

    subject = st.sidebar.text_input(
        f"Subject {i+1}",
        value=f"Subject {i+1}"
    )

    mark = st.sidebar.number_input(
        f"Marks {i+1}",
        min_value=0,
        max_value=100,
        value=75,
        key=i
    )

    subjects.append(subject)
    marks.append(mark)

# ---------------- CALCULATIONS ----------------

avg = round(np.mean(marks),2)

gpa = round(avg / 10,2)

if avg >= 90:
    grade = "A+"
    badge = "🏆 Topper"
elif avg >= 80:
    grade = "A"
    badge = "🌟 Excellent"
elif avg >= 70:
    grade = "B"
    badge = "🔥 Good"
elif avg >= 60:
    grade = "C"
    badge = "👍 Average"
elif avg >= 50:
    grade = "D"
    badge = "⚠️ Needs Work"
else:
    grade = "F"
    badge = "❌ Fail"

# ---------------- METRICS ----------------

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(
        f"""
        <div class='metric-card'>
        <h3>📊 Average</h3>
        <div class='big-number'>{avg}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col2:
    st.markdown(
        f"""
        <div class='metric-card'>
        <h3>🎯 GPA</h3>
        <div class='big-number'>{gpa}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.markdown(
        f"""
        <div class='metric-card'>
        <h3>🏅 Grade</h3>
        <div class='big-number'>{grade}</div>
        </div>
        """,
        unsafe_allow_html=True
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- BADGE ----------------

st.markdown(
f"""
<div class='badge'>
{badge}
</div>
""",
unsafe_allow_html=True
)

# ---------------- DATAFRAME ----------------

df = pd.DataFrame({
    "Subject": subjects,
    "Marks": marks
})

st.markdown("## 📋 Marks Table")

st.dataframe(
    df,
    use_container_width=True
)

# ---------------- CHARTS ----------------

col1, col2 = st.columns(2)

with col1:

    fig1 = px.bar(
        df,
        x="Subject",
        y="Marks",
        color="Marks",
        title="📊 Subject Performance",
        text="Marks"
    )

    fig1.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig1,
        use_container_width=True
    )

with col2:

    fig2 = px.pie(
        df,
        names="Subject",
        values="Marks",
        hole=0.5,
        title="🥧 Marks Distribution"
    )

    fig2.update_layout(
        template="plotly_dark"
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

# ---------------- ANALYSIS ----------------

st.markdown("## 📈 Performance Analysis")

highest_subject = df.loc[df["Marks"].idxmax()]

lowest_subject = df.loc[df["Marks"].idxmin()]

col1, col2 = st.columns(2)

with col1:
    st.success(
        f"🏆 Best Subject: {highest_subject['Subject']} ({highest_subject['Marks']})"
    )

with col2:
    st.warning(
        f"📉 Weak Subject: {lowest_subject['Subject']} ({lowest_subject['Marks']})"
    )

# ---------------- PREDICTION ----------------

prediction = round(
    min(
        100,
        avg + 5
    ),
    2
)

st.info(
    f"🔮 Predicted Next Exam Score: {prediction}"
)

# ---------------- REPORT ----------------

csv = df.to_csv(
    index=False
).encode("utf-8")

st.download_button(
    "📥 Download Report",
    csv,
    "grade_report.csv",
    "text/csv"
)

# ---------------- FOOTER ----------------

st.markdown("---")

st.markdown(
"""
<center>
<h4 style='color:#94a3b8'>
Made with ❤️ using Streamlit
</h4>
</center>
""",
unsafe_allow_html=True
)
