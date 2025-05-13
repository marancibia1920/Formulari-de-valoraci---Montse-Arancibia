# Formulari-de-valoraci---Montse-Arancibia
Aplicació web per gestionar votacions locals. Desenvolupada amb Flask (Python), HTML/CSS i SQLite. 

Funcionalitas:
-Formulari per introduir votacions (DNI, població, valoració).
-Emmagatzematge de dades amb SQL.
-Visualització de votacions ja registrades.

ESTRUCTURA DEL PROJECTE
.
├── app.py              # Aplicació principal de Flask
├── votacions.sql       # Script de creació de la base de dades SQL
├── templates/
│   ├── index.html      # Formulari de votació
│   └── votacions.html  # Taula de votacions registrades

Requisits
-Python 3
-Flask

Instal·lació dels requisits --> pip install flask

INSTRUCCIONS D'ÚS:

Executa l'aplicació app.py
Aceddeix a la web: http://127.0.0.1:5000

Pantalles
-/ : Formulari per introduir dades de votació.
-/votacions : Taula amb les votacions registrades.

