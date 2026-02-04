import streamlit as st
from anthropic import Anthropic
import os

# Page config
st.set_page_config(
    page_title="Implicity Mission Advisor",
    page_icon="🫀",
    layout="wide"
)

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
        **Enjeux de surface :**
        - Maintenir la vélocité produit pendant la transition
        - Assurer la continuité opérationnelle de l'équipe

        **Enjeux sous-jacents :**
        - Structurer une équipe produit qui scale avec l'entreprise
        - Naviguer les contraintes FDA/MDR tout en restant agile
        - Aligner des stakeholders multiples (médecins, patients, fabricants, régulateurs)
        """)

    with col2:
        st.markdown("""
        **Ce que j'apporte :**
        - ✅ Expérience de structuration d'équipes (8-18 personnes)
        - ✅ Navigation réglementaire (Directive Omnibus EU, RGPD)
        - ✅ Capacité à "Manage UP" tout en protégeant les équipes
        - ✅ Posture d'interim assumée : créer de la valeur et préparer la suite
        """)

    st.divider()

    st.header("Mes convictions pour Implicity")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("""
        **🏛️ Le réglementaire comme avantage**

        FDA/MDR ne sont pas des freins. Une équipe mature transforme ces contraintes en avantage compétitif via des process rigoureux et une approche risk-based.
        """)

        st.markdown("""
        **📊 Data comme fondation**

        Dans la télésurveillance cardiaque, la donnée EST le produit. Culture data-driven essentielle.
        """)

    with col2:
        st.markdown("""
        **⚙️ Product Ops = accélérateur**

        Avec 1 Product Ops déjà en place, opportunité de structurer pour que l'équipe puisse doubler sans perdre en efficacité.
        """)

        st.markdown("""
        **🔄 Transition = transformation**

        Un interim n'est pas là pour maintenir le statu quo. C'est une fenêtre pour questionner et améliorer.
        """)

    with col3:
        st.markdown("""
        **🤝 Alignement par la vision**

        Médecins, patients, fabricants, régulateurs : construire une vision produit où chaque partie prenante trouve sa place.
        """)

        st.markdown("""
        **⚡ Excellence opérationnelle + stratégie**

        Capable de débloquer l'opérationnel tout en gardant la hauteur sur le "où va-t-on dans 18 mois ?".
        """)

    st.divider()

    st.header("Pourquoi moi ?")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
        **🎯 Manage UP + protéger les équipes**

        Chez Sephora : stabilisé le delivery, gagné la confiance du CODIR, tout en rendant les équipes plus sereines. Ce n'est pas "soit l'un soit l'autre".

        **📜 Expérience réglementaire**

        - Directive Omnibus EU (Sephora) - coordination juridique/tech/UX
        - Data platform 2M transactions/jour (McDonald's)
        - Services financiers réglementés (CA, AXA, BNP)
        """)

    with col2:
        st.markdown("""
        **👥 Track record structuration équipes**

        - 18 consultants chez Thiga (Tribe Lead)
        - 8 Product People chez Decathlon
        - 3 PMs chez Sephora Europe

        **🤖 Écosystème AI/Data**

        Core Team AI de Thiga avec CEO + 2 partners. Certifications ML (Stanford) et AI Agents (Hugging Face).
        """)

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
        st.subheader("📅 Semaine 1-2")
        st.markdown("**Immersion & Quick Wins**")
        st.markdown("""
        - Rencontres 1:1 avec chaque membre de l'équipe produit
        - Shadow sessions avec les PMs sur leurs sujets
        - Identification de 2-3 quick wins opérationnels
        - **Prise en main d'un sujet concret** pour démontrer par l'exemple
        """)

    with col2:
        st.subheader("📅 Semaine 3-4")
        st.markdown("**Diagnostic & Structuration**")
        st.markdown("""
        - Audit des process produit (discovery, delivery, documentation)
        - Mapping des stakeholders et attentes
        - Proposition d'améliorations avec l'équipe
        - Début de formalisation de la vision produit
        """)

    with col3:
        st.subheader("📅 Mois 2-3")
        st.markdown("**Transformation & Ancrage**")
        st.markdown("""
        - Mise en place des améliorations validées
        - Coaching individuel des PMs et Designers
        - Construction de la roadmap moyen-terme
        - Préparation passation au Head of Product permanent
        """)

    st.divider()

    st.subheader("📦 Livrables clés")

    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        - ✅ Process documentés et opérationnels
        - ✅ Équipe autonome et structurée
        """)
    with col2:
        st.markdown("""
        - ✅ Vision produit formalisée
        - ✅ Recommandations pour le recrutement permanent
        """)

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
