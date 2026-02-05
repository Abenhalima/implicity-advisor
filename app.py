import streamlit as st
from anthropic import Anthropic
import os
import yaml
from pathlib import Path

# ============================================
# LOAD CONTENT FROM FILES
# ============================================
def load_yaml(filename):
    """Load YAML content file"""
    path = Path(__file__).parent / "content" / filename
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def load_prompt():
    """Load system prompt from markdown file"""
    path = Path(__file__).parent / "prompts" / "system.md"
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

# Load all content
ENJEUX_DATA = load_yaml("enjeux.yaml")
CONVICTIONS_DATA = load_yaml("convictions.yaml")
POURQUOI_MOI_DATA = load_yaml("pourquoi_moi.yaml")
PLAN_ACTION_DATA = load_yaml("plan_action.yaml")
PROFIL_DATA = load_yaml("profil.yaml")
SYSTEM_PROMPT = load_prompt()

# Page config
st.set_page_config(
    page_title="Implicity Mission Advisor",
    page_icon="🫀",
    layout="wide"
)

# ============================================
# THIGA BRAND STYLING
# ============================================
st.markdown("""
<style>
    /* Import Kanit font */
    @import url('https://fonts.googleapis.com/css2?family=Kanit:wght@300;400;500;600;700&display=swap');

    /* Thiga Colors */
    :root {
        --thiga-primary: #00D8A2;
        --thiga-violet: #5818FF;
        --thiga-plum: #1B0442;
        --thiga-magenta: #C50041;
        --thiga-light-purple: #E6DEFA;
        --thiga-dark: #0E0E0E;
        --thiga-gray: #848182;
    }

    /* Force light theme */
    .stApp {
        background-color: #ffffff !important;
    }

    .stApp > header {
        background-color: #ffffff !important;
    }

    section[data-testid="stSidebar"] {
        background-color: #f8f9fa !important;
    }

    /* Global font and text color */
    html, body, [class*="css"] {
        font-family: 'Kanit', sans-serif;
        color: #1B0442 !important;
    }

    /* Force all text dark */
    p, li, span, div, label {
        color: #1B0442 !important;
    }

    /* Markdown text */
    .stMarkdown, .stMarkdown p, .stMarkdown li {
        color: #1B0442 !important;
    }

    /* Expander content */
    .streamlit-expanderContent p, .streamlit-expanderContent li {
        color: #1B0442 !important;
    }

    /* Main title styling */
    h1 {
        font-family: 'Kanit', sans-serif !important;
        font-weight: 600 !important;
        color: var(--thiga-plum) !important;
    }

    /* Headers */
    h2, h3 {
        font-family: 'Kanit', sans-serif !important;
        color: var(--thiga-plum) !important;
    }

    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 8px;
        background-color: var(--thiga-light-purple);
        padding: 10px;
        border-radius: 10px;
    }

    .stTabs [data-baseweb="tab"] {
        font-family: 'Kanit', sans-serif;
        font-weight: 500;
        color: var(--thiga-plum);
        border-radius: 8px;
        padding: 10px 20px;
    }

    .stTabs [aria-selected="true"] {
        background-color: var(--thiga-primary) !important;
        color: white !important;
    }

    /* Cards styling */
    .conviction-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 24px;
        margin: 10px 0;
        border-left: 4px solid var(--thiga-primary);
        box-shadow: 0 4px 15px rgba(88, 24, 255, 0.1);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        color: #1B0442;
    }

    .conviction-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(88, 24, 255, 0.15);
    }

    .conviction-card h4 {
        color: var(--thiga-violet) !important;
        margin-bottom: 12px;
        font-weight: 600;
    }

    .conviction-card p, .conviction-card li {
        color: #1B0442 !important;
    }

    /* Highlight boxes */
    .highlight-box {
        background: linear-gradient(135deg, var(--thiga-primary) 0%, #00b88a 100%);
        color: white;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
    }

    .highlight-box h4 {
        color: white !important;
        margin-bottom: 10px;
    }

    /* Why me cards */
    .why-card {
        background: #ffffff;
        border-radius: 12px;
        padding: 20px;
        margin: 10px 0;
        border: 2px solid var(--thiga-light-purple);
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        color: #1B0442;
    }

    .why-card:hover {
        border-color: var(--thiga-primary);
    }

    .why-card h4 {
        color: var(--thiga-violet) !important;
    }

    .why-card p, .why-card li {
        color: #1B0442 !important;
    }

    /* Timeline styling */
    .timeline-card {
        background: #ffffff;
        border-radius: 16px;
        padding: 24px;
        margin: 10px 0;
        border-top: 4px solid var(--thiga-violet);
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        color: #1B0442;
    }

    .timeline-card h3 {
        color: var(--thiga-violet) !important;
    }

    .timeline-card p, .timeline-card li {
        color: #1B0442 !important;
    }

    /* Buttons */
    .stButton > button {
        font-family: 'Kanit', sans-serif;
        background: linear-gradient(135deg, var(--thiga-primary) 0%, #00b88a 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: 500;
        transition: all 0.2s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(135deg, #00b88a 0%, var(--thiga-primary) 100%);
        box-shadow: 0 4px 12px rgba(0, 216, 162, 0.4);
    }

    /* Expanders */
    .streamlit-expanderHeader {
        font-family: 'Kanit', sans-serif;
        font-weight: 500;
        background-color: var(--thiga-light-purple);
        border-radius: 8px;
    }

    /* Chat input */
    .stChatInput > div {
        border-color: var(--thiga-primary) !important;
        border-radius: 12px;
    }

    /* Dividers */
    hr {
        border-color: var(--thiga-light-purple);
    }

    /* Footer */
    .footer {
        text-align: center;
        color: var(--thiga-gray);
        padding: 20px;
        font-size: 14px;
    }

    /* Metrics styling */
    .metric-card {
        background: var(--thiga-plum);
        color: white;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
    }

    .metric-card .number {
        font-size: 2.5em;
        font-weight: 700;
        color: var(--thiga-primary);
    }

    /* Badge styling */
    .badge {
        display: inline-block;
        background: var(--thiga-primary);
        color: white;
        padding: 4px 12px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 500;
        margin: 2px;
    }

    .badge-violet {
        background: var(--thiga-violet);
    }

    /* Grid layouts for aligned cards */
    .grid-3col {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 16px;
        margin: 10px 0;
    }

    .grid-2col {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 16px;
        margin: 10px 0;
    }

    .grid-card {
        height: 100%;
        display: flex;
        flex-direction: column;
    }

    /* Responsive: stack on mobile */
    @media (max-width: 768px) {
        .grid-3col, .grid-2col {
            grid-template-columns: 1fr;
        }
    }
</style>
""", unsafe_allow_html=True)

# Initialize Anthropic client
client = Anthropic(api_key=st.secrets.get("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY")))

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================
# MAIN LAYOUT WITH OVERVIEW + CHAT
# ============================================

# Header with photo - using HTML for better alignment
st.markdown("""
<div style="display: flex; align-items: center; gap: 30px; padding: 20px 0;">
    <img src="https://media.licdn.com/dms/image/v2/D4E03AQFbdiBCN6uZAw/profile-displayphoto-crop_800_800/B4EZnNRJt.HEAI-/0/1760085452086?e=1772064000&v=beta&t=AvnHExiCQXA0jsah6AbpLJXqJErF2pg_mCunV2QABKA"
         style="width: 140px; height: 140px; border-radius: 50%; border: 4px solid #00D8A2; object-fit: cover; flex-shrink: 0;">
    <div>
        <h1 style="margin: 0; font-size: 2em; line-height: 1.1;">Abdessamad Benhalima × Implicity</h1>
        <p style="margin: 2px 0 0 0; font-size: 1.1em; line-height: 1.4;">
            <strong>Candidature pour le poste d'interim Head of Product</strong><br>
            <span style="color: #848182;">Tribe Lead Data & AI Products @ Thiga</span>
        </p>
    </div>
</div>
""", unsafe_allow_html=True)

st.divider()

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["📋 Vue d'ensemble", "💬 Questions", "📅 Plan d'action", "👤 Profil détaillé"])

# ============================================
# TAB 1: OVERVIEW
# ============================================
with tab1:
    # ==========================================
    # SECTION 1: ENJEUX (grille 3x2)
    # ==========================================
    st.header("Ma compréhension de vos enjeux")

    # Use HTML grid for better alignment
    enjeux_cards = ""
    for enjeu in ENJEUX_DATA["enjeux"]:
        points_html = "".join([f"<li>{p}</li>" for p in enjeu["points"]])
        enjeux_cards += f"""
        <div class="grid-card conviction-card">
            <h4>{enjeu["icon"]} {enjeu["title"]}</h4>
            <ul>{points_html}</ul>
        </div>
        """

    st.markdown(f"""
    <div class="grid-3col">
        {enjeux_cards}
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ==========================================
    # SECTION 2: CONVICTIONS (grille 2x2)
    # ==========================================
    st.header("Mes convictions pour Implicity")

    convictions_cards = ""
    for conviction in CONVICTIONS_DATA["convictions"]:
        convictions_cards += f"""
        <div class="grid-card conviction-card">
            <h4>{conviction["icon"]} {conviction["title"]}</h4>
            <p>{conviction["description"]}</p>
        </div>
        """

    st.markdown(f"""
    <div class="grid-2col">
        {convictions_cards}
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # ==========================================
    # SECTION 3: POURQUOI MOI (bloc unique)
    # ==========================================
    st.header("Pourquoi moi ?")

    # Ce que j'apporte (liste)
    apports_html = "".join([f"<li>✅ {a}</li>" for a in POURQUOI_MOI_DATA["ce_que_japporte"]])

    # Preuves (cards)
    preuves_cards = ""
    for preuve in POURQUOI_MOI_DATA["preuves"]:
        content_html = ""
        if "content" in preuve:
            content_html += f"<p>{preuve['content']}</p>"
        if "points" in preuve:
            points = "".join([f"<li>{p}</li>" for p in preuve["points"]])
            content_html += f"<ul>{points}</ul>"
        if "badges" in preuve:
            badges = "".join([
                f'<span class="badge{" badge-violet" if b.get("style") == "violet" else ""}">{b["text"]}</span>'
                for b in preuve["badges"]
            ])
            content_html += f"<p>{badges}</p>"

        preuves_cards += f"""
        <div class="grid-card why-card">
            <h4>{preuve["icon"]} {preuve["title"]}</h4>
            {content_html}
        </div>
        """

    st.markdown(f"""
    <div class="highlight-box" style="margin-bottom: 20px;">
        <h4>✨ Ce que j'apporte</h4>
        <ul>{apports_html}</ul>
    </div>
    <div class="grid-3col">
        {preuves_cards}
    </div>
    """, unsafe_allow_html=True)

# ============================================
# TAB 2: CHAT
# ============================================
with tab2:
    st.header("Posez vos questions")
    st.markdown("*L'assistant répond sur la base de mon profil vérifié - pas d'invention.*")

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("Votre question sur mon profil ou mon approche..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Réflexion..."):
                try:
                    response = client.messages.create(
                        model="claude-sonnet-4-20250514",
                        max_tokens=1024,
                        system=SYSTEM_PROMPT,
                        messages=[
                            {"role": m["role"], "content": m["content"]}
                            for m in st.session_state.messages
                        ]
                    )
                    assistant_message = response.content[0].text
                    st.markdown(assistant_message)
                    st.session_state.messages.append({"role": "assistant", "content": assistant_message})
                except Exception as e:
                    st.error(f"Erreur: {str(e)}")

    # Quick questions
    st.divider()
    st.markdown("**Questions fréquentes :**")

    questions = [
        "Comment gères-tu la relation avec le CODIR ?",
        "Quelle expérience en environnement réglementé ?",
        "Comment structurerais-tu l'équipe produit ?",
        "Quelle serait ta priorité la première semaine ?",
    ]

    cols = st.columns(2)
    for i, q in enumerate(questions):
        with cols[i % 2]:
            if st.button(q, key=f"q_{i}", use_container_width=True):
                st.session_state.messages.append({"role": "user", "content": q})
                st.rerun()

    if st.button("🗑️ Effacer la conversation", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ============================================
# TAB 3: ACTION PLAN
# ============================================
with tab3:
    st.header("Plan d'action proposé")
    st.markdown(f"*{PLAN_ACTION_DATA['intro']}*")

    # Phases - dynamically generated from YAML
    col1, col2, col3 = st.columns(3)
    columns = [col1, col2, col3]

    for i, phase in enumerate(PLAN_ACTION_DATA["phases"]):
        with columns[i % 3]:
            points_html = "".join([f"<li>{p}</li>" for p in phase["points"]])
            st.markdown(f"""
            <div class="timeline-card">
                <h3>📅 {phase["title"]}</h3>
                <p><strong>{phase["subtitle"]}</strong></p>
                <ul>{points_html}</ul>
            </div>
            """, unsafe_allow_html=True)

    st.divider()

    # Livrables
    livrables_html = "".join([f'<span class="badge">{l}</span>' for l in PLAN_ACTION_DATA["livrables"]])
    st.markdown(f"""
    <div class="highlight-box">
        <h4>📦 Livrables clés</h4>
        <p>{livrables_html}</p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# TAB 4: DETAILED PROFILE
# ============================================
with tab4:
    st.header("Profil détaillé")

    # Poste actuel - from YAML
    st.subheader("Poste actuel")
    poste = PROFIL_DATA["poste_actuel"]
    points_md = "\n".join([f"- {p}" for p in poste["points"]])
    st.markdown(f"""
    **{poste["titre"]}** ({poste["lieu"]})
    {points_md}
    """)

    st.subheader("Expériences clés")

    # Expériences - dynamically generated from YAML
    for exp in PROFIL_DATA["experiences"]:
        with st.expander(f"{exp['emoji']} {exp['entreprise']} ({exp['periode']}) - {exp['poste']}"):
            if "points" in exp:
                points_md = "\n".join([f"- {p}" for p in exp["points"]])
                st.markdown(points_md)
            if "sections" in exp:
                for section in exp["sections"]:
                    st.markdown(f"**{section['titre']} :**")
                    items_md = "\n".join([f"- {item}" for item in section["items"]])
                    st.markdown(items_md)

    # Formation - from YAML
    st.subheader("Formation")
    formation_md = "\n".join([f"- {f['emoji']} {f['titre']}" for f in PROFIL_DATA["formation"]])
    st.markdown(formation_md)

# ============================================
# FOOTER
# ============================================
st.divider()
st.caption("Agent créé par Abdessamad Benhalima pour la mission Implicity • Février 2026")
