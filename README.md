# mastertoEC2
🔧 Goal:
   Deploy an application (e.g., a Python web app or any codebase) to a remote EC2 instance using a script.

💡 Prerequisites:
   AWS CLI configured (aws configure)
   SSH key for EC2 access
   EC2 instance with access (IP + username)
   Your app files ready in a directory
   Python or Bash environment to run the script

📦 What the script will do:
   Package the app files (optional zip/tar)
   Copy the app to the EC2 instance using scp
   SSH into the EC2 and run deployment commands:
   Unpack
   Install dependencies
   Start the app (e.g., via systemctl, nohup, or Docker)
