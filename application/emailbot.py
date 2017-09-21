# -*- coding:utf-8 -*-
# Importation des modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

globals()
Fromadd = "saintfourieronesyme@gmail.com"


def envoiemailaviso():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        # Spécification des destinataires en copie carbone (cas de plusieurs destinataires)
        bcc = ""
        # Spécification du destinataire en copie cachée (en copie cachée)

        #  Spécification des destinataires
        message = MIMEMultipart()
        # Création de l'objet "message"
        message['From'] = Fromadd
        # Spécification de l'expéditeur
        message['To'] = Toadd
        # Attache du destinataire à l'objet "message"

        message['CC'] = ",".join(cc)
        # Attache des destinataires en copie carbone à l'objet "message" (cas de plusieurs destinataires)
        message['BCC'] = bcc
        # Attache du destinataire en copie cachée à l'objet "message"

        message['Subject'] = "Aviso"
        # Spécification de l'objet de votre mail
        msg = " les bots Aviso "
        # Message à envoyer
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))
        # Attache du message à l'objet "message", et encodage en UTF-8

        # piece_jointe = ['tester.zip', 'teston.zip']
        nom_fichier = 'DOC_COMP/AVISO.zip'
        # Spécification du nom de la pièce jointe
        piece = open(nom_fichier, "rb")
        # Ouverture du fichier
        part = MIMEBase('application', 'octet-stream')
        # Encodage de la pièce jointe en Base64
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        message.attach(part)
        # Attache de la pièce jointe à l'objet "message"

        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        # Connexion au serveur sortant (en précisant son nom et son port)
        serveur.starttls()
        # Spécification de la sécurisation
        serveur.login(Fromadd, "saint02111366")
        # Authentification
        texte = message.as_string().encode('utf-8')
        # piece_jointes = message.as_string().encode('utf-8')
        # Conversion de l'objet "message" en chaine de caractère et encodage en UTF-8
        Toadds = [Toadd] + cc + [bcc]
        # Rassemblement des destinataires
        serveur.sendmail(Fromadd, Toadds, texte)
        # Envoi du mail
        serveur.quit()
        # Déconnexion du serveur

        print("\n \t\t\t[OK] MAIL AVISO ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)


def envoiemailafnet():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        bcc = ""

        message = MIMEMultipart()
        message['From'] = Fromadd
        message['To'] = Toadd

        message['CC'] = ",".join(cc)
        message['BCC'] = bcc

        message['Subject'] = "Afnet"
        msg = " les bots Afnet "
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

        nom_fichier = 'DOC_COMP/AFNET.zip'
        piece = open(nom_fichier, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        message.attach(part)

        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(Fromadd, "saint02111366")
        texte = message.as_string().encode('utf-8')
        Toadds = [Toadd] + cc + [bcc]
        serveur.sendmail(Fromadd, Toadds, texte)
        serveur.quit()

        print("\n \t\t\t[OK] MAIL AFNET ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)


def envoiemailmoov():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        bcc = ""

        message = MIMEMultipart()
        message['From'] = Fromadd
        message['To'] = Toadd

        message['CC'] = ",".join(cc)
        message['BCC'] = bcc

        message['Subject'] = "Moov"
        msg = "les bots Moov "
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

        nom_fichier = 'DOC_COMP/MOOV.zip'
        piece = open(nom_fichier, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        message.attach(part)

        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(Fromadd, "saint02111366")
        texte = message.as_string().encode('utf-8')
        Toadds = [Toadd] + cc + [bcc]
        serveur.sendmail(Fromadd, Toadds, texte)
        serveur.quit()

        print("\n \t\t\t[OK] MAIL MOOV ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)


def envoiemailvipnet():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        bcc = ""

        message = MIMEMultipart()
        message['From'] = Fromadd
        message['To'] = Toadd

        message['CC'] = ",".join(cc)
        message['BCC'] = bcc

        message['Subject'] = "Vipnet"
        msg = "les bots Vipnet "
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

        nom_fichier = 'DOC_COMP/VIPNET.zip'
        piece = open(nom_fichier, "rb")
        # Ouverture du fichier
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        message.attach(part)

        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(Fromadd, "saint02111366")
        texte = message.as_string().encode('utf-8')
        Toadds = [Toadd] + cc + [bcc]
        serveur.sendmail(Fromadd, Toadds, texte)
        serveur.quit()

        print("\n \t\t\t[OK] MAIL VIPNET ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)


def envoiemailnsia():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        bcc = ""

        message = MIMEMultipart()
        message['From'] = Fromadd
        message['To'] = Toadd

        message['CC'] = ",".join(cc)
        message['BCC'] = bcc

        message['Subject'] = "Nsia"
        msg = "les bots NSIA "
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

        nom_fichier = 'DOC_COMP/NSIA.zip'
        piece = open(nom_fichier, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        message.attach(part)

        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(Fromadd, "saint02111366")
        texte = message.as_string().encode('utf-8')
        Toadds = [Toadd] + cc + [bcc]
        serveur.sendmail(Fromadd, Toadds, texte)
        serveur.quit()

        print("\n \t\t\t[OK] MAIL NSIA ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)


def envoiemailyoomee():

    try:

        Toadd = "warrensaint1@gmail.com"

        cc = []
        bcc = ""

        message = MIMEMultipart()
        message['From'] = Fromadd
        message['To'] = Toadd

        message['CC'] = ",".join(cc)
        message['BCC'] = bcc

        message['Subject'] = "Yoomee"
        msg = "les bots Yoomee "
        message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))

        nom_fichier = 'DOC_COMP/YOOMEE.zip'
        piece = open(nom_fichier, "rb")
        part = MIMEBase('application', 'octet-stream')
        part.set_payload((piece).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', "piece; filename= %s" % nom_fichier)
        message.attach(part)

        serveur = smtplib.SMTP('smtp.gmail.com', 587)
        serveur.starttls()
        serveur.login(Fromadd, "saint02111366")
        texte = message.as_string().encode('utf-8')
        Toadds = [Toadd] + cc + [bcc]
        serveur.sendmail(Fromadd, Toadds, texte)
        serveur.quit()

        print("\n \t\t\t[OK] MAIL YOOMEE ENVOYER !")

    except smtplib.SMTPAuthenticationError as e:

            print(" Erreur d'envoie de mail Authentification requis ! %s \n" % e)