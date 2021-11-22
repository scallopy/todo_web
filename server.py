import os
from http.server import HTTPServer, CGIHTTPRequestHandler


web_dir = os.path.join(os.path.dirname(__file__), 'templates')
os.chdir(web_dir)


hostName = "127.0.0.1"
PORT = 8080


if __name__ == "__main__":
    webServer = HTTPServer(
        server_address=('', PORT), RequestHandlerClass=CGIHTTPRequestHandler
    )
    print("Server started http://%s:%s" % (hostName, PORT))

    try:
        webServer.serve_forever()

    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server Stopped")
