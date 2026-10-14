# FlowLance

CRM conçu pour les freelances. Centralise clients, projets et factures
en un seul outil avec des rappels automatiques.

[![CI/CD](https://github.com/nadanada2/freelance-crm/actions/workflows/ci.yml/badge.svg)](https://github.com/nadanada2/freelance-crm/actions/workflows/ci.yml)

## Stack technique

- **Frontend** : React + Vite + React Router
- **Backend** : Django 6 + Django REST Framework
- **Auth** : JWT (SimpleJWT)
- **Base de données** : PostgreSQL (Docker) / SQLite (installation locale sans Docker)
- **DevOps** : Docker, Docker Compose, GitHub Actions, GitHub Container Registry

## Fonctionnalités

- Authentification sécurisée (register / login / JWT)
- Gestion complète des clients (CRUD)
- Gestion des projets avec statuts (lead → en cours → terminé)
- Facturation avec numérotation automatique (FAC-2024-001)
- Dashboard avec chiffre d'affaires en temps réel
- Rappels intelligents : factures en retard, clients inactifs

## Lancer le projet avec Docker

Prérequis : Docker Desktop.

```bash
docker compose up --build
```

- Frontend : http://localhost:5173
- Backend (API) : http://localhost:8000

## Tests

```bash
docker compose exec backend python manage.py test
```

Les tests couvrent l'inscription et la connexion, la protection de l'API par authentification,
la création d'un client rattaché à l'utilisateur connecté, et l'isolation des données entre utilisateurs.

## CI/CD

À chaque push sur `main`, GitHub Actions :

1. lance les tests du backend ;
2. si les tests passent, construit les images Docker (backend et frontend)
   et les publie sur GitHub Container Registry.

La configuration se trouve dans `.github/workflows/ci.yml`.

## Installation locale (sans Docker)

### Backend

```bash
cd backend
python -m venv venv
venv\Scripts\activate        # Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

L'application est accessible sur http://localhost:5173

## Organisation

Projet réalisé avec Git (versioning) et Trello (gestion des tâches).