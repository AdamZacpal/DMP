# -*- coding: utf-8 -*-
"""
Created on Sun Dec  9 19:50:01 2018

@author: Adam
"""
import smtplib
def napismi():
    import smtplib
    content="Ahoj jak se máš"
    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()
    mail.starttls()
    mail.login("zacpalweb@gmail.com","kavanata123") 
    mail.sendmail("zacpalweb@gmail.com","adamzacpal@seznam.cz",content)
    mail.close()  

