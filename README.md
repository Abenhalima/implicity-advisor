# Implicity Mission Advisor

Agent conversationnel pour présenter la candidature d'Abdessamad Benhalima au poste d'interim Head of Product chez Implicity.

## Déploiement sur Streamlit Cloud

1. Push ce repo sur GitHub
2. Va sur [share.streamlit.io](https://share.streamlit.io)
3. Connecte ton repo GitHub
4. Configure les secrets :
   - Va dans "Advanced settings" > "Secrets"
   - Ajoute : `ANTHROPIC_API_KEY = "sk-ant-..."`
5. Deploy!

## Test en local

```bash
# Crée un environnement virtuel
python -m venv venv
source venv/bin/activate

# Installe les dépendances
pip install -r requirements.txt

# Configure les secrets
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
# Édite secrets.toml avec ta clé API

# Lance l'app
streamlit run app.py
```

## Structure

- `app.py` : Application Streamlit avec le système de prompt complet
- `requirements.txt` : Dépendances Python
- `.streamlit/secrets.toml.example` : Template pour les secrets

## Guardrails

L'agent a des règles strictes :
- Ne jamais inventer d'information
- Distinguer faits (profil) vs convictions (opinions)
- Utiliser les chiffres exacts
- Refuser de répondre si l'info n'est pas disponible
