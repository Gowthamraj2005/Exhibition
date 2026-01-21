import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Career Guidance System")
st.write("Get career suggestions based on marks, skills, and personality")

# =============================
# MACHINE LEARNING MODEL
# =============================
data = {
    'Maths':[85,70,90,60,40,88,65,75,92,55],
    'Physics':[85,60,88,65,45,80,60,70,95,55],
    'Chemistry':[80,70,85,60,50,75,65,68,92,55],
    'Computer':[90,50,95,40,30,85,60,65,98,50],
    'Biology':[70,65,60,80,85,75,70,72,65,80],
    'Accounts':[0,0,0,0,0,0,80,85,75,65],
    'Economics':[0,0,0,0,0,0,70,80,75,60],
    'Business':[0,0,0,0,0,0,75,85,80,60],
    'English':[75,80,90,60,50,78,70,72,85,60],
    'Coding':[1,0,1,0,0,1,0,0,1,0],
    'Communication':[1,1,0,1,1,0,1,1,0,1],
    'Creativity':[0,1,0,1,1,0,1,1,0,1],
    'Art':[0,1,0,1,1,0,1,1,0,1],
    'Sports':[0,0,0,0,1,0,1,1,0,1],
    'Leadership':[0,1,0,1,0,0,1,1,0,1],
    'Teamwork':[1,1,0,1,1,0,1,1,0,1],
    'ProblemSolving':[1,0,1,0,0,1,1,0,1,0],
    'Career':[
        'Software Engineer','Teacher','Data Scientist','Designer','Clerk',
        'Software Engineer','Doctor','Accountant','Entrepreneur','Sports Coach'
    ]
}

df = pd.DataFrame(data)

FEATURES = [
    'Maths','Physics','Chemistry','Computer','Biology',
    'Accounts','Economics','Business','English',
    'Coding','Communication','Creativity','Art','Sports',
    'Leadership','Teamwork','ProblemSolving'
]

X = df[FEATURES]
y = df['Career']

model = DecisionTreeClassifier()
model.fit(X, y)

# =============================
# STREAM SELECTION
# =============================
st.header("1️⃣ Select Your Stream")

stream = st.radio(
    "Choose your stream:",
    ["Computer", "Biology", "Commerce"]
)

# =============================
# MARKS INPUT
# =============================
st.header("2️⃣ Enter Your Marks")

subjects = {
    "Computer": ['Maths','Physics','Chemistry','Computer','English'],
    "Biology": ['Maths','Physics','Chemistry','Biology','English'],
    "Commerce": ['Maths','Accounts','Economics','Business','English']
}[stream]

marks = {}
for sub in subjects:
    marks[sub] = st.number_input(
        f"{sub} Marks",
        min_value=0,
        max_value=100,
        step=1
    )

# =============================
# SKILLS & INTERESTS
# =============================
st.header("3️⃣ Skills & Interests")

skills = {
    'Coding': st.checkbox("Interested in Coding"),
    'Communication': st.checkbox("Good Communication Skills"),
    'Creativity': st.checkbox("Creative Thinking"),
    'Art': st.checkbox("Art / Design Skills"),
    'Sports': st.checkbox("Sports / Physical Skills")
}

# =============================
# PERSONALITY TRAITS
# =============================
st.header("4️⃣ Personality Traits")

personality = {
    'Leadership': st.checkbox("Leadership Skills"),
    'Teamwork': st.checkbox("Teamwork Skills"),
    'ProblemSolving': st.checkbox("Problem Solving Ability")
}

# =============================
# PREDICTION
# =============================
st.header("5️⃣ Career Prediction")

if st.button("🔮 Predict Career"):
    student = {}

    # Store marks
    for f in FEATURES:
        student[f] = 0

    for k,v in marks.items():
        student[k] = v

    # Store skills
    for k,v in skills.items():
        student[k] = int(v)

    # Store personimport streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# =============================
# PAGE CONFIG
# =============================
st.set_page_config(
    page_title="AI Career Guidance System",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 AI Career Guidance System")
st.write("Get career suggestions based on marks, skills, and personality")

# =============================
# MACHINE LEARNING MODEL
# =============================
data = {
    'Maths':[85,70,90,60,40,88,65,75,92,55],
    'Physics':[85,60,88,65,45,80,60,70,95,55],
    'Chemistry':[80,70,85,60,50,75,65,68,92,55],
    'Computer':[90,50,95,40,30,85,60,65,98,50],
    'Biology':[70,65,60,80,85,75,70,72,65,80],
    'Accounts':[0,0,0,0,0,0,80,85,75,65],
    'Economics':[0,0,0,0,0,0,70,80,75,60],
    'Business':[0,0,0,0,0,0,75,85,80,60],
    'English':[75,80,90,60,50,78,70,72,85,60],
    'Coding':[1,0,1,0,0,1,0,0,1,0],
    'Communication':[1,1,0,1,1,0,1,1,0,1],
    'Creativity':[0,1,0,1,1,0,1,1,0,1],
    'Art':[0,1,0,1,1,0,1,1,0,1],
    'Sports':[0,0,0,0,1,0,1,1,0,1],
    'Leadership':[0,1,0,1,0,0,1,1,0,1],
    'Teamwork':[1,1,0,1,1,0,1,1,0,1],
    'ProblemSolving':[1,0,1,0,0,1,1,0,1,0],
    'Career':[
        'Software Engineer','Teacher','Data Scientist','Designer','Clerk',
        'Software Engineer','Doctor','Accountant','Entrepreneur','Sports Coach'
    ]
}

df = pd.DataFrame(data)

FEATURES = [
    'Maths','Physics','Chemistry','Computer','Biology',
    'Accounts','Economics','Business','English',
    'Coding','Communication','Creativity','Art','Sports',
    'Leadership','Teamwork','ProblemSolving'
]

X = df[FEATURES]
y = df['Career']

model = DecisionTreeClassifier()
model.fit(X, y)

# =============================
# STREAM SELECTION
# =============================
st.header("1️⃣ Select Your Stream")

stream = st.radio(
    "Choose your stream:",
    ["Computer", "Biology", "Commerce"]
)

# =============================
# MARKS INPUT
# =============================
st.header("2️⃣ Enter Your Marks")

subjects = {
    "Computer": ['Maths','Physics','Chemistry','Computer','English'],
    "Biology": ['Maths','Physics','Chemistry','Biology','English'],
    "Commerce": ['Maths','Accounts','Economics','Business','English']
}[stream]

marks = {}
for sub in subjects:
    marks[sub] = st.number_input(
        f"{sub} Marks",
        min_value=0,
        max_value=100,
        step=1
    )

# =============================
# SKILLS & INTERESTS
# =============================
st.header("3️⃣ Skills & Interests")

skills = {
    'Coding': st.checkbox("Interested in Coding"),
    'Communication': st.checkbox("Good Communication Skills"),
    'Creativity': st.checkbox("Creative Thinking"),
    'Art': st.checkbox("Art / Design Skills"),
    'Sports': st.checkbox("Sports / Physical Skills")
}

# =============================
# PERSONALITY TRAITS
# =============================
st.header("4️⃣ Personality Traits")

personality = {
    'Leadership': st.checkbox("Leadership Skills"),
    'Teamwork': st.checkbox("Teamwork Skills"),
    'ProblemSolving': st.checkbox("Problem Solving Ability")
}

# =============================
# PREDICTION
# =============================
st.header("5️⃣ Career Prediction")

if st.button("🔮 Predict Career"):
    student = {}

    # Store marks
    for f in FEATURES:
        student[f] = 0

    for k,v in marks.items():
        student[k] = v

    # Store skills
    for k,v in skills.items():
        student[k] = int(v)

    # Store personality
    for k,v in personality.items():
        student[k] = int(v)

    input_data = [student[f] for f in FEATURES]
    prediction = model.predict([input_data])[0]

    st.success("🎯 Suggested Career")
    st.markdown(f"### 🧠 **{prediction}**")

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("AI Career Guidance System | MCA Project | Streamlit Deployment")
ality
    for k,v in personality.items():
        student[k] = int(v)

    input_data = [student[f] for f in FEATURES]
    prediction = model.predict([input_data])[0]

    st.success("🎯 Suggested Career")
    st.markdown(f"### 🧠 **{prediction}**")

# =============================
# FOOTER
# =============================
st.markdown("---")
st.caption("AI Career Guidance System | MCA Project | Streamlit Deployment")
