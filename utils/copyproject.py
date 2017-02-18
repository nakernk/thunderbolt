# AUTHOR: Fernando Gonzalez
# DESCRIPTION: Script para la subida de archivos o directorios por ssh 
# 			   a un server remoto.
#
#			-COPIA EL DIRECTORIO
#
# PRE: Para usar este Script hay que instalar sshpass en el sistema
#		Windows: No se buscaos la vida
#		Linux: sudo apt-get install sshpass
#		Mac: sudo port install sshpass   <- Requiere tener instalado Mac ports (Buscad en internet como instalar ese gestor de paquetes)
#
# COPIA UN DIRECTORIO COMPLETO AL SERVIDOR
# scp -r /home/<USUARIO>/carpeta usuario@dominio.com:/home/<USUARIO>
# 
# COPIA UN ARCHIVO AL SERVIDOR
# scp /home/<USUARIO>/archivo.txt usuario@dominio.com:/home/<USUARIO>
#

import os

####################################################################
# CONFIGURACION DEL SCRIPT
#
# Configuracion SSH
server =  '192.168.1.100'		#Servidor raspberry
usuario = 'pi'					#Usuario ssh
clave =   'raspbian'			#Clave ssh

#Ruta del directorio origen (local)
local = '/Users/fernandogonzalez/Developer/Python/thunderbolt'

#Ruta del directorio destino (remoto)
remoto = './python/' #ruta relativa al directorio /home/usuario (~/)
#####################################################################

# Inicio del programa
print "\n\n -== Script TRANSFERENCIA DE DIRECTORIO ==- \n\n"

#Funcion que ejecuta un comando y devuelve el resultado de la ejecucion
def run_command(command, message):
    results = os.system(command)

    if results == 0:
        return message
    else:
        return str(results) + "\n"

#Copia el directorio del tema y sus archivos (Solo los cambios)
command = 'sshpass -p \''+clave+'\' scp -r '+local+' '+usuario+'@'+server+':'+remoto
print "Copiando Directorio...\n"
print run_command(command, '')

print "-- Proceso finalizado-- :)\n\n"

