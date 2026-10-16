import sqlite3    # Importe la bibiotèque sqlite3.
bdd = sqlite3.connect ( "db_vetements.db" )   # Ouvre le fichier de base de données.
curseur = bdd.cursor ()   # Créer un curseur.

import tkinter as tk      # Importe la bibliotèque tkinter renommé tk.
from tkinter import ttk, messagebox     # Importe les fonctions ttk et messagebox.



### TRAITEMENT DE LA TABLE TAILLE

def ajouter_taille ( c, Id_taille, Taille ) :
    ''' Vérifie si la taille existe déjà, puis ajoute une taille avec son id à la table TAILLE si elle n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_taille : un id pour la table TAILLE
            Taille : le nom de la taille
          
        POST : Ajoute la taille à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_taille FROM TAILLE
                  WHERE Id_taille = ? ;
                  """
    c.execute ( requete, ( Id_taille, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id de la taille existe déjà. Veuillez en choisir un autre." )
        return
    
    # Vérifie si la taille est déjà présente.
    requete = """ SELECT * FROM TAILLE
                  WHERE Taille = ? ;
              """
    c.execute ( requete, ( Taille, ) )
    
    # Si elle existe déjà, on informe dans la console.
    if c.fetchone () :
        print ( "La taille existe déjà dans la table." )
        return 
    
    # Insère la nouvelle taille.
    requete = """ INSERT INTO TAILLE ( Id_taille, Taille )
                  VALUES ( ?, ? ) ;
              """
    c.execute ( requete, ( Id_taille, Taille ) )
    bdd.commit ()
    
    # Informe que la taille a bien été ajoutée dans la console.
    print ( "La taille a été ajoutée avec succès !" )
    
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#ajouter_taille ( curseur, 1, 'S' )


def afficher_taille ( c ) :
    ''' Récupère le nom des tailles et leur id, puis affiche toutes les tailles disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des tailles dans la console python.
    '''
    
    # Récupère le resultat de la requête soit le nom des tailles. 
    requete = """ SELECT * FROM TAILLE ; """
    c.execute ( requete )
    tailles = c.fetchall ()
    
    # Si il n'y a aucune taille, on informe qu'il n'y a pas de tailles disponibles dans la console.
    if not tailles :
        print ( "Aucune taille trouvée." )
        
    # Sinon on affiche les tailles une par une afin de former une liste dans la console.
    else :
        print ( "Liste des tailles :" )
        for t in tailles :
            print ( f"Taille {t[0]} : {t[1]}" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_taille ( curseur )


def supprimer_taille ( c, Taille ) :
    ''' Vérifie si la taille existe, puis la supprime la taille demandée si elle existe. Sinon, on informe que cela n'est pas possible dans la console.
        PRE :
            c : le curseur
            Taille : le nom de la taille
            
        POST : Supprime la taille de la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la taille existe.
    requete = """ SELECT * FROM TAILLE
                  WHERE Taille = ( ? ) ;
              """
    c.execute ( requete, ( Taille, ) )
    # Permet de vérifier par la suite si la taille existe ou non en récupérant la première ligne du résultat.
    taille = c.fetchone ()
    
    if  not taille :
        # Informe que la taille n'existe pas dans la console.
        print ( f"Aucune taille trouvée pour {Taille}." )
        return
    Id_taille = taille[0]
        
    # Vérifie que la taille n'est pas utilisée en clé étrangère.
    requete = """ SELECT Id_taille FROM VETEMENTS
                  WHERE Id_taille = ? ;
                  """
    c.execute ( requete, ( Id_taille, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer la taille ( contrainte de référence ).
    if resultat :
        print ( "La taille est utilisée pour un vêtement, elle ne peut pas être supprimée." )
        return
    
    # Sinon on supprime la taille.
    else :
        requete = """ DELETE FROM TAILLE
                      WHERE Taille = ? ;
                  """
        c.execute ( requete, ( Taille, ) )
        bdd.commit ()
        
        # Informe que la taille a bien été supprimée dans la console.
        print ( "La taille a été supprimée avec succès." )
        
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#supprimer_taille ( curseur, 'M' )
    


### TRAITEMENT DE LA TABLE COULEUR

def ajouter_couleur ( c, Id_couleur, Couleur ) :
    ''' Vérifie si la couleur existe déjà, puis ajoute une couleur avec son id à la table COULEUR si elle n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_couleur : un id pour la table COULEUR
            Couleur : le nom de la couleur
          
        POST : Ajoute la couleur à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_couleur FROM COULEUR
                  WHERE Id_couleur = ? ;
                  """
    c.execute ( requete, ( Id_couleur, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id de la couleur existe déjà. Veuillez en choisir un autre." )
        return
    
    # Vérifie si la couleur est déjà présente.
    requete = """ SELECT * FROM COULEUR
                  WHERE Couleur = ? ;
                  """
    c.execute ( requete, ( Couleur,) )
    
    # Si elle existe déjà, on informe dans la console.
    if c.fetchone () :
        print ( "La couleur existe déjà dans la table." )
        return 
    
    # Insère la nouvelle couleur. 
    requete = """ INSERT INTO COULEUR ( Id_couleur, Couleur )
                  VALUES ( ?, ? ) ;
                  """
    c.execute ( requete, ( Id_couleur, Couleur ) )
    bdd.commit ()
    
    # Informe que la couleur a bien été ajoutée dans la console.
    print ( "La couleur a été ajoutée avec succès !" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#ajouter_couleur ( curseur, 3, 'noir' )


def afficher_couleur ( c ) :
    ''' Récupère le nom des couleurs et leur id, puis affiche toutes les couleurs disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des couleurs dans la console python.
    '''
    
    # Récupère le resultat de la requête soit le nom des couleurs. 
    requete = """ SELECT * FROM COULEUR ; """
    c.execute ( requete )
    couleurs = c.fetchall ()
    
    # Si il n'y a aucune couleur, on informe qu'il n'y a pas de couleurs disponibles dans la console.
    if not couleurs :
        print ( "Aucune couleur trouvée." )
    
    # Sinon on affiche les tailles une par une afin de former une liste dans la console.
    else :
        print ( "Liste des couleurs :" )
        for coul in couleurs :
            print ( f"Couleur {coul[0]} : {coul[1]}" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_couleur ( curseur )


def supprimer_couleur ( c, Couleur ) :
    ''' Vérifie si la couleur existe, puis la supprime la couleur demandée si elle existe. Sinon, on informe que cela n'est pas possible dans la console.
        PRE :
            c : le curseur
            Couleur : le nom de la couleur
            
        POST : Supprime la couleur de la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la couleur existe.
    requete = """ SELECT * FROM COULEUR
                  WHERE Couleur = ( ? ) ;
                  """
    c.execute ( requete, ( Couleur, ) )
    # Permet de vérifier par la suite si la couleur existe ou non en récupérant la première ligne du résultat.
    couleur = c.fetchone()  
    
    if  not couleur :
        # Informe que la couleur n'existe pas dans la console.
        print ( f"Aucune couleur trouvée pour {Couleur}." )
        return
    Id_couleur = couleur[0]
        
    # Vérifie que la couleur n'est pas utilisée en clé étrangère.
    requete = """ SELECT Id_couleur FROM VETEMENTS
                  WHERE Id_couleur = ? ;
                  """
    c.execute ( requete, ( Id_couleur, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer la couleur ( contrainte de référence ).
    if resultat :
        print ( "La couleur est utilisée pour un vêtement, elle ne peut pas être supprimée." )
    
    # Sinon on supprime la couleur.
    else :
        requete = """ DELETE FROM COULEUR
                      WHERE Couleur = ? ;
                  """
        c.execute ( requete, ( Couleur, ) )
        bdd.commit ()
        
        # Informe que la couleur a bien été supprimée dans la console.
        print ( "La couleur a été supprimée avec succès." )
        
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.      
#supprimer_couleur ( curseur, 'rouge' )
    


### TRAITEMENT DE LA TABLE MOTIF

def ajouter_motif ( c, Id_motif, Motif ) :
    ''' Vérifie si le motif existe déjà, puis ajoute un motif avec son id à la table MOTIF si il n'existe pas ou informe d'une erreur dans la consol.
        PRE :
            c : le curseur
            Id_motif : un id pour la table MOTIF
            Motif : le nom du motif
          
        POST : Ajoute le motif à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_motif FROM MOTIF
                  WHERE Id_motif= ? ;
                  """
    c.execute ( requete, ( Id_motif, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id du motif existe déjà. Veuillez en choisir un autre." )
        return
    
    # Vérifie si le motif est déjà présent. 
    requete = """ SELECT * FROM MOTIF
                  WHERE Motif = ? ;
                  """
    c.execute ( requete, ( Motif,) )
    
    # Si il existe déjà, on informe dans la console.
    if c.fetchone () :
        print ( "Le motif existe déjà dans la table." )
        return 
    
    # Insère le nouveau motif.
    requete = """ INSERT INTO MOTIF ( Id_motif, Motif )
                  VALUES ( ?, ? ) ;
                  """
    c.execute ( requete, ( Id_motif, Motif ) )
    bdd.commit ()
    
    # Informe que le motif a bien été ajouté dans la console.
    print ( "Le motif a été ajouté avec succès." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#ajouter_motif ( curseur, 3, 'fleur' )


def afficher_motif ( c ) :
    ''' Récupère le nom des motifs et leur id, puis affiche toutes les motifs disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des motifs dans la console python.
    '''
    
    # Récupère le resultat de la requête soit le nom des motifs.
    requete = """ SELECT * FROM MOTIF ; """
    c.execute ( requete )
    motifs = c.fetchall ()
    
    # Si il n'y a aucun motif, on informe qu'il n'y a pas de motifs disponibles dans la console.
    if not motifs :
        print ( "Aucun motif trouvé." )
    
    # Sinon on affiche les motifs un par un afin de former une liste dans la console.
    else :
        print ( "Liste des motifs :" )
        for m in motifs :
            print ( f"Motif {m[0]} : {m[1]}" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_motif ( curseur )


def supprimer_motif ( c, Motif ) :
    ''' Vérifie si le motif existe, puis supprime le motif demandé si il existe. Sinon, on informe que cela n'est pas possible dans la console.
        PRE :
            c : le curseur
            Motif : le nom du motif
            
        POST : Supprime le motif de la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si le motif existe.
    requete = """ SELECT * FROM MOTIF
                  WHERE Motif = ( ? ) ;
                  """
    c.execute ( requete, ( Motif, ) )
    # Permet de vérifier par la suite si le motif existe ou non en récupérant la première ligne du résultat.
    motif = c.fetchone()  
    
    if  not motif :
        # Informe que le motif n'existe pas dans la console.
        print ( f"Aucun motif trouvé pour {Motif}." )
        return
    Id_motif = motif[0]
        
    # Vérifie que le motif n'est pas utilisé en clé étrangère.
    requete = """ SELECT Id_motif FROM VETEMENTS
                  WHERE Id_motif = ? ;
                  """
    c.execute ( requete, ( Id_motif, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer le motif ( contrainte de référence ).
    if resultat :
        print ( "Le motif est utilisé pour un vêtement, il ne peut pas être supprimé." )
    
    # Sinon on supprime le motif.
    else :
        requete = """ DELETE FROM MOTIF
                      WHERE Motif = ? ;
                  """
        c.execute ( requete, ( Motif, ) )
        bdd.commit ()
        
        # Informe que le motif a bien été supprimé dans la console.
        print ( "Le motif a été supprimé avec succès." )
 
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#supprimer_motif ( curseur, 'carreau' )
    
    
### TRAITEMENT DE LA TABLE FOURNISSEUR

def ajouter_fournisseur ( c, Id_fournisseur, Nom_fournisseur, Pays ) :
    ''' Vérifie si le fournisseur existe déjà, puis ajoute un fournisseur avec son id à la table FOURNISSEURS si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_fournisseur : un id pour la table FOURNISSEURS
            Nom_fournisseur : le nom du fournisseur
            Pays : l'origine des produits 
          
        POST : Ajoute le fournisseur à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_fournisseur FROM FOURNISSEURS
                  WHERE Id_fournisseur = ? ;
                  """
    c.execute ( requete, ( Id_fournisseur, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id du fournisseur existe déjà. Veuillez en choisir un autre." )
        return
    
    # Vérifie si le fournisseur est déjà présent. 
    requete = """ SELECT * FROM FOURNISSEURS
                  WHERE Nom_fournisseur = ? ;
                  """
    c.execute ( requete, ( Nom_fournisseur,) )
    
    # Si il existe déjà, on informe dans la console.
    if c.fetchone () :
        print ( "Le fournisseur existe déjà." )
        return 
    
    # Insère le nouveau fournisseur.
    requete = """ INSERT INTO FOURNISSEURS ( Id_fournisseur, Nom_fournisseur, Pays )
                  VALUES ( ?, ?, ? ) ;
                  """
    c.execute ( requete, ( Id_fournisseur, Nom_fournisseur, Pays ) )
    
    # Permet de modifier la base de données.
    bdd.commit ()
    
    # Informe que le motif a bien été ajouté dans la console.
    print ( "Fournisseur ajouté avec succès." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#ajouter_fournisseur( curseur, 1, "Dior", "France" )


def afficher_fournisseur ( c ) :
    ''' Récupère le nom des fournisseurs et leur id, puis affiche toutes les fournisseurs disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des fournisseurs dans la console python.
    '''
    
    # Récupère le resultat de la requête soit le nom des fournisseurs.
    c.execute ( """ SELECT * FROM FOURNISSEURS ; """ )
    # On stocke tout les noms de fournisseur dans une variable.
    fournisseurs = c.fetchall ()
    
    # Si il n'y a aucun fournisseur, on informe qu'il n'y a pas de fournisseurs disponibles dans la console.
    if not fournisseurs :
        print ( "Aucun fournisseur trouvé." )
        
    # Sinon on affiche les fournisseurs un par un afin de former une liste dans la console.    
    else :
        print ( "Liste des fournisseurs :" )
        for fournisseur in fournisseurs :   
            print ( f"Fournisseur {fournisseur[0]} : {fournisseur[1]} en {fournisseur[2]}" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_fournisseur( curseur )
    

def enlever_fournisseur( c, Nom_fournisseur ) :
    ''' Vérifie si le fournisseur existe, puis l'enlève si il existe. Sinon, on informe que cela n'est pas possible dans la console.
        PRE :
            c : le curseur
            Nom_fournisseur : le nom du fournisseur
            
        POST : Enlève le fournisseur de la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si le fournisseur existe.
    requete = """ SELECT * FROM FOURNISSEURS
                  WHERE Nom_fournisseur = ( ? ) ;
                  """
    c.execute ( requete, ( Nom_fournisseur, ) )
    # Permet de vérifier par la suite si le fournisseur existe ou non en récupérant la première ligne du résultat.
    fournisseur = c.fetchone()  
    
    if  not fournisseur :
        # Informe que le fournisseur n'existe pas dans la console.
        print ( f"Aucun fournisseur trouvé pour {Nom_fournisseur}." )
        return
    Id_fournisseur = fournisseur[0]
        
    # Vérifie que le fournisseur n'est pas utilisé en clé étrangère.
    requete = """ SELECT Id_fournisseur FROM VETEMENTS
                  WHERE Id_fournisseur = ? ;
                  """
    c.execute ( requete, ( Id_fournisseur, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer le fournisseur ( contrainte de référence ).
    if resultat :
        print ( "Le fournisseur est utilisé pour un vêtement, il ne peut pas être supprimé." )
    
    # Sinon on supprime le fournisseur.
    else :
        requete = """ DELETE FROM FOURNISSEURS
                      WHERE Motif = ? ;
                  """
        c.execute ( requete, ( Nom_fournisseur, ) )
        bdd.commit ()
        
        # Informe que le fournisseur a bien été supprimé dans la console.
        print ( "Le fournisseur a été supprimé avec succès." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#enlever_fournisseur(curseur,"Chanel")
        

def modifier_fournisseur ( c, Nom_fournisseur, New_pays ) :
    ''' Vérifie si le fournisseur existe et récupère son id, puis le modifie si il existe. Sinon on informe qu'il n'existe pas dans la console.
        PRE :
            c : le curseur
            Nom_fournisseur : le nom du fournisseur
            New_pays : la nouvelle origine des produits du fournisseur
            
        POST : Modifie l'origine des produits dans la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si le fournisseur existe et récupère son id si oui.
    requete = """ SELECT Id_fournisseur FROM FOURNISSEURS
                  WHERE Nom_fournisseur = ? ;
                  """
    c.execute ( requete, ( Nom_fournisseur, ) )
    fournisseur = c.fetchone ()
    
    # Si il n'existe pas, on informe l'utilisateur dans la console.
    if not fournisseur :
        print ( "Le fournisseur n'existe pas." )
        return
    
    # Sinon on récupère l'id.
    Id_fournisseur = fournisseur[0]
    
    # Modifie le pays dans la base de données.
    requete = """ UPDATE FOURNISSEURS SET Pays = ?
                  WHERE Id_fournisseur = ? ;
                  """
    c.execute ( requete, ( New_pays, Id_fournisseur ) )
    bdd.commit ()       
    
    # Informe que l'origine été modifié sans problèmes dans la console.
    print ( f"L'origine de {Nom_fournisseur} a été modifiée avec succès." )
  
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#modifier_fournisseur ( curseur, 'Chanel', 'France' )
    
    

### TRAITEMENT DE LA TABLE CLIENTS
        
def ajouter_client ( c, Num_client, Nom, Prenom, Adresse) :
    ''' Vérifie si le client existe déjà, puis ajoute un client avec son id à la table CLIENTS si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Num_client : un id pour la table CLIENTS
            Nom : le nom du client
            Prenom : le prénom du client
            Adresse : l'adresse du client
          
        POST : Ajoute le client à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Num_client FROM CLIENTS
                  WHERE Num_client = ? ;
                  """
    c.execute ( requete, ( Num_client, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "Le numéro de client existe déjà. Veuillez en choisir un autre." )
        return
    
    # Vérifie si le client est déjà présent.
    requete = """ SELECT * FROM CLIENTS
                  WHERE Num_client = ? ;
                  """
    c.execute ( requete, ( Num_client, ) )
    
    # Si il existe déjà, on informe dans la console.
    if c.fetchone () :
        print ( "Le client existe déjà dans la table." )
        return 
    
    # Insère le nouveau client.
    requete = """ INSERT INTO CLIENTS ( Num_client, Nom, Prenom, Adresse )
                  VALUES ( ?, ?, ?, ? ) ;
                  """
    c.execute ( requete, ( Num_client, Nom, Prenom, Adresse ) )
    
    # Permet de modifier la base de données.
    bdd.commit ()
    
    # Vérifie que le fournisseur soit bien ajouté sans problèmes, on renvoit une phrase de confirmation dans la console.
    print ( "Client ajouté avec succès." )
    
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#ajouter_client( curseur, 344, "Delacour", "Marie", "34 Avenue Foch" )


def afficher_clients ( c ) :
    ''' Récupère le nom des clients et leur id, puis affiche toutes les clients disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des clients dans la console python.
    '''
    
    # Récupère le resultat de la requête soit le nom des clients.
    c.execute ( """ SELECT * FROM CLIENTS ; """ )
    # On stocke tout les clients dans une variable.
    clients = c.fetchall ()
    
    # Si il n'y a aucun fournisseur, on informe qu'il n'y a pas de fournisseurs disponibles dans la console.
    if not clients :
        print ( "Aucun client trouvé." )
        
    # Sinon on affiche les fournisseurs un par un afin de former une liste dans la console.    
    else :
        print ( "Liste des clients :" )
        for c in clients :   
            print ( f"Client {c[0]} : {c[1]} {c[2]} à l'adresse {c[3]}" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_clients ( curseur )    
    
    
def enlever_client( c, Num_client ) :
    ''' Vérifie si le client existe, puis l'enlève si il existe. Sinon, on informe que cela n'est pas possible dans la console.
        PRE :
            c : le curseur
            Num_client : le numéro du client
            
        POST : Enlève le client de la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si le client existe.
    requete = """ SELECT * FROM CLIENTS
                  WHERE Num_client = ( ? ) ;
                  """
    c.execute ( requete, ( Num_client, ) )
    # Permet de vérifier par la suite si le client existe ou non en récupérant la première ligne du résultat.
    client = c.fetchone()  
    
    if  not client :
        # Informe que le client n'existe pas dans la console.
        print ( f"Aucun client trouvé pour {Nom_client} {Prenom_client}." )
        return
    Num_client = client[0]
        
    # Vérifie que le client n'est pas utilisé en clé étrangère.
    requete = """ SELECT Num_client FROM ACHATS
                  WHERE Num_client = ? ;
                  """
    c.execute ( requete, ( Num_client, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer le client ( contrainte de référence ).
    if resultat :
        print ( "Le client est utilisé pour un achat, il ne peut pas être supprimé." )
    
    # Sinon on enlève le client.
    else :
        requete = """ DELETE FROM CLIENTS
                      WHERE Num_client = ? ;
                  """
        c.execute ( requete, ( Num_client, ) )
        bdd.commit ()
        
        # Informe que le client a bien été supprimé dans la console.
        print ( "Le client a été supprimé avec succès." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#enlever_client ( curseur, 344 )   
    
    
def modifier_client ( c, Num_client, New_nom = None, New_adresse = None ) :
    # L'utilisation de '...' = None permet de ne spécifier que certains attibuts, ceux qui ne sont pas renseigner prennent la valeur None
    ''' Vérifie si le client existe et récupère son id, puis le modifie si il existe. Sinon on informe qu'il n'existe pas dans la console.
        PRE :
            c : le curseur
            Num_client : le numéro du client
            New_nom : le nouveau nom du client ou None ( en cas de mariage ou divorce )
            New_adresse : la nouvelle adresse du client ou None
            
        POST : Modifie les informations du client dans la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si le client existe.
    requete = """ SELECT Num_client FROM CLIENTS
                  WHERE Num_client = ? ;
                  """
    c.execute ( requete, ( Num_client, ) )
    client = c.fetchone ()
    
    # Si il n'existe pas, on informe l'utilisateur dans la console.
    if not client :
        print ( "Le client n'existe pas." )
        return
    
    # Sinon on récupère l'id.
    Numero_c = client[0]

    # Modifie le nom.
    if New_nom is not None :
        requete = """ UPDATE CLIENTS SET Nom = ?
                      WHERE Num_client = ? ;
                      """
        c.execute ( requete, ( New_nom, Numero_c ) )
        bdd.commit ()
        
        # Informe que le nom a bien changé dans la console.
        print ( f"Le nom a été modifié avec succès !" )
    
    # Modifie l'adresse.
    if New_adresse is not None:
        requete = """ UPDATE CLIENTS SET Adresse = ?
                      WHERE Num_client = ? ;
                      """
        c.execute ( requete, ( New_adresse, Numero_c ) )
        bdd.commit ()
        
        # Informe que l'adresse a bien changé dans la console.
        print ( f"L'adresse a été modifiée avec succès !" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#modifier_client ( curseur, 344, New_nom = "Marneau", New_adresse = "34 Avenue des champs" )
    
    

### TRAITEMENT DE LA TABLE VETEMENTS
        
def nouveau_vetement ( c, Id_vetement, Nom, Taille, Couleur, Motif, Note, Prix_achat, Prix_revente, Fournisseur ) :
    ''' Vérifie si la taille existe déjà et récupère son id, si la couleur existe déjà et récupère son id, si le motif existe déjà et récupère son id, si le fournisseur existe déjà et récupère son id,
        si le vêtement existe déjà.
        Puis ajoute un vêtement avec son id à la table VETEMENTS si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_vêtement : un id pour la table VETEMENTS
            Nom : le nom du vêtement
            Taille : la taille du vêtement
            Couleur : la couleur du vêtement
            Motif : le motif du vêtement
            Note : la note du vêtement
            Prix_achat : le prix lors de l'achat du vêtement auprès du fournisseur
            Prix_revente : le prix de vente du vêtement au client
            Fournisseur : le nom du fournisseur
          
        POST : Ajoute le vêtement à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Id_vetement = ? ;
                  """
    c.execute ( requete, ( Id_vetement, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id du vêtement existe déjà. Veuillez en choisir un autre." )
        return
    
    ## Recherche de l'id de toutes les clés étrangères.
    # Recherche de l'Id de la taille à partir de son nom.
    requete = """ SELECT Id_taille FROM TAILLE
                  WHERE Taille = ? ;
                  """
    c.execute ( requete, ( Taille, ) )
    taille = c.fetchone ()
    
    # Si la taille existe, récupère son id sinon on informe que la taille n'exite pas dans la console.
    if not taille :
        print ( "La taille existe pas." )
        return
    Id_taille = taille[0]
    
    # Recherche de l'Id de la couleur à partir de son nom.
    requete = """ SELECT Id_couleur FROM COULEUR
                  WHERE Couleur = ? ;
                  """
    c.execute ( requete, ( Couleur, ) )
    couleur = c.fetchone ()
    
    # Si la couleur existe, récupère son id sinon on informe que la couleur n'exite pas dans la console.
    if not couleur :
        print ( "La couleur n'existe pas." )
        return
    Id_couleur = couleur[0]
    
    # Recherche de l'Id du motif à partir de son nom.
    requete = """ SELECT Id_motif FROM MOTIF
                  WHERE Motif = ? ;
                  """
    c.execute ( requete, ( Motif, ) )
    motif = c.fetchone ()
    
    # Si le motif existe, récupère son id sinon on informe que le motif n'exite pas dans la console.
    if not motif:
        print ( "Le motif n'existe pas." )
        return
    Id_motif = motif[0]
     
    # Recherche de l'Id du fournisseur à partir de son nom.
    requete = """ SELECT Id_fournisseur FROM FOURNISSEURS
                  WHERE Nom_fournisseur = ? ;
                  """
    c.execute ( requete, ( Fournisseur, ) )
    fournisseur = c.fetchone ()
    
    # Si le fournisseur existe, récupère son id sinon on informe qu'il n'exite pas dans la console.
    if not fournisseur :
        print ( "Le fournisseur n'existe pas." )
        return
    Id_fournisseur = fournisseur[0]
    
    # Vérifie si le vêtement existe déjà.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? AND Id_taille = ? AND Id_couleur = ? AND Id_motif = ? AND Id_fournisseur = ? ;
                  """
    c.execute ( requete, ( Nom, Id_taille, Id_couleur, Id_motif, Id_fournisseur ) )
    ex_stock = c.fetchone ()
    
    # Si il existe, on informe qu'il existe déjà dans la console.
    if ex_stock :
        print ( "Ce vêtement existe déjà." )
        return
    
    # Sinon on ajoute le nouveau vêtement.
    requete = """ INSERT INTO VETEMENTS ( Id_vetement, Nom, Id_taille, Id_couleur, Id_motif, Note, Prix_achat, Prix_revente, Id_fournisseur )
                  VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?) ;
                  """
    c.execute ( requete, ( Id_vetement,  Nom, Id_taille, Id_couleur, Id_motif, Note, Prix_achat, Prix_revente, Id_fournisseur ) )
    bdd.commit ()
    
    # Informe que le vêtement a bien été ajouté dans la console.
    print ( f"Le vêtement a été ajouté avec succès !" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#nouveau_vetement ( curseur, 567, "JUGGGGG", 'M', 'noir', 'uni', 8, 400, 45678, 'Dior' )
    
    
def afficher_vetements ( c ):
    ''' Récupère le nom des vêtements et leur id, puis affiche tous les vêtements disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des vêtements dans la console python.
    '''
    
    # Récupère les informations sur les vêtements.
    requete = """ SELECT Id_vetement, Nom, Taille, Couleur, Motif, Note, Prix_revente, Nom_fournisseur FROM VETEMENTS
                  JOIN TAILLE ON VETEMENTS.Id_taille = TAILLE.Id_taille
                  JOIN COULEUR ON VETEMENTS.Id_couleur = COULEUR.Id_couleur
                  JOIN MOTIF ON VETEMENTS.Id_motif = MOTIF.Id_motif
                  JOIN FOURNISSEURS ON VETEMENTS.Id_fournisseur = FOURNISSEURS.Id_fournisseur ;
                  """
    c.execute ( requete )
    vetements = c.fetchall ()
    
    # Si il n'y a aucun vêtement, on informe qu'il n'y a pas de vêtements disponibles dans la console.
    if not vetements :
        print ( "Aucun vêtement trouvé." )
        
    # Sinon on affiche les fournisseurs un par un afin de former une liste dans la console.
    else :
        print ( "Liste des vêtements :" )
        for v in vetements :
            print ( f" Vêtement {v[0]} : {v[1]} {v[3]} à motif {v[4]} en taille {v[2]} de {v[7]} avec une note de {v[5]} au prix de {v[6]} " )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_vetements ( curseur )
    
    
def supprimer_vetement ( c, Nom, Taille, Couleur, Motif, Fournisseur ) :
    ''' Vérifie si la taille existe déjà et récupère son id, si la couleur existe déjà et récupère son id, si le motif existe déjà et récupère son id, si le fournisseur existe déjà et récupère son id,
        si le vêtemtn existe déjà.
        Puis supprime le vêtement de la table VETEMENTS si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_vêtement : un id pour la table VETEMENTS
            Nom : le nom du vêtement
            Taille : la taille du vêtement
            Couleur : la couleur du vêtement
            Motif : le motif du vêtement
            Note : la note du vêtement
            Prix_achat : le prix lors de l'achat du vêtement auprès du fournisseur
            Prix_revente : le prix de vente du vêtement au client
            Fournisseur : le nom du fournisseur
          
        POST : Supprime le vêtement à la base de données ou informe d'une erreur dans la console.
    '''
    
    ## Recherche de l'id de toutes les clés étrangères.
    # Recherche de l'Id de la taille  à partir de son nom.
    requete = """ SELECT Id_taille FROM TAILLE
                  WHERE Taille = ? ;
                  """
    c.execute ( requete, ( Taille, ) )
    taille = c.fetchone ()
    
    # Si la taille existe, récupère son id sinon on informe que la taille n'exite pas dans la console.
    if not taille :
        print ( "La taille n'existe pas." )
        return
    Id_taille = taille[0]
    
    # Recherche de l'Id de la couleur  à partir de son nom.
    requete = """ SELECT Id_couleur FROM COULEUR
                  WHERE Couleur = ? ;
                  """
    c.execute ( requete, ( Couleur, ) )
    couleur = c.fetchone ()
    
    # Si la couleur existe, récupère son id sinon on informe que la couleur n'exite pas dans la console.
    if not couleur :
        print ( "La couleur n'existe pas." )
        return
    Id_couleur = couleur[0]
    
    # Recherche de l'Id du motif à partir de son nom.
    requete = """ SELECT Id_motif FROM MOTIF
                  WHERE Motif = ? ;
                  """
    c.execute ( requete, ( Motif, ) )
    motif = c.fetchone ()
    
    # Si le motif existe, récupère son id sinon on informe que le motif n'exite pas dans la console.
    if not motif:
        print ( "Le motif n'existe pas." )
        return
    Id_motif = motif[0]
     
    # Recherche de l'Id du fournisseur à partir de son nom.
    requete = """ SELECT Id_fournisseur FROM FOURNISSEURS
                  WHERE Nom_fournisseur = ? ;
                  """
    c.execute ( requete, ( Fournisseur, ) )
    fournisseur = c.fetchone ()
    
    # Si le fournisseur existe, récupère son id sinon on informe qu'il n'exite pas dans la console.
    if not fournisseur :
        print ( "Le fournisseur n'existe pas." )
        return
    Id_fournisseur = fournisseur[0]
    
    # Vérifie que le vêtement existe.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? AND Id_taille = ? AND Id_couleur = ? AND Id_motif = ? AND Id_fournisseur = ? ;
                  """
    c.execute ( requete, ( Nom, Id_taille, Id_couleur, Id_motif, Id_fournisseur ) )
    vetement = c.fetchone ()
      
    if  not vetement :
        # Informe que le vêtement n'existe pas dans la console.
        print ( f"Aucun vêtement trouvé pour {Nom}." )
        return
    Id_vetement = vetement[0]
        
    # Vérifie que le vêtement n'est pas utilisé en clé étrangère de STOCK.
    requete = """ SELECT Id_vetement FROM STOCK
                  WHERE Id_vetement = ? ;
                  """
    c.execute ( requete, ( Id_vetement, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer le vêtement ( contrainte de référence ).
    if resultat :
        print ( "Le vêtement est utilisé pour un stock, il ne peut pas être supprimé." )
        return
     
    # Vérifie que le vêtement n'est pas utilisé en clé étrangère de ACHATS.
    requete = """ SELECT Id_vetement FROM ACHATS
                  WHERE Id_vetement = ? ;
                  """
    c.execute ( requete, ( Id_vetement, ) )
    resultat = c.fetchone ()
    
    # Si le résultat contient une au moins un vêtement avec cet id, on informe que l'on ne peut pas supprimer le vêtement ( contrainte de référence ).
    if resultat :
        print ( "Le vêtement est utilisé pour un achat, il ne peut pas être supprimé." )
        return
    
    # Sinon on supprime le vêtement.
    else :
        requete = """ DELETE FROM VETEMENTS
                      WHERE Nom = ? ;
                  """
        c.execute ( requete, ( Nom, ) )
        bdd.commit ()
        
        # Informe que le vêtement a bien été supprimé dans la console .
        print ( "Le vêtement a été supprimé avec succès." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#supprimer_vetement ( curseur, "Jean", 'M', 'rouge', 'carreau', 'Chanel' )
    
    
def modifier_vetement ( c, Nom, New_taille = None, New_couleur = None, New_motif = None, New_fournisseur = None, New_prix_achat = None, New_prix_revente = None, New_note = None ) :
    # L'utilisation de '...' = None permet de ne spécifier que certains attibuts, ceux qui ne sont pas renseigner prennent la valeur None
    ''' Vérifie si la taille existe déjà et récupère son id, si la couleur existe déjà et récupère son id, si le motif existe déjà et récupère son id, si le fournisseur existe déjà et récupère son id,
        si le vêtemtn existe déjà.
        Puis modifie le vêtement de la table VETEMENTS, si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Nom : le nom du vêtement
            New_taille : la nouvelle taille du vêtement ou None
            New_couleur : la nouvelle couleur du vêtement ou None
            New_motif : le nouveau motif du vêtement ou None
            New_note : la nouvelle note du vêtement ou None
            New_prix_achat : le nouveau prix lors de l'achat du vêtement auprès du fournisseur ou None
            New_prix_revente : le nouveau prix de vente du vêtement au client ou None
            New_fournisseur : le nom du fournisseur ou None
          
        POST : Modifie le vêtement à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si le vêtement existe et récupère son id si oui.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom, ) )
    vetement = c.fetchone ()
    
    # Si il n'existe pas, on informe l'utilisateur dans la console.
    if not vetement :
        print ( "Le vêtement n'existe pas." )
        return
    
    # Sinon on récupère l'id.
    Id_vetement = vetement[0]
    
    ## Modifie les champs spécifiés.
    # Modifie la taille.
    if New_taille :
        requete = """ SELECT Id_taille FROM TAILLE
                      WHERE Taille = ? ;
                      """
        c.execute ( requete, ( New_taille, ) )
        taille = c.fetchone ()
        
        # Vérifie si la taille existe puis modifie la taille du vêtement dans la base de données.
        if taille :
            Id_taille = taille[0]
            requete = """ UPDATE VETEMENTS SET Id_taille = ?
                          WHERE Id_vetement = ? ;
                          """
            c.execute ( requete, ( Id_taille, Id_vetement ) )
            bdd.commit ()
            
            # Informe que la taille a bien changé dans la console.
            print ( "La taille du vêtement a été changé avec succès !" )
        
        # Si la taille n'existe pas, on informe dans la console.
        else :
            print ( "La taille n'existe pas." )
        
    # Modifie la couleur.
    if New_couleur :
        requete = """ SELECT Id_couleur FROM COULEUR
                      WHERE Couleur = ? ;
                      """
        c.execute ( requete, ( New_couleur, ) )
        couleur = c.fetchone ()
        
        # Vérifie si la couleur existe puis modifie la couleur du vêtement dans la base de données.
        if couleur :
            Id_couleur = couleur[0]
            requete = """ UPDATE VETEMENTS SET Id_couleur = ?
                          WHERE Id_vetement = ? ;
                          """
            c.execute ( requete, (Id_couleur, Id_vetement) )
            bdd.commit ()
            
            # Informe que la couleur a bien changé dans la console.
            print ( "La couleur du vêtement a été changé avec succès !" )
        
        # Si la couleur n'existe pas, on informe dans la console.
        else :
            print ( "La couleur n'existe pas." )
            
    # Modifie le motif.
    if New_motif :
        requete = """ SELECT Id_motif FROM MOTIF
                      WHERE Motif = ? ;
                      """
        c.execute ( requete, ( New_motif, ) )
        motif = c.fetchone ()
        
        # Vérifie si le motif existe puis modifie le motif du vêtement dans la base de données.
        if motif :
            Id_motif = motif[0]
            requete = """ UPDATE VETEMENTS SET Id_motif = ?
                          WHERE Id_vetement = ? ;
                          """
            c.execute ( requete, (Id_motif, Id_vetement) )
            bdd.commit ()
            
            # Informe que le motif a bien changé dans la console.
            print ( "Le motif du vêtement a été changé avec succès." )
        
        # Si le motif n'existe pas, on informe dans la console.
        else :
            print ( "Le motif n'existe pas." )
     
    # Modifie le fournisseur.
    if New_fournisseur :
        requete = """ SELECT Id_fournisseur FROM FOURNISSEURS
                      WHERE Nom_fournisseur = ? ;
                      """
        c.execute ( requete, ( New_fournisseur, ) )
        fournisseur = c.fetchone ()
        
        # Vérifie si le fournisseur existe puis modifie le fournisseur du vêtement dans la base de données.
        if fournisseur :
            Id_fournisseur = fournisseur[0]
            requete = """ UPDATE VETEMENTS SET Id_fournisseur = ?
                          WHERE Id_vetement = ? ;
                          """
            c.execute ( requete, (Id_fournisseur, Id_vetement) )
            bdd.commit ()
            
            # Informe que le fournisseur a bien changé dans la console.
            print ( "Le fournisseur du vêtement a été changé avec succès." )
        
        # Si le fournisseur n'existe pas, on informe dans la console.
        else :
            print ( "Le fournisseur n'existe pas." )
        
    # Modifie le prix d'achat.
    if New_prix_achat is not None :
        requete = """ UPDATE VETEMENTS SET Prix_achat = ?
                      WHERE Id_vetement = ? ;
                      """
        c.execute ( requete, ( New_prix_achat, Id_vetement ) )
        bdd.commit ()
        
        # Informe que le prix d'achat a bien changé dans la console.
        print ( f"Le prix d'achat a été modifié avec succès !" )
    
    # Modifie le prix de revente.
    if New_prix_revente is not None :
        requete = """ UPDATE VETEMENTS SET Prix_revente = ?
                      WHERE Id_vetement = ? ;
                      """
        c.execute ( requete, ( New_prix_revente, Id_vetement ) )
        bdd.commit ()
        
        # Informe que le prix de revente a bien changé dans la console.
        print ( f"Le prix de revente a été modifié avec succès !" )
     
    # Modifie la note.
    if New_note is not None :
        requete = """ UPDATE VETEMENTS SET Note = ?
                      WHERE Id_vetement = ? ;
                      """
        c.execute ( requete, ( New_note, Id_vetement ) )
        bdd.commit ()
        
        # Informe que la note a bien changé dans la console.
        print ( f"La note a été modifié avec succès !" )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#modifier_vetement ( curseur, "Robe", New_taille = "XS", New_couleur = 'noir', New_motif = "fleur",New_fournisseur = 'Dior', New_prix_achat = 300, New_prix_revente = 500, New_note = 7 )
    


### TRAITEMENT DE LA TABLE STOCK
        
def nouveau_stock ( c, Id_stock, Nom_vetement, Nb_vetements, Lieu ) :
    ''' Vérifie si le vêtement existe déjà et récupère son id, si le stock existe déjà, puis ajoute un stock avec son id à la table STOCK si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_stock : un id pour la table STOCK
            Nom_vetement : le nom du vêtement à mettre dans le stock
            Lieu : le lieu de stockage du vêtement
          
        POST : Ajoute le stock à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_stock FROM STOCK
                  WHERE Id_stock = ? ;
                  """
    c.execute ( requete, ( Id_stock, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id du stock existe déjà. Veuillez en choisir un autre." )
        return
    
    # Recherche de l'Id du vêtement  à partir de son nom si il existe.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone ()
    
    # Si le vêtement existe, récupère son id.
    if vetement :
        Id_vetement = vetement[0]
        
    # Informe que le vêtement n'exite pas dans la console.
    else :
        print ( "Le vêtement n'existe pas." )
        return
        
    # Vérifie si le stock existe déjà pour ce vêtement et ce lieu.
    requete = """ SELECT Id_stock FROM STOCK
                  WHERE Id_vetement = ? AND Lieu = ? ;
                  """
    c.execute ( requete, ( Id_vetement, Lieu ) )
    ex_stock = c.fetchone ()
    
    # Si il existe, on informe qu'il existe déjà dans la console.
    if ex_stock :
        print ( f"Le stock de {Nom_vetement} à {Lieu} existe déjà." )
        return
    
    # Sinon on ajoute le nouveau stock à la base de données.
    requete = """ INSERT INTO STOCK ( Id_stock, Id_vetement, Nb_vetements, Lieu )
                  VALUES ( ?, ?, ?, ? ) ;
                  """
    c.execute ( requete, ( Id_stock, Id_vetement, Nb_vetements, Lieu ) )
    bdd.commit ()
    
    # Informe que le stock a bien été ajouté dans la console.
    print ( f"Le stock de {Nb_vetements} {Nom_vetement} à {Lieu} a été ajouté avec succès." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#nouveau_stock ( curseur, 8, "Veste", 30, "Paris" )
    
    
def afficher_stock ( c ) :
    ''' Récupère le nom des stocks et leur id, puis affiche toutes les stock disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des stock dans la console python.
    '''
    
    # Récupère les informations sur le stock.
    requete = """ SELECT Nom, Nb_vetements, Lieu FROM STOCK
                  JOIN VETEMENTS ON STOCK.Id_vetement = VETEMENTS.Id_vetement ;""" 
    c.execute ( requete )
    stocks = c.fetchall ()
    
    # Si il n'y a aucun stock, on informe qu'il n'y a pas de stocks disponibles dans la console.
    if not stocks :
        print ( "Aucun stock trouvé." )
        
    # Sinon on affiche les fournisseurs un par un afin de former une liste dans la console.  
    else :
        print ( "Liste des stocks :" )
        for s in stocks :
            print ( f" {s[1]} {s[0]} à {s[2]}" )  

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_stock ( curseur )    
    
    
def supprimer_stock ( c, Nom_vetement, Lieu ) :
    ''' Récupère l'id du vêtement si il existe, sinon on informe qu'il n'existe pas dans la console et une fenêtre pop.
        Vérifie si le stock existe et récupère son id, puis le modifie si il existe. Sinon on informe qu'il n'existe pas dans la console.
        PRE :
            c : le curseur
            Nom_vetement : le nom du vêtement que l'on veut supprimer du stock
            Lieu : le lieu de ce vêtement
            
        POST : Supprime le stock dans la base de données ou informe d'une erreur dans la console.
    '''
    
    # Recherche de l'Id du vêtement à partir de son nom.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone ()
    
    # Si le vêtement existe, récupère son id.
    if vetement :
        Id_vetement = vetement[0]
        
    # Informe que le vêtement n'exite pas dans la console.
    else :
        print ( "Le vêtement n'existe pas." )
        return
        
    # Vérifie si le stock existe déjà pour ce vêtement et ce lieu.
    requete = """ SELECT Id_stock FROM STOCK
                  WHERE Id_vetement = ? AND Lieu = ? ;
                  """
    c.execute ( requete, ( Id_vetement, Lieu ) )
    ex_stock = c.fetchone ()  
    
    if ex_stock :
        # Supprime le stock.
        requete = """ DELETE FROM STOCK
                      WHERE Id_vetement = ? AND Lieu = ? ;
                      """
        c.execute ( requete, ( Id_vetement, Lieu) )
        bdd.commit ()
        
        # Informe que le stock a bien été supprimé dans la console.
        print ( "Le stock a été supprimé avec succès." )
    
    else :
        # Informe que le stock n'existe pas dans la console.
        print ( f"Aucun stock trouvé pour {Nom_vetement}." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#supprimer_stock ( curseur,"Veste", "Paris" )
    
    
def ajouter_dans_stock ( c, Nom_vetement, Nb_en_plus, Lieu ) :
    ''' Vérifie si le vêtement existe et récupère son id, si le stock existe. Si oui, on ajoute la quantité en plus dans le stock existant.
        Sinon on informe qu'il n'existe pas dans la console .
        PRE :
            c : le curseur
            Nom_vetement : le nom du vêtement 
            Nb_en_plus : la quantité à ajouter en plus pour ce vêtement
            Lieu : le lieu du stock
            
        POST : Ajoute une quantité du stock pour le vêtement spécifié dans la base de données ou informe d'une erreur dans la console.
    '''
    
    # Recherche de l'Id du vêtement  à partir de son nom.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone ()
    
    # Si le vêtement existe, récupère son id.
    if vetement :
        Id_vetement = vetement[0]
        
    # Informe que le vêtement n'existe pas dans la console.
    else :
        print ( "Le vêtement n'existe pas." )
        return
    
    # Vérifie si le stock existe déjà pour ce vêtement et ce lieu.
    requete = """ SELECT Id_stock, Nb_vetements FROM STOCK
                  WHERE Id_vetement = ? AND Lieu = ? ;
                  """
    c.execute ( requete, ( Id_vetement, Lieu ) )
    ex_stock = c.fetchone ()
    
    # Si le stock existe,on ajoute la quantité à l'existant.
    if ex_stock :
        requete = """ UPDATE STOCK SET Nb_vetements = Nb_vetements + ?
                      WHERE Id_stock = ? ;
                      """
        c.execute ( requete , ( Nb_en_plus, ex_stock[0] ) )
        bdd.commit ()
        
        # Informe que la quantité a bien changé dans la console.
        print ( f"{Nb_en_plus} {Nom_vetement} ont été ajoutés au stock avec succès ! " )
        
    # Sinon on informe que le stock n'existe pas dans la console.
    else :
        print ( "Le stock n'existe pas, veuiller en créer un." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#ajouter_dans_stock ( curseur, "Jean", 10, "Paris" )


def enlever_du_stock ( c, Nom_vetement, Lieu, Quantite ) :
    ''' Vérifie si le vêtement existe et récupère son id, si le stock existe. Si oui, on retire la quantité dans le stock existant si possible.
        Sinon on informe qu'il n'existe pas dans la console.
        PRE :
            c : le curseur
            Nom_vetement : le nom du vêtement 
            Nb_en_plus : la quantité à ajouter en plus pour ce vêtement
            Lieu : le lieu du stock
            
        POST : Retire une quantité du stock pour le vêtement spécifié dans la base de données ou informe d'une erreur dans la console.
    '''
    
    # Recherche de l'Id du vêtement à partir de son nom.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone ()
    
    # Si le vêtement existe, récupère son id.
    if vetement :
        Id_vetement = vetement[0]
        
    # Informe que le vêtement n'existe pas dans la console. 
    else :
        print ( "Le vêtement n'existe pas." )
        return
    
    # Vérifie si le stock existe pour ce vêtement et ce lieu.
    requete = """ SELECT Id_stock, Nb_vetements FROM STOCK
                  WHERE Id_vetement = ? AND Lieu = ? ;
                  """
    c.execute ( requete, ( Id_vetement, Lieu ) )
    ex_stock = c.fetchone ()
    
    # Si le stock existe, on met la quantité restante dans une variable.
    if ex_stock :
        quantite_actuelle = ex_stock[1]
        
        # Si le stock est suffisant, on soustrait la quantité vendu.
        if quantite_actuelle >= Quantite :
            requete = """ UPDATE STOCK SET Nb_vetements = Nb_vetements - ?
                          WHERE Id_stock = ? ;
                          """
            c.execute ( requete, ( Quantite, ex_stock[0] ) )
            bdd.commit ()
            
            # Informe que la quantite a bien été enlevée dans la console..
            print ( f"{Quantite} {Nom_vetement} à {Lieu} a été enlevé avec succès ! " )
            
        # Sinon on informe qe ce n'est pas possible d'enlever la quantité voulue dans la console.
        else :
            print ( f"Le nombre de {Nom_vetement} en stock est insuffisant pour pouvoir en enlever {Quantite}." )
            
    # Si le stock n'existe pas, on informe l'utilisateur dans la console.
    else :
        print ( "Aucun stock trouvé." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#enlever_du_stock ( curseur, "Jean", "Paris", 4 )
    
    
    
### TRAITEMENT DE LA TABLE ACHATS
        
def nouvelle_commande ( c, Id_achat, Nom_client, Prenom_client, Adresse_client, Nom_vetement, Quantite, Date_achat, Num_commande, Lieu ) :
    ''' Vérifie si le vêtement existe déjà et récupère son id, si le stock est suffisant pour la commande, si le client existe déjà et récupère son id, si la commande existe déjà.
        Puis ajoute une commande avec son id à la table ACHATS si il n'existe pas ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Id_achat : un id pour la table ACHATS
            Nom_client : le nom du client
            Prenom_client : le prénom du client
            Adresse_client : l'adresse du client
            Nom_vetement : le nom du vêtement
            Quantite : la quantité du vêtement commandée
            Date_achat : la date d'achat de l'article
            Num_commande : le numéro de la commande 
            Lieu : le lieu de l'achat
          
        POST : Ajoute la commande à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Vérifie si la clé primaire existe déjà.
    requete = """ SELECT Id_achat FROM ACHATS
                  WHERE Id_achat = ? ;
                  """
    c.execute ( requete, ( Id_achat, ) )
    resultat = c.fetchone ()
    
    # Informe que la clé primaire existe déjà dans la console.
    if resultat :
        print( "L'id de l'achat existe déjà. Veuillez en choisir un autre." )
        return
    
    # Vérifie si le vêtement existe.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement= c.fetchone ()
    
    # Si le vêtement n'existe pas, on informe dans la console.
    if not vetement :
        print ( "Le vêtement n'existe pas." )
        return
    Id_vetement = vetement[0]
    
    # Vérifie si le stock est suffisant et existant.
    requete = """ SELECT Nb_vetements FROM STOCK
                  WHERE Id_vetement = ? AND Lieu = ? ;
                  """
    c.execute ( requete, ( Id_vetement, Lieu ) )
    stock = c.fetchone ()
    
    # Si le stock est insuffisant ou inexistant, on informe dans la console.
    if not stock or stock[0] < Quantite :
        print ( "Stock insuffisant." )
        return
    
    # Vérifie si le client existe, si non on l'ajoute.
    requete = """ SELECT Num_client FROM CLIENTS
                  WHERE Nom = ? AND Prenom = ? AND Adresse = ? ;
                  """
    c.execute ( requete, ( Nom_client, Prenom_client, Adresse_client ) )
    client = c.fetchone ()
    
    # Si le client existe pas, on informe dans la console.
    if not client :
        print ( "Le client n'existe pas. Veuillez l'ajouter." )
        return
    Num_client = client[0]
    
    # Vérifie si la commande existe déjà
    requete = """ SELECT Id_achat FROM ACHATS
                  WHERE Quantite = ? AND Num_commande =? AND Date_achat = ? AND Num_client = ? AND Id_vetement = ? ; """
    c.execute ( requete, ( Quantite, Num_commande, Date_achat, Num_client, Id_vetement ) )
    achat = c.fetchone ()
    
    # Si il existe, on informe qu'il existe déjà dans la console.
    if achat :
        print ( "Cette commande existe déjà." )
        return
    
    # Ajoute la commande a la base de données.
    requete = """ INSERT INTO ACHATS ( Id_achat, Quantite, Num_commande, Date_achat, Num_client, Id_vetement )
                  VALUES ( ?, ?, ?, ?, ?, ? ) ;
                  """
    c.execute ( requete, ( Id_achat, Quantite,  Num_commande,  Date_achat, Num_client, Id_vetement ) )
    bdd.commit ()
    
    # Informe que la commande a été ajouté dans la console.
    print ( "La commande a été ajouté avec succès." )
    
    # Met le stock à jour.
    gs.enlever_du_stock ( c, Nom_vetement, Lieu, Quantite )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#nouvelle_commande ( curseur, 93, 'Delacour', "Marie", "34 Avenue Foch", "Jean", 2, "41/12/2024", 4678, "Paris" )    
    
    
def afficher_commandes ( c ):
    ''' Récupère les commande et leur id, puis affiche toutes les commandes disponibles dans la base de données dans la console python.
        PRE :
            c : le curseur
            
        POST : Affiche la liste des commandes dans la console python.
    '''
    
    # Récupère les informations sur les commandes. 
    requete = """ SELECT Quantite, Num_commande, Date_achat, CLIENTS.Nom , CLIENTS.Prenom, VETEMENTS.Nom FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement
                  JOIN CLIENTS ON ACHATS.Num_client = CLIENTS.Num_client ;
                  """
    c.execute ( requete )
    commandes = c.fetchall ()
    
    # Si il n'y a aucun vêtement, on informe qu'il n'y a pas de vêtements disponibles dans la console.
    if not commandes :
        print ( "Aucune commande trouvé" )
        
    # Sinon on affiche les fournisseurs un par un afin de former une liste dans la console.
    else :
        print ( "Liste des commandes :" )
        for c in commandes :
            print ( f" Commande {c[1]} : {c[0]} {c[5]} acheté par {c[3]} {c[4]} le {c[2]} " )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#afficher_commandes( curseur )     
    
 
def retour_articles( c, Nom_client, Prenom_client, Adresse_client, Nom_vetement, Quantite_retour, Lieu, Date_achat ):
    ''' Vérifie si le client existe déjà et récupère son id, si le client existe déjà et récupère son id, si la commande existe déjà.
        Vérifie si la quantité retournée est valide, réintègre dans le stock les vêtements et met à jour la commande dans la table ACHATS.
        Si il y a un problème, on informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Nom_client : le nom du client
            Prenom_client : le prénom du client
            Adresse_client : l'adresse du client
            Nom_vetement : le nom du vêtement
            Quantite_retour : la quantité du vêtement commandée à retourner
            Date_achat : la date d'achat de l'article
            Lieu : le lieu de l'achat
          
        POST : Gère le retour de la commande à la base de données ou informe d'une erreur dans la console.
    '''
    
    # Récupére le numéro du client.
    requete = """ SELECT Num_client FROM CLIENTS
                  WHERE Nom = ? AND Prenom = ? AND Adresse = ? ;
                  """
    c.execute ( requete, ( Nom_client, Prenom_client, Adresse_client ) )
    client = c.fetchone()
      
    # Si le client n'existe pas, on informe dans la console.
    if not client:
        print ( f"Aucun client trouvé." )
        return
    Num_client = client[0]

    # Récupére l'id du vêtement.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone()
        
    # Si le vêtement n'existe pas, on informe dans la console.
    if not vetement:
        print ( f"Le vêtement n'existe pas." )
        return
    Id_vetement = vetement[0]

    # Vérifie si la commande existe.
    requete = """ SELECT Id_achat, Quantite FROM ACHATS
                  WHERE Num_client = ? AND Id_vetement = ? AND Date_achat = ? ;
                  """
    c.execute( requete, ( Num_client, Id_vetement, Date_achat) )
    commande = c.fetchone()
        
    # Si la commande n'existe pas, on informe dans la console.
    if not commande:
        print ( "Aucune commande trouvée." )
        return

    Id_achat = commande[0]
    Quantite_commande = commande[1]

    # Vérifie si la quantité retournée est valide, que la quantité retournée ne dépasse pas la quantité vendu.
    if Quantite_retour > Quantite_commande:
        print ( "La quantité retournée dépasse la quantité commandée." )
        return

    # Réintégre les articles au stock.
    ajouter_dans_stock ( c, Nom_vetement, Quantite_retour, Lieu )

    # Met à jour ou supprime la commande.
    # Supprimer la commande si tout est retourné.
    if Quantite_retour == Quantite_commande:
        requete = """ DELETE FROM ACHATS
                      WHERE Id_achat = ? ;
                      """
        c.execute( requete, (Id_achat,))
        bdd.commit ()
    
        # Informe que la commande a été supprimée dans la console.
        print ( f"La commande pour {Nom_vetement} a été entièrement supprimée." )
        
    # Réduit la quantité restante de la commande.
    else :
        nouvelle_quantite = Quantite_commande - Quantite_retour
        requete = """ UPDATE ACHATS SET Quantite = ?
                      WHERE Id_achat = ? ;
                      """
        c.execute( requete, (nouvelle_quantite, Id_achat) )
        bdd.commit ()
        
        # Informe que la comma nde a été mise à jour dans la console.
        print ( f"{Quantite_retour} {Nom_vetement} retournées. Commande mise à jour avec {nouvelle_quantite} unités restantes." )
        
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.        
#retour_articles( curseur, "Delacour", "Marie", "34 Avenue Foch", "Jean", 1, "Paris", "09/12/2024" )
#retour_articles( curseur, "Delacourt", "Marie", "34 Avenue des champs", "Robe", 2, "Paris", "09/12/2024" )

    
def calcule_prix_total_commande ( c, Date_achat, Nom_client, Prenom_client, Adresse_client ) :
    ''' Récupère le numéro du client et de la commande, puis calcule le prix total d'une commande.
        Si il y a un problème on informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Date_achat : la date lors de l'achat de la commande
            Nom_client : le nom du client
            Prenom_client : le prenom du client
            Adresse_client : l'adresse du client
            
        POST : Affiche le prix total d'une commande ou informe d'une erreur dans la console. 
    '''
    
    # Récupère le numéro du client.
    requete = """ SELECT Num_client FROM CLIENTS
                  WHERE Nom = ? AND Prenom = ? AND Adresse = ? ;
                  """
    c.execute ( requete, ( Nom_client, Prenom_client, Adresse_client ) )
    client = c.fetchone()
      
    # Si le client n'existe pas, on informe dans la console.
    if not client:
        print ( f"Aucun client trouvé." )
        return
    Num_client = client[0]
    
    # Récupère le numéro de la commande.
    requete = """ SELECT Num_commande FROM ACHATS
                  WHERE Num_client = ? AND Date_achat = ? ;
                  """
    c.execute ( requete, ( Num_client, Date_achat ) )
    com = c.fetchone()
     
    # Si la commande n'existe pas, on informe dans la console.
    if not com:
        print ( f"Aucune commande trouvée." )
        return
    Num_commande = com[0]
    
    # Récupère la quantité et le prix de revente liés à chaque articles de la commande.
    requete = """ SELECT SUM (Quantite * Prix_revente) FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement
                  WHERE Num_commande= ? ;
                  """
    c.execute ( requete, ( Num_commande, ) )
    total = c.fetchone ()
    
    # Affiche le total de la commande dans la console.
    print ( f" Le total de la commande pour {Nom_client} {Prenom_client} le {Date_achat} est de {total[0]}." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
    


### TRAITEMENT DES FINANCES

def benefice_un_vetement ( c, Nom_vetement ) :
    ''' Récupère les informations sur le vêtement. Puis on calcule la quantité vendu du vêtement et son bénéficce sur la totalité de ses ventes.
        Ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Nom_vetement : le nom du vêtement
            
        POST : Affiche le bénéfice sur la totalité des ventes de ce vêtements ou informe d'une erreur dans la console.
    '''

    # Récupère l'id du vêtement.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone ()
    
    # Si le vêtements n'existe pas, on informe dans la console.
    if not vetement :
        print ( f"Aucun vêtement trouvé." )
        return
    
    # Sinon on enregistre dans 3 variables differentes le contenu de la variable vêtement.
    Id_vetement = vetement[0]
    
    # Calcule le bénéfice vendu de ce vêtement.
    requete = """ SELECT SUM( Prix_revente - Prix_achat ) * SUM( Quantite ) FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement
                  WHERE ACHATS.Id_vetement = ? ;
                  """
    c.execute ( requete, ( Id_vetement, ) )
    benefice = c.fetchone () 
    
    # Affiche le bénéfice total pour ce vêtement. '.2f' sert à arrondir à 2 chiffres après la virgule.
    print ( f"Le bénéfice total pour {Nom_vetement} est de {benefice[0]:.2f} €." )
    return benefice

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#benefice_un_vetement ( curseur, "Robe" )

def benefice_total ( c ) :
    ''' Récupère le nom des vêtement. Puis on calcule le bénéfice par vêtement puis le bénéfice sur la totalité des ventes.
        Ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            
        POST : Affiche le bénéfice sur la totalité des ventes ou informe d'une erreur dans la console.
    '''

    # Récupère le bénéfice de tous les vêtemnts.
    requete = """ SELECT SUM( ( Prix_revente - Prix_achat ) * Quantite ) FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement ;
                  """
    c.execute ( requete )
    total = c.fetchone ()

    # Affiche le bénéfice total des ventes dans la console.
    print ( f"Le bénéfice total des ventes est de {total[0]:.2f} €." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#benefice_total ( curseur ) 


def gain_un_vetement ( c, Nom_vetement ) :
    ''' Récupère les informations sur le vêtement. Puis on calcule la quantité vendu du vêtement et son gain sur la totalité de ses ventes.
        Ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            Nom_vetement : le nom du vêtement
            
        POST : Affiche le gain sur la totalité des ventes de ce vêtements ou informe d'une erreur dans la console.
    '''

    # Récupère l'id du vêtement.
    requete = """ SELECT Id_vetement FROM VETEMENTS
                  WHERE Nom = ? ;
                  """
    c.execute ( requete, ( Nom_vetement, ) )
    vetement = c.fetchone ()
    
    # Si le vêtements n'existe pas, on informe dans la console.
    if not vetement :
        print ( f"Aucun vêtement trouvé." )
        return
    
    # Sinon on enregistre dans 2 variables differentes le contenu de la variable vêtement.
    Id_vetement = vetement[0]
    
    # Calcule le gain vendu de ce vêtement.
    requete = """ SELECT Prix_revente  * SUM( Quantite ) FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement
                  WHERE ACHATS.Id_vetement = ? ;
                  """
    c.execute ( requete, ( Id_vetement, ) )
    gain = c.fetchone () 
    
    # Affiche le gain total pour ce vêtement. '.2f' sert à arrondir à 2 chiffres après la virgule.
    print ( f"Le gain total pour {Nom_vetement} est de {gain[0]:.2f} €." )
    return gain

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#gain_un_vetement ( curseur, "Robe" )


def gain_total ( c ) :
    ''' Récupère le nom des vêtement. Puis on calcule le gain par vêtement puis le gain sur la totalité des ventes.
        Ou informe d'une erreur dans la console.
        PRE :
            c : le curseur
            
        POST : Affiche le gain sur la totalité des ventes ou informe d'une erreur dans la console.
    '''

    # Récupère le gain de tous les vêtemnts.
    requete = """ SELECT SUM( Prix_revente * Quantite ) FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement ;
                  """
    c.execute ( requete )
    total = c.fetchone ()
        
    # Affiche le bénéfice total des ventes dans la console.
    print ( f"Le gain total des ventes est de {total[0]:.2f} €." )

## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#gain_total ( curseur )



### TRAITEMENT STATISTIQUES
    
def meilleure_vente ( c ) :
    ''' Récupère le nom et la quantité du vêtement le plus vendu. Ou informe d'un problème dans la console.
        PRE :
            c : le curseur
        
        POST : Affiche le meilleur vêtement ou informe d'une erreur dans la console..
    '''
    
    # Récupère le nom et la quantité des vêtements vendu en les groupant par vêtement et rangé par ordre décroissant.
    # "AS" permet de donner un surnom à SUM ( Quantite ) et évite de devoir le remarquer.
    # "GROUP BY" permet de grouper les sommes d'un vêtment ensemble et donc de les additionner entre elles.
    # LIMIT 1 permet de récupérer seulement le premier élément.
    requete = """ SELECT Nom, SUM ( Quantite ) AS total_vendu FROM ACHATS
                  JOIN VETEMENTS ON ACHATS.Id_vetement = VETEMENTS.Id_vetement
                  GROUP BY VETEMENTS.Nom
                  ORDER BY total_vendu DESC
                  LIMIT 1 ;
                  """
    c.execute ( requete )
    resultat = c.fetchone ()
    
    # Si il n'y a pas de vente, on informe qu'il n'y a pas de meilleure vente dans la console.
    if not resultat :
        print ( "Il n'y a pas de meilleure vente." )
        return
    
    # Sinon on affiche la meilleure vente dans la console.
    print ( f"Le vêtmenent le plus de vente est {resultat[0]} avec {resultat[1]} ventes." )
 
## Test :
    # Plusieurs tests ont étaient réalisés grâce à cette ligne en la modifiant à chaque fois afin de l'adapter à la base de données.
#meilleure_vente ( curseur )
    
    
    
######## INTERFACE PYTHON ########

# Affiche la première page de l'interface.
def afficher_menu():
    print("\n∘•··•∘ʚ Menu Principal ɞ∘•··•∘")
    print("╔════════════════════════════╗")
    print("1. Acceder aux statistiques")
    print("2. Modifier la base de données")
    print("3. Quitter")
    print("╚════════════════════════════╝")
    

# Affiche et fait fonctionner la deuxième page pour le menu statistique.
def afficher_menuStatistiques():
    while True:
        print("\n∘•··•∘ʚ Menu Statistiques ɞ∘•··•∘")
        print("╔══════════════════════════════╗")
        print("1. Acceder aux gains totaux")
        print("2. Acceder aux gains par produit") 
        print("3. Acceder aux bénéfices totaux")
        print("4. Acceder aux bénéfices par produit")
        print("5. Afficher le meilleur article")
        print("6. Retour au menu principal")
        print("╚══════════════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            gain_total(curseur)
        elif choix == "2":
            nom = input("Entrez le nom du vêtement : ")
            gain_un_vetement(curseur, nom)
        elif choix == "3":
            benefice_total(curseur) 
        elif choix == "4":
            nom = input("Entrez le nom du vêtement : ")
            benefice_un_vetement(curseur, nom)
        elif choix == "5":
            meilleure_vente(curseur)
        elif choix == "6":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Affiche et fait fonctionner la deuxième page pour le menu de modification.
def afficher_menuPrincipal():
    while True:
        print("\n∘•·•∘ʚ Menu Modification ɞ∘•·•∘")
        print("╔════════════════════════════╗")
        print("1. Acceder au menu Vetement")
        print("2. Acceder au menu Client") 
        print("3. Acceder au menu Achat")
        print("4. Acceder au menu Taille")
        print("5. Acceder au menu Motif")
        print("6. Acceder au menu Couleur")
        print("7. Acceder au menu Fournisseur")
        print("8. Retour au menu principal")
        print("╚════════════════════════════╝")

        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            menu_vetement()
        elif choix == "2":
            menu_client()
        elif choix == "3":
            menu_achat()
        elif choix == "4":
            menu_taille()
        elif choix == "5":
            menu_motif()
        elif choix == "6":
            menu_couleur()
        elif choix == "7":
            menu_fournisseur()
        elif choix == "8":
            break
        else:
            print("Choix invalide, veuillez réessayer.")

# Affiche et fait fonctionner la deuxième page pour le menu vêtement.
def menu_vetement():
    while True:
        print("\n∘•·•∘ʚ Menu Vêtements ɞ∘•·•∘")
        print("╔═══════════════════════════╗")
        print("1. Ajouter un vêtement")
        print("2. Afficher les vêtements")
        print("3. Modifier un vêtement")
        print("4. Supprimer un vêtement")
        print("5. Retour")
        print("╚═══════════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            id_v = input("Id du vêtement : ")
            nom = input("Nom : ")
            taille = input("Taille : ")
            couleur = input("Couleur : ")
            motif = input("Motif : ")
            note = input("Note : ")
            prix_achat = float(input("Prix d'achat : "))
            prix_revente = float(input("Prix de revente : ")) 
            fournisseur = input("Fournisseur : ")
            nouveau_vetement(curseur, id_v, nom, taille, couleur, motif, note, prix_achat, prix_revente, fournisseur)
        elif choix == "2":
            afficher_vetements(curseur)
        elif choix == "3":
            nom = input("Nom du vêtement à modifier : ")
            taille = input("Nouvelle taille (laisser vide si inchangé) : ")
            couleur = input("Nouvelle couleur (laisser vide si inchangé) : ")
            motif = input("Nouveau motif (laisser vide si inchangé) : ")
            note = input("Nouvelle note (laisser vide si inchangé) : ")
            prix_achat = input("Nouveau prix d'achat (laisser vide si inchangé) : ")
            prix_revente = input("Nouveau prix de revente (laisser vide si inchangé) : ")
            fournisseur = input("Nouveau fournisseur (laisser vide si inchangé) : ")
            
            if prix_achat:
                prix_achat = float(prix_achat)
            else:
                prix_achat = None
                
            if prix_revente:
                prix_revente = float(prix_revente) 
            else:
                prix_revente = None
                
            if not taille:
                taille = None
            if not couleur:
                couleur = None
            if not motif:
                motif = None
            if not note:
                note = None
            if not fournisseur:
                fournisseur = None
                
            modifier_vetement(curseur, nom, taille, couleur, motif, fournisseur, prix_achat, prix_revente, note)
        elif choix == "4":
            nom = input("Nom du vêtement : ")
            taille = input("Taille : ")
            couleur = input("Couleur : ")
            motif = input("Motif : ")
            fournisseur = input("Fournisseur : ")
            supprimer_vetement(curseur, nom, taille, couleur, motif, fournisseur)
        elif choix == "5":
            break
        else:
            print("Choix invalide")

# Affiche et fait fonctionner la deuxième page pour le menu client.
def menu_client():
    while True:
        print("\n∘•·•∘ʚ Menu Client ɞ∘•·•∘")
        print("╔════════════════════╗")
        print("1. Ajouter un client")
        print("2. Afficher les clients")
        print("3. Modifier un client")
        print("4. Supprimer un client")
        print("5. Retour")
        print("╚════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            num = input("Numéro client : ")
            nom = input("Nom : ")
            prenom = input("Prénom : ")
            adresse = input("Adresse : ")
            ajouter_client(curseur, num, nom, prenom, adresse)
        elif choix == "2":
            afficher_clients(curseur)
        elif choix == "3":
            num = input("Numéro du client : ")
            nom = input("Nouveau nom (laisser vide si inchangé) : ")
            adresse = input("Nouvelle adresse (laisser vide si inchangé) : ")
            if not nom:
                nom = None
            if not adresse:
                adresse = None
            modifier_client(curseur, num, nom, adresse)
        elif choix == "4":
            num = input("Numéro du client : ")
            enlever_client(curseur, num)
        elif choix == "5":
            break
        else:
            print("Choix invalide")

# Affiche et fait fonctionner la deuxième page pour le menu achat.
def menu_achat():
    while True:
        print("\n∘•·•∘ʚ Menu Achat ɞ∘•·•∘")
        print("╔═════════════════════════╗")
        print("1. Nouvelle commande")
        print("2. Afficher les commandes")
        print("3. Retourner des articles")
        print("4. Calculer prix total commande")
        print("5. Retour")
        print("╚═════════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            id_achat = input("Id achat : ")
            nom_client = input("Nom client : ")
            prenom_client = input("Prénom client : ")
            adresse_client = input("Adresse client : ")
            vetement = input("Nom du vêtement : ")
            quantite = int(input("Quantité : "))
            date = input("Date (JJ/MM/AAAA) : ")
            num_commande = input("Numéro de commande : ")
            lieu = input("Lieu : ")
            nouvelle_commande(curseur, id_achat, nom_client, prenom_client, adresse_client, vetement, quantite, date, num_commande, lieu)
        elif choix == "2":
            afficher_commandes(curseur)
        elif choix == "3":
            nom_client = input("Nom client : ")
            prenom_client = input("Prénom client : ")
            adresse_client = input("Adresse client : ")
            vetement = input("Nom du vêtement : ")
            quantite = int(input("Quantité à retourner : "))
            lieu = input("Lieu : ")
            date = input("Date d'achat (JJ/MM/AAAA) : ")
            retour_articles(curseur, nom_client, prenom_client, adresse_client, vetement, quantite, lieu, date)
        elif choix == "4":
            date = input("Date d'achat (JJ/MM/AAAA) : ")
            nom_client = input("Nom client : ")
            prenom_client = input("Prénom client : ")
            adresse_client = input("Adresse client : ")
            calcule_prix_total_commande(curseur, date, nom_client, prenom_client, adresse_client)
        elif choix == "5":
            break
        else:
            print("Choix invalide")

# Affiche et fait fonctionner la deuxième page pour le menu taille.
def menu_taille():
    while True:
        print("\n∘•·•∘ʚ Menu Taille ɞ∘•·•∘")
        print("╔═══════════════════════╗")
        print("1. Ajouter une taille")
        print("2. Afficher les tailles")
        print("3. Supprimer une taille")
        print("4. Retour")
        print("╚═══════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            id_t = input("Id taille : ")
            taille = input("Taille : ")
            ajouter_taille(curseur, id_t, taille)
        elif choix == "2":
            afficher_taille(curseur)
        elif choix == "3":
            taille = input("Taille à supprimer : ")
            supprimer_taille(curseur, taille)
        elif choix == "4":
            break
        else:
            print("Choix invalide")

# Affiche et fait fonctionner la deuxième page pour le menu motif.
def menu_motif():
    while True:
        print("\n∘•·•∘ʚ Menu Motif ɞ∘•·•∘")
        print("╔═════════════════════════╗")
        print("1. Ajouter un motif")
        print("2. Afficher les motifs")
        print("3. Supprimer un motif")
        print("4. Retour")
        print("╚═════════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            id_m = input("Id motif : ")
            motif = input("Motif : ")
            ajouter_motif(curseur, id_m, motif)
        elif choix == "2":
            afficher_motif(curseur)
        elif choix == "3":
            motif = input("Motif à supprimer : ")
            supprimer_motif(curseur, motif)
        elif choix == "4":
            break
        else:
            print("Choix invalide")

# Affiche et fait fonctionner la deuxième page pour le menu couleur.
def menu_couleur():
    while True:
        print("\n∘•·•∘ʚ Menu Couleur ɞ∘•·•∘")
        print("╔═════════════════════════════╗")
        print("1. Ajouter une couleur")
        print("2. Afficher les couleurs")
        print("3. Supprimer une couleur")
        print("4. Retour")
        print("╚═════════════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            id_c = input("Id couleur : ")
            couleur = input("Couleur : ")
            ajouter_couleur(curseur, id_c, couleur)
        elif choix == "2":
            afficher_couleur(curseur)
        elif choix == "3":
            couleur = input("Couleur à supprimer : ")
            supprimer_couleur(curseur, couleur)
        elif choix == "4":
            break
        else:
            print("Choix invalide")

# Affiche et fait fonctionner la deuxième page pour le menu fournisseur.
def menu_fournisseur():
    while True:
        print("\n∘•·•∘ʚ Menu Fournisseurs ɞ∘•·•∘")
        print("╔════════════════════════════╗")
        print("1. Ajouter un fournisseur")
        print("2. Afficher les fournisseurs")
        print("3. Modifier un fournisseur")
        print("4. Retour")
        print("╚════════════════════════════╝")
        
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            id_f = input("Id fournisseur : ")
            nom = input("Nom : ")
            pays = input("Pays : ")
            ajouter_fournisseur(curseur, id_f, nom, pays)
        elif choix == "2":
            afficher_fournisseur(curseur)
        elif choix == "3":
            nom = input("Nom du fournisseur : ")
        elif choix == "4":
            break
            

def main():
    while True:
        afficher_menu()
        choix = input("Entrez votre choix : ")
        
        if choix == "1":
            afficher_menuStatistiques()
        elif choix == "2": 
            afficher_menuPrincipal()
        elif choix == "3":
            print("Au revoir!")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()
    
# Ferme la base de données
bdd.close ()

###### ESSAIE TKINTER #######


# # Fonction pour valider les champs numériques
# def est_numero(valeur):
#     try:
#         float(valeur)
#         return True
#     except ValueError:
#         return False
# 
# # Fonction pour ajouter un vêtement
# def ajouter_vetement_tkinter():
#     nom = entry_nom_vetement.get()
#     taille = entry_taille.get()
#     couleur = entry_couleur.get()
#     motif = entry_motif.get()
#     prix_achat = entry_prix_achat.get()
#     prix_revente = entry_prix_revente.get()
# 
#     if not all([nom, taille, couleur, motif, prix_achat, prix_revente]):
#         messagebox.showerror("Erreur", "Tous les champs sont requis.")
#         return
# 
#     if not (est_numero(prix_achat) and est_numero(prix_revente)):
#         messagebox.showerror("Erreur", "Les prix doivent être des nombres valides.")
#         return
# 
#     try:
#         gv.nouveau_vetement(curseur, None, nom, taille, couleur, motif, None, prix_achat, prix_revente, 'Dior')
#         bdd.commit()
#         messagebox.showinfo("Succès", "Vêtement ajouté avec succès.")
#     except sqlite3.Error as e:
#         messagebox.showerror("Erreur", str(e))
# 
# # Fonction pour ajouter un client
# def ajouter_client_tkinter():
#     num_client = entry_num_client.get()
#     nom = entry_nom_client.get()
#     prenom = entry_prenom.get()
#     adresse = entry_adresse.get()
# 
#     if not all([num_client, nom, prenom, adresse]):
#         messagebox.showerror("Erreur", "Tous les champs sont requis.")
#         return
# 
#     try:
#         gcl.ajouter_client(curseur, num_client, nom, prenom, adresse)
#         bdd.commit()
#         messagebox.showinfo("Succès", "Client ajouté avec succès.")
#     except sqlite3.Error as e:
#         messagebox.showerror("Erreur", str(e))
# 
# # Fenêtre principale
# root = tk.Tk()
# root.title("Gestion des vêtements et des clients")
# root.geometry("800x600")
# 
# # Création du menu
# menu = tk.Menu(root)
# root.config(menu=menu)
# 
# gestion_menu = tk.Menu(menu, tearoff=0)
# menu.add_cascade(label="Gestion", menu=gestion_menu)
# 
# # Onglets/notebook
# notebook = ttk.Notebook(root)
# notebook.pack(pady=10, expand=True)
# 
# # Onglet Vêtements
# frame_vetements = ttk.Frame(notebook)
# notebook.add(frame_vetements, text="Vêtements")
# 
# ttk.Label(frame_vetements, text="Nom:").grid(row=0, column=0, padx=10, pady=10)
# entry_nom_vetement = ttk.Entry(frame_vetements)
# entry_nom_vetement.grid(row=0, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_vetements, text="Taille:").grid(row=1, column=0, padx=10, pady=10)
# entry_taille = ttk.Entry(frame_vetements)
# entry_taille.grid(row=1, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_vetements, text="Couleur:").grid(row=2, column=0, padx=10, pady=10)
# entry_couleur = ttk.Entry(frame_vetements)
# entry_couleur.grid(row=2, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_vetements, text="Motif:").grid(row=3, column=0, padx=10, pady=10)
# entry_motif = ttk.Entry(frame_vetements)
# entry_motif.grid(row=3, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_vetements, text="Prix Achat:").grid(row=4, column=0, padx=10, pady=10)
# entry_prix_achat = ttk.Entry(frame_vetements)
# entry_prix_achat.grid(row=4, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_vetements, text="Prix Revente:").grid(row=5, column=0, padx=10, pady=10)
# entry_prix_revente = ttk.Entry(frame_vetements)
# entry_prix_revente.grid(row=5, column=1, padx=10, pady=10)
# 
# btn_ajouter_vetement = ttk.Button(frame_vetements, text="Ajouter Vêtement", command=ajouter_vetement_tkinter)
# btn_ajouter_vetement.grid(row=6, column=0, columnspan=2, pady=20)
# 
# # Onglet Clients
# frame_clients = ttk.Frame(notebook)
# notebook.add(frame_clients, text="Clients")
# 
# ttk.Label(frame_clients, text="Numéro Client:").grid(row=0, column=0, padx=10, pady=10)
# entry_num_client = ttk.Entry(frame_clients)
# entry_num_client.grid(row=0, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_clients, text="Nom:").grid(row=1, column=0, padx=10, pady=10)
# entry_nom_client = ttk.Entry(frame_clients)
# entry_nom_client.grid(row=1, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_clients, text="Prénom:").grid(row=2, column=0, padx=10, pady=10)
# entry_prenom = ttk.Entry(frame_clients)
# entry_prenom.grid(row=2, column=1, padx=10, pady=10)
# 
# ttk.Label(frame_clients, text="Adresse:").grid(row=3, column=0, padx=10, pady=10)
# entry_adresse = ttk.Entry(frame_clients)
# entry_adresse.grid(row=3, column=1, padx=10, pady=10)
# 
# btn_ajouter_client = ttk.Button(frame_clients, text="Ajouter Client", command=ajouter_client_tkinter)
# btn_ajouter_client.grid(row=4, column=0, columnspan=2, pady=20)

# Boucle principale
#root.mainloop()