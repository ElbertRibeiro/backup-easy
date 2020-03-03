#Constroi o arquivo e path de backup e retorna
from datetime import datetime, date

class Datahora:
    date = datetime.now()
    print ( date.hour, ':', date.minute, '  ', date.day, '-', 
        date.month, '-', date.year )

@staticmethod
class Backup:
    def gerabackup():
#        date = (time.strftime("%Y-%m-%d"))

    #cria o nome do arquivo de backup
        backupfile = '%s-backup-full.tar.gz' % date

    #destino onde será gravado o backup
        pathdesdino = '/mnt/hdbackup/%s' % backupfile

    #pasta que será feita backup
        pathorigem = '/mnt/storage'

    #comando de execução
        backup = 'tar cvf %s %s' % (pathdesdino, pathorigem)

        print ( backup )
