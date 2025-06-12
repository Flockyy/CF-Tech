# CF-Tech  Centre Formation tech


Bienvenue sur ce projet dans le cadre de la formation **Data Engineering Bootcamp – Simplon HDF 2025**.  

Projet à rendre à la fin du 6eme jour.


# 👩‍🎓​ Contexte

Développer le backend d'une solution permettant de gérer un centre de formation, en prenant en compte:
-   les utilisateurs (formateurs, apprenants, staff, admins),
-   les sessions de formation (planning, salles, matériel),
-   les inscriptions des apprenants aux sessions et leurs assiduité.



# 🎯 Objectif

-   Concevoir le schéma relationnel (en SQLModel/SQLAlchemy).
-   Implémenter la validation des données à l’entrée (création/modification) à l’aide de Pydantic.
-   Mettre en place Alembic pour gérer les migrations successives du schéma.
-   Bonus – Développer une application web ou desktop (streamlit, tkinter ou flask) pour interagir avec la base.
-   Collaborer via Git/GitHub
-   Préparer la présentation finale



# 💾 Définition des Modèles (SQLModel & Pydantic)

**Users**
-    Classe de base UserBase (table=False) avec champs communs, puis classes Apprenant, Formateur, StaffPedagogique, Admin héritant de UserBase chacune déclarée table=True.



## 🛠️ Technologies Utilisées
  
-   ⛃ Sqlmodel pour la modélisation des entités.

-   ✅ Pydantic pour la validation des données.

-   ⚗️ Alembic pour les migrations de base de données.

-   🗲 FastAPI 


## 📁 Structure du projet
  
```

CF-TECH/
├── .env
├── .gitignore
├── README.md
├── UML.drawio
├── alembic
│   ├── README
│   ├── env.py
│   ├── script.py.mako
│   └── versions
│       ├── 0eee3628ff11_deleting_id_constraints.py
│       ├── 2425b875fdd2_create_users_tables.py
│       ├── 5b67819ce123_adding_foreign_keys_in_courses_.py
│       ├── a500b7d6e22f_adding_room_color.py
│       ├── ab5508a5ed27_adding_foreign_keys_in_attendances.py
│       └── c88f6d6561bb_adding_many_to_many_staff_duty.py
├── alembic.ini
├── app
│   ├── __init__.py
│   ├── api
│   │   ├── deps.py
│   │   ├── main.py
│   │   └── routes
│   │       ├── admin.py
│   │       ├── duty.py
│   │       ├── staff.py
│   │       ├── trainee.py
│   │       └── trainer.py
│   ├── backend_pre_start.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── db.py
│   ├── crud
│   │   ├── __init__.py
│   │   ├── admin_crud.py
│   │   ├── attendance_crud.py
│   │   ├── course_crud.py
│   │   ├── duty_crud.py
│   │   ├── registration_crud.py
│   │   ├── room_crud.py
│   │   ├── staff_crud.py
│   │   ├── trainee_crud.py
│   │   └── trainer_crud.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── attendance.py
│   │   ├── course.py
│   │   ├── registration.py
│   │   ├── room.py
│   │   ├── staff.py
│   │   ├── trainee.py
│   │   ├── trainer.py
│   │   └── user.py
│   ├── schemas
│   │   ├── __init__.py
│   │   ├── admin_schema.py
│   │   ├── attendance_schema.py
│   │   ├── course_schema.py
│   │   ├── duty_schema.py
│   │   ├── duty_staff_schema.py
│   │   ├── registration_schema.py
│   │   ├── room_schema.py
│   │   ├── staff_schema.py
│   │   ├── trainee_schema.py
│   │   ├── trainer_schema.py
│   │   └── user_schema.py
│   ├── tests
│   │   ├── __init__.py
│   │   └── crud
│   │       ├── __init__.py
│   │       ├── test_admin.py
│   │       ├── test_attendance.py
│   │       ├── test_course.py
│   │       ├── test_duty.py
│   │       ├── test_registration.py
│   │       ├── test_staff.py
│   │       ├── test_trainee.py
│   │       ├── test_trainer.py
│   │       └── test_user.py
│   └── views
│       └── user_view.py
├── database.db
└── requirements.txt

```

  
## 🚀 Mise en route  
  
### 📦 Installation  
  
```bash  
git clone https://github.com/Flockyy/CF-Tech.git
cd CF-Tech

sur linux
python3 -m venv .venv
source venv/bin/activate

sur windows
python -m venv .venv
.\.venv\Scripts\Activate.ps1

pip install -r requirements.txt

alembic upgrade head

python3 app/backend_pre_start.py


```


## 🧪 Lancer l'application

Une fois les dépendences installées et la base de données créée:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

```
dans un navigateur, aller sur http://127.0.0.1:8000/docs ou http://127.0.0.1:8000/redoc


## 📜 License

This project is licensed under the MIT License ©️ 2025.  
You are free to use, modify, and distribute this project with proper attribution.


## 👥 L'équipe

Ce projet a été créé dans le cadre de la formation **Data Engineering Bootcamp – Simplon HDF 2025**.  par une équipe de 3 apprenants:

🔗 [Florian Abgrall](https://github.com/Flockyy)  
🔗 [Sébastien Dewaelle](https://github.com/cebdewaelle)  
🔗 [César Gattano](https://github.com/cesarGattano)

