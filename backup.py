#Constroi o arquivo e path de backup e retorna
from datetime import datetime, date

now = datetime.now()
print ( now.hour, ':', now.minute, '  ', now.day, '-', 
    now.month, '-', now.year )


class Backup:
    def gerabackup():
        date = (time.strftime("%Y-%m-%d"))

    #cria o nome do arquivo de backup
        backupfile = '%s-backup-full.tar.gz' % date

    #destino onde será gravado o backup
        pathdesdino = '/mnt/hdbackup/%s' % backupfile

    #pasta que será feita backup
        pathorigem = '/mnt/storage'

    #comando de execução
        backup = 'tar cvf %s %s' % (pathdesdino, pathorigem)

        return backup
