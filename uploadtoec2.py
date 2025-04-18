import paramiko
from scp import SCPClient
import os

# Configs
EC2_IP = 'your-ec2-ip'
EC2_USER = 'ec2-user'  # or ubuntu
KEY_PATH = '/path/to/your/key.pem'
LOCAL_APP_DIR = './myapp'
REMOTE_APP_DIR = '/home/ec2-user/myapp'

# Create SSH client
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(EC2_IP, username=EC2_USER, key_filename=KEY_PATH)

# Create SCP client
scp = SCPClient(ssh.get_transport())

# Upload files
print("Uploading files...")
scp.put(LOCAL_APP_DIR, recursive=True, remote_path=REMOTE_APP_DIR)

# Run deployment commands
print("Running remote setup...")
commands = [
    f'cd {REMOTE_APP_DIR}',
    'pip install -r requirements.txt',  # adjust as needed
    'nohup python app.py &'  # or use systemctl or docker
]

for cmd in commands:
    stdin, stdout, stderr = ssh.exec_command(cmd)
    print(stdout.read().decode())
    print(stderr.read().decode())

# Cleanup
scp.close()
ssh.close()
print("Deployment complete!")
