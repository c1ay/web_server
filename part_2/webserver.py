#coding:utf-8
import socket
import sys

class WSGIServer(object):
    '''
        wsgi 提供wsgi层接口
    '''
    address_family = socket.AF_INET
    socket_type = socket.SOCK_STREAM
    request_queue_size = 1

    def __init__(self, server_address):
        self.listen_socket = listen_socket = socket.socket(
                self.address_family,
                self.socket_type
                )
        listen_socket.setsockopt(socket.SOL_SOCKET, sockdet.SO_REUSEADDR, 1)
        listen_socket.bind(server_address)
        listen_socket.listen(self.request_queue_size)
        host, port = self.listen_socket.getsockname()[:2]
        self.server_name = socket.getfqdn(host)
        self.server_port = port
        self.headers_set = []

    def set_app(self, application):
        self.application = application

    def serve_forever(self):
        listen_socket = self.listen_socket
        while True:
            self.client_connection, client_address = listen_socket.accept()
            self.handle_one_request()

    def handle_one_request(self):
        self.request_data = request_data = self.client_connection.recv(1024)
        print ''.join(
                '<{line}\n'.format(line=line)
                for line in request_data.splitlines()
                )

        self.parse_request(request_data)
        env = self.get_environ()
        result = self.application(env, self.start_response)
        self.finish_response(result)

    def parse_request(self, text):
        pass

    def get_environ(self):
        pass

    def start_response(self):
        pass

    def finish_response(self):
        pass
               
