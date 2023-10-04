from fabric import Connection, task

@task
def deploy_web_static(c):
    # Path to the 0-setup_web_static.sh script on your local machine
    local_script_path = './0-setup_web_static.sh'

    # Path to the 0-setup_web_static.sh script on the remote server
    remote_script_path = '/tmp/0-setup_web_static.sh'

    # Upload the deployment script to the remote server
    c.put(local_script_path, remote=remote_script_path)

    # Make the script executable on the remote server
    c.sudo(f'chmod +x {remote_script_path}')

    # Run the deployment script on the remote server
    c.sudo(remote_script_path)
