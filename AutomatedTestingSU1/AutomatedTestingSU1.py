import paramiko, scp, os, shutil, time, re
hostname = '172.20.133.12'
username = 'gencom'
password = 'y8gf839i'
port = 22
cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
cliente.connect(hostname=hostname, 
                username=username, 
                password=password, 
                auth_timeout=25,
                port=port)
session = cliente.invoke_shell()
session.settimeout(timeout=20)

scp_cliente = scp.SCPClient (cliente.get_transport() )

archivio = input('Nome archivio: ')
ruta = os.path.join(r"C:\Users\gabriel.melero\source\repos\GetDataCisco\GetDataCisco",archivio) 
#You should change this if you want to use it in your local computer
ruta2 = os.path.join(r"C:\Users\gabriel.melero\source\repos\AutomatedTestingSU1\AutomatedTestingSU1", archivio )
#And this root to jejejej, because its for my WiNdOwS CoMpUtEr as you can see
ruta3 = os.path.join(r"/home/gencom/GetDataCisco/GetDataCisco")

shutil.copyfile( ruta, ruta2 )
scp_cliente.put(ruta2, remote_path=ruta3 )

scp_cliente.close()
#Abro una nueva conexion
cliente = paramiko.SSHClient()
cliente.set_missing_host_key_policy( paramiko.AutoAddPolicy() )
cliente.connect(hostname=hostname, 
                username=username, 
                password=password, 
                auth_timeout=25,
                port=port)
session = cliente.invoke_shell()
session.settimeout(timeout=20)
session.send('ll | grep source\n ')
time.sleep(.5)
print( session.recv(65000).decode() )
sourceFile = input('Which source file you want?: ')
session.send('set -a ; source /home/gencom/'+sourceFile+' ; set +a\n')
time.sleep(.5)
print( session.recv(65000).decode('cp850') )
session.send('env | grep IFX\n')
time.sleep(.5)
print( session.recv(65000).decode() )

session.send('cd /home/gencom/GetDataCisco/GetDataCisco\n')
time.sleep(.5)
session.recv(65000).decode()

session.send('python3 '+ archivio +'\n')
time.sleep(.5)
print( session.recv(65000).decode("cp850"))

time.sleep(.5)
num= 1
while not session.recv_ready():
    try:
        print( session.recv(65000).decode("cp850"))
    except:
        print("\n")

    time.sleep(.5)
    num+=1
    if num==10:
        break

