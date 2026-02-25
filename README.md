# Agent IA – Emploi & Insertion Professionnelle - Projet E2 RNCP37827

Agent conversationnel intelligent développé pour une organisation publique, destiné à accompagner les usagers dans leurs démarches professionnelles et l'accès à l'emploi.

Ce projet couvre le cycle complet :
1. **Veille** (C6) — Identification et suivi des évolutions NLP/IA/RGPD
2. **Benchmark** (C7) — Comparaison de 3 solutions, recommandation argumentée
3. **Installation & configuration** (C8) — Déploiement du service retenu

---

## Contexte

Ce projet répond au besoin d'une organisation publique souhaitant proposer aux usagers un agent IA spécialisé dans l'emploi et l'insertion. La complexité des dispositifs d'insertion, la diversité des offres d'emploi et la multiplicité des informations disponibles rendent l'orientation et le suivi des parcours difficiles à gérer manuellement.

---

## Fonctionnalités

- **Orientation personnalisée** : guide les utilisateurs vers les dispositifs adaptés à leur profil et situation
- **Information actualisée** : fournit des informations claires sur les offres d'emploi, les formations et les aides disponibles
- **Aide à la candidature** : assistance à la rédaction de CV, lettres de motivation et préparation aux entretiens
- **Mise en relation** : facilite le contact avec des services spécialisés ou des partenaires locaux

---

## Architecture technique

L'agent IA repose sur trois composantes essentielles :

1. **Le cerveau (LLM)** – modèle de langage large via Azure OpenAI Service (GPT-4.x)
2. **Les instructions** – prompt système définissant le comportement de l'agent
3. **Les outils** – base de connaissances et connecteurs vers des services externes

---

## Stack technologique

| Composant | Technologie |
|-----------|-------------|
| Langage | Python |
| Cloud & LLM | Microsoft Azure OpenAI Service |
| Interface utilisateur | Streamlit |
| Monitoring | Azure Monitor (intégré) |

---

## Prérequis

- Python 3.10+
- Un abonnement Microsoft Azure avec accès à Azure OpenAI Service
- Une ressource Azure OpenAI déployée avec un modèle GPT-4.x

---

## Installation

```bash
# Cloner le dépôt
git clone <url-du-repo>
cd <nom-du-repo>

# Créer un environnement virtuel
python -m venv venv
source venv/bin/activate  # Windows : venv\Scripts\activate

# Installer les dépendances
pip install -r requirements.txt
```

---

## Configuration

Créer un fichier `.env` à la racine du projet avec les variables suivantes :

```env
AZURE_OPENAI_ENDPOINT=https://<votre-ressource>.openai.azure.com/
AZURE_OPENAI_API_KEY=<votre-clé-api>
AZURE_OPENAI_DEPLOYMENT_NAME=<nom-du-déploiement>
AZURE_OPENAI_API_VERSION=2024-02-01
```

> **Important** : Ne jamais commiter le fichier `.env` dans le dépôt. Ajouter `.env` à votre `.gitignore`.

---

## Lancement

```bash
streamlit run app.py
```

L'interface sera accessible par défaut à l'adresse `http://localhost:8501`.

---

## Conformité & sécurité

Ce projet est développé conformément aux réglementations en vigueur :

- **RGPD** : hébergement des données en Europe, traitement anonymisé, journalisation des échanges
- **EU AI Act** : transparence envers les utilisateurs, traçabilité du fonctionnement du modèle
- **Recommandations CNIL** : protection des données personnelles des usagers
- **RBAC (least privilege)** : gestion des accès par rôles sur Azure
- **Monitoring continu** : supervision des performances et détection d'anomalies via Azure Monitor

---

## Structure du projet

```
.
├── streamlit_gui
│   ├── app.py                  # Point d'entrée Streamlit
├── src/
│   ├── chat_app.py         # Connexion et configuration Azure OpenAI
│                           # Outils et connecteurs de l'agent
├── data/                   # Base de connaissances
├── tests/                  # Tests unitaires et d'intégration
├── requirements.txt
├── .env.example
└── README.md
```


## 📄 Licence

Ce projet est développé à des fins éducatives dans le cadre de la certification RNCP37827.

## 👤 Auteur

Chaima SAAD - Candidate à la certification RNCP37827 Développeur en Intelligence Artificielle

---

**Note** : Ce projet démontre l'ensemble des compétences C6 à C9 du Bloc 2 "Intégrer des modèles et des services d’intelligence artificielle".