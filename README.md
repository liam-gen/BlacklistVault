<div align="center">
	<br />
	<p>
		<h1>BlacklistVault - Centralized Blacklist Checker</h1>
	</p>
	<br />
	<p>
		<img src="https://img.shields.io/badge/python-3.11-blue" alt="Python 3.11" />
		<img src="https://img.shields.io/badge/FastAPI-0.100-green" alt="FastAPI" />
		<img src="https://img.shields.io/badge/license-MIT-lightgrey" alt="LICENCE MIT" />
	</p>
</div>

---

## Description

**BlacklistVault** est une API REST développée en **Python** avec **FastAPI** permettant centraliser différentes blacklistes (email, ip, liens, discord, ...)

Elle supporte plusieurs services et formats (JSON, HTML) et est conçue pour être facilement extensible.


> ⚠️ **Vos idées sont les bienvenues !**  
>  
> Si vous connaissez des **api de blacklist** (IP, email, Discord, liens…), n'hésitez pas à partager vos suggestions !  
>  
> Chaque contribution aide à rendre l'API plus complète et fiable.


## Fonctionnalités

- Vérification d'une adresse IP
- (bientôt) Vérification d'une adresse email
- (bientôt) Vérification d'un lien
- (bientôt) Vérification d'un fichier
- (bientôt) Vérification d'un nom de domaine
- (bientôt) Vérification d'un numéro de téléphone

---

## Idées & évolutions

- **Cache Redis** :  
  Enregistrer les résultats pour éviter les requêtes répétitives.  
  Générer une **clé MD5** unique basée sur l'adresse ip, email, etc. pour stocker/retrouver facilement les résultats.

- **Nouvelles recherches** :  
  - Adresse email  
  - Liens / URLs  
  - Fichiers  
  - Noms de domaine  
  - Numéros de téléphone

- **Intégrations possibles** :  
    - Extension navigateur
        - **Vérification en temps réel** des domaines et liens visités
        - **Analyse automatique** des fichiers téléchargés
        - **Alertes** pour les sites suspects
        - **Blocage** des sites malveillants

    - Bot Discord
        - **Vérification automatique** des utilisateurs
        - **Analyse des liens** envoyés
        - **Analyse des fichiers** envoyés

    - Intégration Gmail/Email
        - **Plugin Gmail** pour l'analyse des emails reçus
        - **Vérification des pièces jointes** avant ouverture
        - **Quarantaine automatique** des emails suspects

---

## Contribution

Les contributions sont les bienvenues !
Je suis actuellement en train de mettre en place cette partie.

---

## Roadmap

- [x] API de base avec FastAPI
- [x] Documentation automatique
- [ ] Vérification d'adresses IP
- [ ] Vérification d'emails et domaines
- [ ] Analyse de fichiers
- [ ] Analyse de liens/URLs
- [ ] Interface web d'administration
- [ ] Extension navigateur (Chrome/Firefox)
- [ ] Bot Discord
- [ ] Intégrations email (Gmail, Outlook)


---

## Licence

Ce projet est sous licence **MIT**. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

---

## Support

- **Issues GitHub** : Pour reporter des bugs ou demander des fonctionnalités
- **Email** : contact@liamcharpentier.fr
