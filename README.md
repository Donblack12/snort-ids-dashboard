# 🚨 Snort IDS — Tableau de bord visuel

Projet personnel de détection d'intrusions avec **Snort** et visualisation web via **Flask**. Ce projet permet de suivre les alertes réseau en temps réel dans un environnement Linux virtualisé.

---

## 🎯 Objectif du projet

> Mettre en place un système IDS open-source, détecter du trafic malveillant, analyser les alertes générées par Snort, puis les afficher proprement sur un dashboard accessible via navigateur.

Ce projet m'a permis de toucher à :
- La configuration de Snort
- L’écriture de règles personnalisées
- Le parsing de logs
- Le développement web Python avec Flask
- L'intégration de visualisation de données avec Matplotlib

---

## 🧰 Technologies utilisées

| Stack | Utilisation |
|-------|-------------|
| Snort | Détection d’intrusion (IDS) |
| Flask | Interface web pour afficher les alertes |
| Matplotlib | Génération de graphiques d’alertes |
| Bootstrap 5 | Mise en forme visuelle responsive |
| Multipass / Ubuntu | VM pour l’environnement d’exécution |
| PhpStorm | Éditeur distant pour la VM Ubuntu |

---

## 🖼️ Aperçu du dashboard

### 📊 Graphique des alertes
![Graphique]

### 🧾 Liste des dernières alertes
![Alertes]

---

## ⚙️ Installation rapide

```bash
git clone https://github.com/Donblack12/snort-ids-dashboard.git
cd snort-ids-dashboard
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Accès via [http://localhost:5000](http://localhost:5000) ou depuis l’IP de la VM Multipass : `http://<IP_VM>:5000`


## 📂 Structure du projet

```
snort-ids-dashboard/
├── app.py                  # Application Flask
├── README.md               # Présentation du projet
├── capture/               # Captures d’écran
└── venv/                   # Environnement virtuel (non versionné)
```


## ✅ Fonctionnalités

- Lecture dynamique du fichier d’alertes Snort (`snort.alert.fast`)
- Affichage graphique des types d’alertes
- Affichage des 20 dernières alertes en table
- Design responsive Bootstrap


## 💡 Idées futures (TODO)

- 📤 Ajout d’un bouton pour télécharger les logs
- 📈 Sauvegarde des alertes dans une base de données SQLite
- 📨 Envoi automatique d’emails pour certaines alertes critiques
- 📄 Génération de rapports hebdomadaires (PDF/HTML)


## 👤 Auteur

**Donbeni Imboyo Muanambelo**  
Étudiant passionné de cybersécurité & DevSecOps  
🔗 GitHub : [@Donblack12](https://github.com/Donblack12)

Ce projet est distribué sous la licence MIT. Vous pouvez l’utiliser, le modifier et le diffuser librement.
