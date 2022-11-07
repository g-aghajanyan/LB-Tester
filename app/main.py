from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import socket
from os import getenv

hostName = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes(f"""
<html>
   <head>
      <title>LB-Tester</title>
   </head>
   <style>
   table, th, td {{
       border:1px solid black; border-collapse: collapse;
    }}
   </style>
   <body>
      <table style="width:360px">
         <tr>
            <th>Proto</th>
            <th>Req_Ver</th>
            <th>Req_Type</th>
         </tr>
         <tr>
            <td>{self.protocol_version}</td>
            <td>{self.request_version}</td>
            <td>{self.command}</td>
         </tr>
      </table>
      <p>
        <p><b>HostName:</b>&emsp;&emsp;&emsp;&ensp;{socket.gethostname()}<br>
        <b>Client Address:</b>&emsp;&ensp;&nbsp;{self.client_address}<br>
        <b>APP_VERSION:</b>&emsp;{getenv('APP_VERSION', "unspecified")}
      </p>
      <b>Request Path:</b> /path4?param1=val1</p>
      <p>
        <b>HEADERS:</b><br>
        <pre>{self.headers}</pre>
      </p>
   </body>
</html>
""", "utf-8"))

if __name__ == "__main__":        
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.") 