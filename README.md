# mastertoEC2
🔧 Goal:
   Deploy an application (e.g., a Python web app or any codebase) to a remote EC2 instance using a script.

💡 Prerequisites:

: AWS CLI configured (aws configure)<br /> 
: SSH key for EC2 access<br /> 
: EC2 instance with access (IP + username)<br /> 
: Your app files ready in a directory<br /> 
: Python or Bash environment to run the script <br /> 

📦 What the script will do:

: Package the app files (optional zip/tar)<br /> 
: Copy the app to the EC2 instance using scp<br /> 
: SSH into the EC2 and run deployment commands:<br /> 
: Unpack<br /> 
: Install dependencies<br /> 
: Start the app (e.g., via systemctl, nohup, or Docker)<br /> 

Note:

1. Install required libs: pip install paramiko scp

2. Ensure your security group allows SSH (port 22)


