from flask import Flask, request

app = Flask(__name__)


@app.route('/flask-app/', methods=['GET'])
def routing_function():
    """
    Routing function a human formatted response of all data in the db.
    Only allowed methods are GET and POST with the payload JSON or DICT
    Other service such as PATCH, PUT and DELETE are not allowed method and hence will return 405 response
    method not allowed for the service.
    :return:
    """
    print("Flask App")


if __name__ == '__main__':
    """
    Running flask application route
    """
    app.run()
