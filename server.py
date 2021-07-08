import sys

from gevent.pywsgi import WSGIServer

from routes import api

if __name__ == "__main__":
    if "debug" in sys.argv:
        api.run(host="0.0.0.0", port=5002, debug=True, threaded=True)
    else:
        http_server = WSGIServer(("0.0.0.0", 5002), api)
        http_server.serve_forever()
