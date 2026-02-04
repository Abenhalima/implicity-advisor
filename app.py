import streamlit as st
from anthropic import Anthropic
import os

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
</style>
""", unsafe_allow_html=True)

# Initialize Anthropic client
client = Anthropic(api_key=st.secrets.get("ANTHROPIC_API_KEY", os.getenv("ANTHROPIC_API_KEY")))

# System prompt with full context and guardrails
SYSTEM_PROMPT = """Tu es un assistant qui aide à comprendre la candidature d'Abdessamad Benhalima pour le poste d'interim Head of Product chez Implicity.

# CONTEXTE IMPLICITY

Implicity est une medtech française spécialisée dans la télésurveillance cardiaque. Ils ont développé une plateforme qui collecte les données des pacemakers et défibrillateurs de multiples fabricants (Medtronic, Abbott, Boston Scientific, Biotronik, MicroPort) pour permettre aux cardiologues de suivre leurs patients à distance.

**Situation actuelle :**
- Scale-up en croissance (levée de fonds récente)
- Équipe produit de 5 personnes (2 Product Managers, 2 Product Designers, 1 Product Ops)
- Environnement réglementé (dispositifs médicaux, RGPD santé)
- Contexte multi-pays (France, US, expansion européenne)
- Départ de la Head of Product actuelle → besoin d'un interim pour 6-9 mois

**Enjeux identifiés :**
1. **Surface** : Maintenir la vélocité produit pendant la transition
2. **Sous-jacent** : Structurer une équipe produit qui scale avec l'entreprise
3. **Réglementaire** : Naviguer les contraintes FDA/MDR tout en restant agile
4. **Multi-stakeholder** : Aligner médecins, patients, fabricants, régulateurs

---

# PROFIL ABDESSAMAD BENHALIMA

## Poste actuel
**Tribe Lead Data & AI Products chez Thiga** (cabinet de conseil en Product Management, Paris)
- Dirige une équipe de 18 consultants (PMs et Product Designers)
- Croissance revenue de 1.2M€ à 2.1M€ (+75% YoY)
- Gère P&L, forecasting, recrutement
- Membre de la Core Team AI avec le CEO et 2 partners pour piloter les initiatives AI de Thiga

## Expérience pertinente détaillée

### Leadership & Management d'équipes produit

**Sephora (Avril 2023 - Mai 2024)** - Product Lead Europe
- Management de 3 Product Managers sur les produits e-commerce européens
- Ownership de l'expérience Discovery (Home, Search, Product Pages) avec KPIs de conversion
- **POINT CLÉ - Manage UP** : A stabilisé le delivery, gagné la confiance du CODIR tout en rendant les équipes plus "sereines" - démontrant la capacité à gérer la pression du haut tout en protégeant et motivant les équipes
- Initiative stratégique sur le parcours promotionnel : alignement business, juridique, tech et plusieurs équipes produit
- **Expérience réglementaire EU** : En charge de garantir la compliance avec la Directive Omnibus (directive n° 2019/2161 concernant la protection des consommateurs) sur les pratiques de promotions - coordination des aspects légaux, techniques et UX pour assurer la conformité tout en préservant l'expérience utilisateur

**Decathlon (2022)** - Product Lead
- Management de 8 Product People (équipe significative)
- Structuration des pratiques produit

### Environnements réglementés & data-sensibles

**McDonald's France (2020)** - Consultant Data Platform
- Définition des premiers use cases pour un Datalake traitant jusqu'à 2M transactions/jour
- Conception architecture V1, identification compétences, roadmap 2020

**Vertuoz by ENGIE (2017-2018)** - Product Strategist
- Refonte d'une plateforme B2B SaaS de monitoring de performance énergétique des bâtiments
- Données sensibles, environnement réglementé (performance énergétique)
- Réduction du time-to-value de 1 semaine à immédiat via simplification onboarding

### Expérience grands groupes & transformation

**Chez Thiga (2020-présent) :**
- Leboncoin : Marketplace high-traffic
- Christian Dior : E-commerce luxe
- SeLoger : Marketplace immobilière
- Galeries Lafayette : Retail transformation
- Chanel : Luxe & transformation digitale

**Chez Wavestone (2012-2017) :**
- Crédit Agricole, AXA, BNP Paribas : Services financiers réglementés
- L'Oréal, SNCF, Engie, La Poste : Grands groupes en transformation

### Formation & certifications
- M.Eng. Télécommunications & Systèmes Sans Fil - ISEP Paris
- Machine Learning Specialization - DeepLearning.AI & Stanford (2024)
- AI Agents Fundamentals - Hugging Face (2025)

---

# CONVICTIONS POUR IMPLICITY

## Conviction 1 : Le réglementaire comme avantage compétitif
Dans un environnement FDA/MDR, la tentation est de voir le réglementaire comme un frein. Ma conviction : une équipe produit mature transforme ces contraintes en avantage compétitif. Des process de documentation rigoureux, une traçabilité des décisions, une approche risk-based du développement - tout cela peut accélérer les cycles plutôt que les ralentir si c'est bien intégré dans la culture produit.

## Conviction 2 : Product Ops comme accélérateur de scale
Avec 1 Product Ops déjà en place, il y a une opportunité de structurer les rituels, la documentation, et les métriques de manière à ce que l'équipe puisse doubler sans perdre en efficacité. Le rôle d'un Head of Product interim est de laisser des fondations solides, pas juste de "tenir la boutique".

## Conviction 3 : L'alignement multi-stakeholder par la vision partagée
Médecins, patients, fabricants, régulateurs - chacun a ses priorités. La clé n'est pas de faire des compromis sur tout, mais de construire une vision produit suffisamment claire et inspirante pour que chaque partie prenante y trouve sa place. C'est un travail de narration et d'alignement constant.

## Conviction 4 : Transition = opportunité de transformation
Un interim n'est pas là pour maintenir le statu quo. C'est une fenêtre unique pour questionner les pratiques, identifier les quick wins, et préparer l'équipe à accueillir un Head of Product permanent dans les meilleures conditions.

## Conviction 5 : Data comme fondation
Dans la télésurveillance cardiaque, la donnée EST le produit. Une culture data-driven dans l'équipe produit (métriques d'usage, feedback loops, A/B testing quand possible) est essentielle.

## Conviction 6 : Excellence opérationnelle + vision stratégique
Un Head of Product doit être capable de descendre dans l'opérationnel (débloquer un sujet, challenger un spec) tout en gardant la hauteur stratégique (où va-t-on dans 18 mois ?).

---

# PLAN D'ACTION PROPOSÉ (Approche offensive)

## Semaine 1-2 : Immersion & Quick Wins
- Rencontres 1:1 avec chaque membre de l'équipe produit
- Shadow sessions avec les PMs sur leurs sujets en cours
- Identification de 2-3 quick wins opérationnels à délivrer rapidement
- Prise en main d'un sujet concret pour démontrer par l'exemple

## Semaine 3-4 : Diagnostic & Structuration
- Audit des process produit actuels (discovery, delivery, documentation)
- Mapping des stakeholders et de leurs attentes
- Proposition d'améliorations process avec l'équipe
- Début de formalisation de la vision produit

## Mois 2-3 : Transformation & Ancrage
- Mise en place des améliorations process validées
- Coaching individuel des PMs et Designers
- Construction de la roadmap moyen-terme
- Préparation de la passation au futur Head of Product permanent

## Livrables clés
- Process documentés et opérationnels
- Équipe autonome et structurée
- Vision produit formalisée
- Recommandations pour le recrutement du Head of Product permanent

---

# POURQUOI ABDESSAMAD

## 1. Capacité à "Manage UP" tout en protégeant les équipes
Chez Sephora, démonstration concrète : a su gagner la confiance du CODIR (visibilité, delivery fiable, communication executive) tout en créant un environnement serein pour les équipes. Ce n'est pas "soit l'un soit l'autre" - c'est une compétence de translation et de protection.

## 2. Expérience des environnements réglementés et data-sensibles
- Chez Sephora : pilotage de la mise en conformité avec la Directive Omnibus (directive EU 2019/2161 sur la protection des consommateurs) - coordination juridique, tech et UX
- McDonald's : data platform, 2M transactions/jour
- Vertuoz/ENGIE : performance énergétique réglementée
- Services financiers : Crédit Agricole, AXA, BNP Paribas
Compréhension native des contraintes de compliance et de la valeur de la rigueur.

## 3. Track record de structuration d'équipes produit
- 18 consultants managés chez Thiga
- 8 Product People chez Decathlon
- 3 PMs chez Sephora
Pas juste du management, mais de la structuration : process, rituels, montée en compétence.

## 4. Posture d'interim assumée
En tant que consultant, habitué à arriver dans des contextes nouveaux, créer de la valeur rapidement, et préparer la suite. Pas d'agenda caché de "rester à tout prix" - l'objectif est de laisser l'équipe dans un meilleur état.

## 5. Connaissance de l'écosystème AI/Data
Membre de la Core Team AI de Thiga avec le CEO et 2 partners. Certifications ML (Stanford/DeepLearning.AI) et AI Agents (Hugging Face). Peut accompagner Implicity sur les sujets d'IA appliquée à la santé si pertinent.

## 6. Réactivité et disponibilité
En tant que Tribe Lead, flexibilité pour s'engager rapidement sur une mission stratégique.

---

# GUARDRAILS - RÈGLES STRICTES

1. **Ne jamais inventer d'information** : Si une question porte sur un élément non présent dans ce contexte, réponds "Je n'ai pas cette information dans le profil d'Abdessamad."

2. **Distinguer faits et convictions** :
   - Les éléments du profil sont des FAITS vérifiables
   - Les convictions sont des OPINIONS/POSITIONS d'Abdessamad
   - Toujours être clair sur cette distinction

3. **Ne pas exagérer** :
   - Utiliser les chiffres exacts (8 Product People chez Decathlon, pas "une grande équipe")
   - Ne pas inventer de résultats ou métriques non mentionnés

4. **Rester factuel sur Implicity** : Le contexte Implicity vient d'un call de qualification. Ne pas inventer de détails sur leur organisation ou leurs défis au-delà de ce qui est documenté.

5. **Ton professionnel** : Répondre de manière claire, structurée, et professionnelle. Pas de marketing excessif.

---

# FORMAT DE RÉPONSE

- Réponds en français sauf si la question est en anglais
- Sois concis mais complet
- Utilise des bullet points pour la clarté quand approprié
- Si tu cites une expérience, mentionne le contexte (entreprise, période)
- Si tu donnes une conviction, précise que c'est une position/opinion
"""

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# ============================================
# MAIN LAYOUT WITH OVERVIEW + CHAT
# ============================================

st.title("🫀 Abdessamad Benhalima × Implicity")
st.markdown("**Candidature pour le poste d'interim Head of Product**")

st.divider()

# Create tabs for different sections
tab1, tab2, tab3, tab4 = st.tabs(["📋 Vue d'ensemble", "💬 Questions", "📅 Plan d'action", "👤 Profil détaillé"])

# ============================================
# TAB 1: OVERVIEW
# ============================================
with tab1:
    st.header("Ma compréhension de vos enjeux")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="conviction-card">
            <h4>🔍 Enjeux de surface</h4>
            <ul>
                <li>Maintenir la vélocité produit pendant la transition</li>
                <li>Assurer la continuité opérationnelle de l'équipe</li>
            </ul>
            <h4>🎯 Enjeux sous-jacents</h4>
            <ul>
                <li>Structurer une équipe produit qui scale avec l'entreprise</li>
                <li>Naviguer les contraintes FDA/MDR tout en restant agile</li>
                <li>Aligner des stakeholders multiples (médecins, patients, fabricants, régulateurs)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="highlight-box">
            <h4>✨ Ce que j'apporte</h4>
            <ul>
                <li>✅ Expérience de structuration d'équipes (8-18 personnes)</li>
                <li>✅ Navigation réglementaire (Directive Omnibus EU, RGPD)</li>
                <li>✅ Capacité à "Manage UP" tout en protégeant les équipes</li>
                <li>✅ Posture d'interim assumée : créer de la valeur et préparer la suite</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.header("Mes convictions pour Implicity")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="conviction-card">
            <h4>🏛️ Le réglementaire comme avantage</h4>
            <p>FDA/MDR ne sont pas des freins. Une équipe mature transforme ces contraintes en avantage compétitif via des process rigoureux et une approche risk-based.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="conviction-card">
            <h4>📊 Data comme fondation</h4>
            <p>Dans la télésurveillance cardiaque, la donnée EST le produit. Culture data-driven essentielle.</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="conviction-card">
            <h4>⚙️ Product Ops = accélérateur</h4>
            <p>Avec 1 Product Ops déjà en place, opportunité de structurer pour que l'équipe puisse doubler sans perdre en efficacité.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="conviction-card">
            <h4>🔄 Transition = transformation</h4>
            <p>Un interim n'est pas là pour maintenir le statu quo. C'est une fenêtre pour questionner et améliorer.</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="conviction-card">
            <h4>🤝 Alignement par la vision</h4>
            <p>Médecins, patients, fabricants, régulateurs : construire une vision produit où chaque partie prenante trouve sa place.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="conviction-card">
            <h4>⚡ Excellence opérationnelle + stratégie</h4>
            <p>Capable de débloquer l'opérationnel tout en gardant la hauteur sur le "où va-t-on dans 18 mois ?".</p>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.header("Pourquoi moi ?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        <div class="why-card">
            <h4>🎯 Manage UP + protéger les équipes</h4>
            <p>Chez Sephora : stabilisé le delivery, gagné la confiance du CODIR, tout en rendant les équipes plus sereines. Ce n'est pas "soit l'un soit l'autre".</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="why-card">
            <h4>📜 Expérience réglementaire</h4>
            <ul>
                <li>Directive Omnibus EU (Sephora) - coordination juridique/tech/UX</li>
                <li>Data platform 2M transactions/jour (McDonald's)</li>
                <li>Services financiers réglementés (CA, AXA, BNP)</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="why-card">
            <h4>👥 Track record structuration équipes</h4>
            <p>
                <span class="badge">18 consultants - Thiga</span>
                <span class="badge badge-violet">8 Product People - Decathlon</span>
                <span class="badge">3 PMs - Sephora Europe</span>
            </p>
            <p style="margin-top: 10px;">Pas juste du management, mais de la structuration : process, rituels, montée en compétence.</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="why-card">
            <h4>🤖 Écosystème AI/Data</h4>
            <p>Core Team AI de Thiga avec CEO + 2 partners.</p>
            <p>
                <span class="badge badge-violet">ML - Stanford</span>
                <span class="badge">AI Agents - Hugging Face</span>
            </p>
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
                        model="claude-3-5-sonnet-20241022",
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
                    st.error(f"Erreur lors de la génération de la réponse. Veuillez réessayer.")

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
    st.markdown("*Approche offensive : je prends des sujets dès la semaine 1*")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        <div class="timeline-card">
            <h3>📅 Semaine 1-2</h3>
            <p><strong>Immersion & Quick Wins</strong></p>
            <ul>
                <li>Rencontres 1:1 avec chaque membre de l'équipe produit</li>
                <li>Shadow sessions avec les PMs sur leurs sujets</li>
                <li>Identification de 2-3 quick wins opérationnels</li>
                <li><strong>Prise en main d'un sujet concret</strong> pour démontrer par l'exemple</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
        <div class="timeline-card">
            <h3>📅 Semaine 3-4</h3>
            <p><strong>Diagnostic & Structuration</strong></p>
            <ul>
                <li>Audit des process produit (discovery, delivery, documentation)</li>
                <li>Mapping des stakeholders et attentes</li>
                <li>Proposition d'améliorations avec l'équipe</li>
                <li>Début de formalisation de la vision produit</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown("""
        <div class="timeline-card">
            <h3>📅 Mois 2-3</h3>
            <p><strong>Transformation & Ancrage</strong></p>
            <ul>
                <li>Mise en place des améliorations validées</li>
                <li>Coaching individuel des PMs et Designers</li>
                <li>Construction de la roadmap moyen-terme</li>
                <li>Préparation passation au Head of Product permanent</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div class="highlight-box">
        <h4>📦 Livrables clés</h4>
        <p>
            <span class="badge">Process documentés</span>
            <span class="badge">Équipe autonome</span>
            <span class="badge">Vision produit formalisée</span>
            <span class="badge">Recommandations recrutement</span>
        </p>
    </div>
    """, unsafe_allow_html=True)

# ============================================
# TAB 4: DETAILED PROFILE
# ============================================
with tab4:
    st.header("Profil détaillé")

    st.subheader("Poste actuel")
    st.markdown("""
    **Tribe Lead Data & AI Products chez Thiga** (Paris)
    - Direction d'une équipe de 18 consultants (PMs et Product Designers)
    - Croissance revenue de 1.2M€ à 2.1M€ (+75% YoY)
    - Gestion P&L, forecasting, recrutement
    - Membre de la Core Team AI avec le CEO et 2 partners
    """)

    st.subheader("Expériences clés")

    with st.expander("🛍️ Sephora (2023-2024) - Product Lead Europe"):
        st.markdown("""
        - Management de 3 Product Managers sur les produits e-commerce européens
        - Ownership de l'expérience Discovery (Home, Search, Product Pages)
        - **Manage UP** : Stabilisé le delivery, gagné la confiance du CODIR tout en rendant les équipes plus "sereines"
        - **Compliance Directive Omnibus** : Coordination juridique, technique et UX pour assurer la conformité sur les pratiques de promotions
        """)

    with st.expander("🏃 Decathlon (2022) - Product Lead"):
        st.markdown("""
        - Management de 8 Product People
        - Structuration des pratiques produit
        """)

    with st.expander("🍔 McDonald's France (2020) - Consultant Data Platform"):
        st.markdown("""
        - Définition des premiers use cases pour un Datalake (jusqu'à 2M transactions/jour)
        - Conception architecture V1, identification compétences, roadmap
        """)

    with st.expander("⚡ Vertuoz by ENGIE (2017-2018) - Product Strategist"):
        st.markdown("""
        - Refonte plateforme B2B SaaS de monitoring de performance énergétique
        - Environnement réglementé, données sensibles
        - Réduction du time-to-value de 1 semaine à immédiat
        """)

    with st.expander("🏦 Wavestone (2012-2017) - Consultant"):
        st.markdown("""
        Services financiers réglementés :
        - Crédit Agricole, AXA, BNP Paribas

        Grands groupes en transformation :
        - L'Oréal, SNCF, Engie, La Poste
        """)

    st.subheader("Formation")
    st.markdown("""
    - 🎓 M.Eng. Télécommunications & Systèmes Sans Fil - ISEP Paris
    - 🤖 Machine Learning Specialization - DeepLearning.AI & Stanford (2024)
    - 🤖 AI Agents Fundamentals - Hugging Face (2025)
    """)

# ============================================
# FOOTER
# ============================================
st.divider()
st.caption("Agent créé par Abdessamad Benhalima pour la mission Implicity • Février 2026")
