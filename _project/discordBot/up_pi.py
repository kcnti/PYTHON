import os, sys
os.system(f"scp {sys.argv[1]} pi@192.168.1.46:/home/pi/backup_server")