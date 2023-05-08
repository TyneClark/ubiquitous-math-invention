from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import sqlite3
from db import *
from compute import *
import json

class MyRequestHandler(BaseHTTPRequestHandler):

    def handleNotFound(self):
        self.send_response(404)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("Not found.", "utf-8"))

    def handleGetDB(self):
        #print("headers at GET:", self.headers)
        db = numDB()
        nums = db.getDB()

        if nums != None:
            # response status code
            self.send_response(200)
            # response header
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            # response body
            self.wfile.write(bytes(json.dumps(nums), "utf-8")) #jsonify
        else:
            self.handleNotFound()

    def do_GET(self):
        path_parts = self.path.split("/")
        if len(path_parts) == 3:
            collection_name = path_parts[1]
            member_id = path_parts[2]
        else:
            collection_name = path_parts[1]
            member_id = None

        count = 0
        if collection_name == "db":
            count = 1
            if member_id:
                self.handleNotFound
            else:
                self.handleGetDB()
        if count == 0:
            self.handleNotFound()

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    pass

def run():
    db = numDB()
    db.createTable()
    db = None # disconnect from database

    port = 8080
    if "PORT" in os.environ:
        port = int(os.environ["PORT"])
    listen = ("0.0.0.0", port)
    server = ThreadedHTTPServer(listen, MyRequestHandler)
    print("Server Running!")
    server.serve_forever()

if __name__ == '__main__':
    run()
    startTestingNumbers()