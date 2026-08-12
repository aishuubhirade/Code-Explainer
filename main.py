import streamlit as st
from agent import explain_code

st.set_page_config(
    page_title="AI Code Explainer",
    page_icon="🤖",
    layout="wide"
)

# ---------------- CSS ---------------- #

st.markdown("""
<style>

.stApp{
background:linear-gradient(135deg,#f4f7fb,#eef2ff);
font-family:'Segoe UI';
}

/* Hide Streamlit menu */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Left Card */

.left-card{
background:#16213e;
padding:30px;
border-radius:20px;
color:white;
height:100%;
box-shadow:0 10px 25px rgba(0,0,0,.15);
}

.left-title{
font-size:30px;
font-weight:bold;
margin-bottom:15px;
}

.left-text{
font-size:17px;
line-height:1.8;
color:#ddd;
}

.lang{
margin-top:25px;
font-size:18px;
font-weight:bold;
}

.lang-item{
padding:8px 0;
font-size:18px;
}

/* Right */

.title{
text-align:center;
font-size:45px;
font-weight:bold;
color:#222;
}

.subtitle{
text-align:center;
font-size:20px;
color:#555;
margin-bottom:25px;
}

/* Text Area */

textarea{
font-size:16px !important;
}

/* Button */

.stButton>button{

width:100%;
height:55px;
background:linear-gradient(90deg,#00C9FF,#0072FF);
color:white;
font-size:20px;
font-weight:bold;
border:none;
border-radius:12px;

}

.stButton>button:hover{
background:linear-gradient(90deg,#0072FF,#00C9FF);
}

/* Output */

.output{

background:white;
padding:20px;
border-radius:15px;
box-shadow:0px 10px 20px rgba(0,0,0,.1);

}

</style>
""", unsafe_allow_html=True)


# ---------------- Layout ---------------- #

left,right=st.columns([1,3])

# ---------------- Left ---------------- #

with left:

    st.markdown("""

<div class="left-card">

<div class="left-title">
📘 Code Explainer
</div>

<div class="left-text">

This application helps non-technical users understand programming code in simple English.

</div>

<div class="lang">

Supported Languages

</div>

<div class="lang-item">🐍 Python</div>

<div class="lang-item">☕ Java</div>

<div class="lang-item">🟨 JavaScript</div>

<div class="lang-item">⚙️ C++</div>

<div class="lang-item">🔹 C</div>

<div class="lang-item">💙 HTML</div>

<div class="lang-item">🎨 CSS</div>

</div>

""",unsafe_allow_html=True)

# ---------------- Right ---------------- #

with right:

    st.markdown("<div class='title'>💻 AI Code Explainer</div>",unsafe_allow_html=True)

    st.markdown("<div class='subtitle'>Convert complex code into simple, plain-English explanations using AI.</div>",unsafe_allow_html=True)

    code=st.text_area(
        "🔥 Enter Your Code",
        height=350,
        placeholder="""Example

def greet(name):
    print("Hello",name)

greet("John")
"""
    )

    if st.button("🚀 Explain Code"):

        if code.strip()=="":

            st.warning("Please enter code.")

        else:

            with st.spinner("AI is thinking..."):

                result=explain_code(code)

            st.markdown("### 💻 Your Code")
            st.code(code)

            st.markdown("### 🤖 Explanation")

            st.markdown(f"""
<div class="output">

{result}

</div>
""",unsafe_allow_html=True)

st.markdown("---")
st.caption("🎓 BCA Mini Project | AI Code Explainer | Powered by OpenRouter")