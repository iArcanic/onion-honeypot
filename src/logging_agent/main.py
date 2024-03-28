import paramiko


class MySSHServer(paramiko.ServerInterface):
    def check_auth_password(self, username, password):
        return paramiko.AUTH_SUCCESSFUL


host_key = paramiko.RSAKey.generate(2048)
server = '0.0.0.0'
port = 2222

ssh_server = paramiko.Transport((server, port))
ssh_server.add_server_key(host_key)
ssh_server.start_server(server=server)

while True:
    client, addr = ssh_server.accept()
    client_handler = paramiko.Channel(client)
    client_handler.invoke_shell()
