import smtplib

server=smtplib.SMTP_SSL("smtp.gmail.com",465)

server.login("aashutoshkumar.mishra98@gmail.com","Aa$hu173001")

server.sendmail("aashutoshkumar.mishra98@gmail.com","aashutoshkumar.mishra98@gmail.com","hello how are u")

server.quit()