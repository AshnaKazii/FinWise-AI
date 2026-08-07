import streamlit as st


def load_css():
    st.markdown("""
<style>


/* -----------------------------
   GLOBAL
------------------------------*/


#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}


.block-container{
    padding-top:1rem;
    padding-bottom:2rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:1400px;
}


/* -----------------------------
   SIDEBAR
------------------------------*/


[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#0F172A,#1E293B);
}


[data-testid="stSidebar"] *{
    color:white;
}


[data-testid="stSidebarNav"]{
    padding-top:15px;
}


/* -----------------------------
   HEADINGS
------------------------------*/


h1{
    color:#16A34A;
    font-weight:800;
}


h2,h3{
    font-weight:700;
}


/* -----------------------------
   METRIC CARDS
------------------------------*/


[data-testid="metric-container"]{


background:white;


border-radius:18px;


padding:18px;


border:1px solid #E5E7EB;


box-shadow:0 10px 20px rgba(0,0,0,.08);


}


[data-testid="metric-container"]:hover{


transform:translateY(-5px);


transition:.25s;


}


/* -----------------------------
   BUTTONS
------------------------------*/


.stButton>button{


width:100%;


height:48px;


border-radius:12px;


border:none;


font-weight:700;


background:#16A34A;


color:white;


}


.stButton>button:hover{


background:#15803D;


}


/* -----------------------------
   INPUTS
------------------------------*/


.stTextInput input,
.stNumberInput input{


border-radius:10px;


}


textarea{


border-radius:10px !important;


}


/* -----------------------------
   DATAFRAME
------------------------------*/


[data-testid="stDataFrame"]{


border-radius:14px;


overflow:hidden;


}


/* -----------------------------
   CHAT
------------------------------*/


[data-testid="stChatMessage"]{


border-radius:14px;


padding:15px;


}


/* -----------------------------
   INFO BOX
------------------------------*/


.stAlert{


border-radius:14px;


}


/* -----------------------------
   PROGRESS BAR
------------------------------*/


.stProgress>div>div>div{


background:#16A34A;


}


</style>
""", unsafe_allow_html=True)