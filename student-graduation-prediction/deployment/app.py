import streamlit as st
import pickle
import numpy as np

# ======================
# Konfigurasi Halaman
# ======================
st.set_page_config(
    page_title="Prediksi Kelulusan Mahasiswa",
    page_icon="🎓",
    layout="wide"
)

# ======================
# Load Model
# ======================
model = pickle.load(open("model_kelulusan.pkl", "rb"))

# ======================
# Custom CSS
# ======================
st.markdown("""
<style>
.main {
    background-color: #f8fafc;
}

.title {
    text-align: center;
    color: #2563eb;
    font-size: 40px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 20px;
}

.result-box {
    padding: 20px;
    border-radius: 15px;
    text-align: center;
    font-size: 24px;
    font-weight: bold;
}

.success-box {
    background-color: #dcfce7;
    color: #166534;
}

.fail-box {
    background-color: #fee2e2;
    color: #991b1b;
}
</style>
""", unsafe_allow_html=True)

# ======================
# Sidebar
# ======================
with st.sidebar:
    st.image(
        "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
        width=120
    )

    st.title("📚 Informasi")

    st.markdown("""
    **Judul Proyek**

    Prediksi Kelulusan Mahasiswa Berdasarkan Data Akademik Menggunakan Algoritma Random Forest

    **Metodologi**
    - CRISP-DM

    **Algoritma**
    - Random Forest

    **Dataset**
    - Students Performance in Exams
    """)

# ======================
# Header
# ======================
st.markdown(
    '<p class="title">🎓 Prediksi Kelulusan Mahasiswa</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Machine Learning menggunakan Random Forest</p>',
    unsafe_allow_html=True
)

st.divider()

# ======================
# Input
# ======================
col1, col2 = st.columns(2)

with col1:

    gender = st.selectbox(
        "👤 Gender",
        ["Female", "Male"]
    )

    race = st.selectbox(
        "🌎 Race/Ethnicity",
        ["Group A", "Group B", "Group C", "Group D", "Group E"]
    )

    education = st.selectbox(
        "🎓 Parental Education",
        [
            "Some High School",
            "High School",
            "Some College",
            "Associate Degree",
            "Bachelor Degree",
            "Master Degree"
        ]
    )

with col2:

    lunch = st.selectbox(
        "🍱 Lunch",
        ["Free/Reduced", "Standard"]
    )

    preparation = st.selectbox(
        "📖 Test Preparation",
        ["None", "Completed"]
    )

st.divider()

st.subheader("📊 Nilai Akademik")

math_score = st.slider(
    "Mathematics Score",
    0,
    100,
    75
)

reading_score = st.slider(
    "Reading Score",
    0,
    100,
    75
)

writing_score = st.slider(
    "Writing Score",
    0,
    100,
    75
)

# ======================
# Encoding
# ======================
gender_map = {
    "Female": 0,
    "Male": 1
}

race_map = {
    "Group A": 0,
    "Group B": 1,
    "Group C": 2,
    "Group D": 3,
    "Group E": 4
}

education_map = {
    "Associate Degree": 0,
    "Bachelor Degree": 1,
    "High School": 2,
    "Master Degree": 3,
    "Some College": 4,
    "Some High School": 5
}

lunch_map = {
    "Free/Reduced": 0,
    "Standard": 1
}

prep_map = {
    "None": 0,
    "Completed": 1
}

# ======================
# Prediksi
# ======================
if st.button("🔍 Prediksi Kelulusan", use_container_width=True):

    avg_score = (
        math_score +
        reading_score +
        writing_score
    ) / 3

    input_data = np.array([[
        gender_map[gender],
        race_map[race],
        education_map[education],
        lunch_map[lunch],
        prep_map[preparation],
        math_score,
        reading_score,
        writing_score
    ]])

    prediction = model.predict(input_data)

    st.divider()

    st.metric(
        label="Rata-rata Nilai",
        value=f"{avg_score:.2f}"
    )

    if prediction[0] == 1:

        st.markdown(
            """
            <div class="result-box success-box">
            ✅ DIPREDIKSI LULUS
            </div>
            """,
            unsafe_allow_html=True
        )

        st.balloons()

    else:

        st.markdown(
            """
            <div class="result-box fail-box">
            ❌ DIPREDIKSI TIDAK LULUS
            </div>
            """,
            unsafe_allow_html=True
        )

# ======================
# Footer
# ======================
st.divider()

st.caption(
    "Dibuat menggunakan Streamlit • Random Forest • CRISP-DM"
)