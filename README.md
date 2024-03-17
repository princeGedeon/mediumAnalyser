# Medium Analyser avec Langchain

## Introduction

Medium Analyser est une application qui utilise Langchain et des modèles de langage à grande échelle (LLM) pour analyser et interpréter le contenu sur Medium. Grâce à l'intégration de la gestion de la mémoire, elle offre une performance optimisée.

## Installation

### Prérequis

Avant de commencer, assurez-vous d'avoir Python installé sur votre machine. Créez un environnement virtuel pour gérer les dépendances de manière isolée.

### Création d'un environnement virtuel

Pour créer un environnement virtuel, exécutez la commande suivante dans votre terminal :

```bash
python -m venv venv
```

Activez l'environnement virtuel :

- Sur Windows :
  ```bash
  .\venv\Scripts\activate
  ```

- Sur Unix ou MacOS :
  ```bash
  source venv/bin/activate
  ```

### Installation des dépendances

Installez les dépendances nécessaires à l'aide du gestionnaire de paquets pip :

```bash
pip install -r requirements.txt
```

## Configuration

Avant de lancer l'application, vous devez configurer les clés API nécessaires :

1. **Clé API OpenAI :** Utilisée pour accéder aux modèles LLM d'OpenAI.

2. **Clé API Pinecone :** Nécessaire pour la gestion de la mémoire et l'indexation des données.

Ajoutez les clés API dans un fichier `.env` à la racine de votre projet :

```plaintext
OPENAI_API_KEY=.................
PINECONE_API_KEY=........................
```

## Lancement de l'application

Pour démarrer l'application, exécutez la commande suivante :

```bash
python main.py
```

## Conclusion

Vous avez maintenant tout ce qu'il faut pour lancer et utiliser Medium Analyser. Suivez ces instructions pour installer, configurer et exécuter l'application. Profitez de l'analyse approfondie des contenus Medium avec le soutien de Langchain et des LLM.


Par **Prince Gédon GUEDJE**