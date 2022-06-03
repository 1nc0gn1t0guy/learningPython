class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()


# dos procesos
# amis, desde la zona de holanda han solicitado tener un sharepoint con fotos
# el proceso debe lanzarse, lanzar un powershell con o365 y asignara a cada usuario una foto en concreto
# 
#  cada x tiemop se lanza un script de caducidad de password, analiza quien esta caducado en ad y lo caduca en o365
# fgpp
# sacamos un listado de todos los users caducados
# automaticamente lanzamos el siguiente comando de powershell a o365 pidiendo que se bloquee el usuario en el ad y que cambie el password la siguiente vez que se conecte