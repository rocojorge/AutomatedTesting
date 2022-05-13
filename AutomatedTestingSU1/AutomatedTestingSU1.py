import paramiko, scp, os, shutil, time, GetDataCisco

hostname = 'ip'
username = 'user'
password = 'pass'
port = 22
out_number = 1
variable = "y"

try:
    while variable != "n":
        scp_session,error = GetDataCisco.ConnectToSCP(hostname,username,password,port)
        archivio = input('Nome archivio: ')
        if archivio == 'n':break
        archivio+='.py'
        ruta = os.path.join(r"C:\Users\gabriel.melero\source\repos\GetDataCisco\GetDataCisco",archivio) 
        #You should change this if you want to use it in your local computer
        ruta2 = os.path.join(r"C:\Users\gabriel.melero\source\repos\AutomatedTestingSU1\AutomatedTestingSU1\PROVAS", archivio )
        #And this root to jejejej, because its for my WiNdOwS CoMpUtEr as you can see
        ruta3 = os.path.join(r"/home/gencom/GetDataCisco/GetDataCisco")

        shutil.copyfile( ruta, ruta2 )
        print(ruta)
        print("Copied...")

        scp_session.put( ruta2,ruta3 )
        print('Send it to...')
        print(ruta3)
        scp_session.close()

        ssh_session, error = GetDataCisco.ConnectToSSH(hostname,username,password,port)
        USER,HOSTNAME = GetDataCisco.TakeUserHostName( ssh_session )

        command = 'cd '+ruta3+'\n'
        lista, error = GetDataCisco.RunCommand( ssh_session ,out_number, HOSTNAME, USER, command=command )
        for line in lista:
            print(line)
        print('\n')
        command = input('Number of the source file: ')
        if command == 'n':break
        command = r'set -a ; source /home/gencom/source'+str(command)+'.sh ; set +a'

        lista, error = GetDataCisco.RunCommand( ssh_session ,out_number, HOSTNAME, USER, command=command )
        for line in lista:
            print(line)

        command = 'python3 '+ archivio + '\n'
        lista, error = GetDataCisco.RunCommand( ssh_session ,out_number, HOSTNAME, USER, command=command )
        for line in lista:
            print(line)
        print('\n')

        variable = input("Would you like to do it again?(N=Uscita, Other=Continua) : ")
except:
    print("Bad exit, you have done something bad there bro...")
    input()
print("Uscire correttamente")



