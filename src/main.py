#!/usr/bin/env python3

# pi2open
# a pishock to openshock api translation layer
#
# this was written at 5:30am
# do not expect it to hold up well!
#
# author: k01e <k01e.alm07@gmail.com>
# license: MIT
# deps: flask, request, ./openshock.py


from flask import Flask, request
from openshock import ControlType, openshock_api
import os


PORT = 8000
OPENSHOCK_URL = "https://api.openshock.app/"
OPENSHOCK_TOKEN = None
OPENSHOCK_SHOCKER = None


def token_err():
    print(
        "please provide a token, either through the envvar OPENSHOCK_TOKEN or via the variable"
    )
    exit(1)


def shocker_err():
    print(
        "please provide a shocker id, either through the envvar OPENSHOCK_SHOCKER or via the variable"
    )
    exit(1)


app = Flask(__name__)
api = openshock_api(
    api_key=OPENSHOCK_TOKEN or os.environ.get("OPENSHOCK_TOKEN") or token_err(),
    url=OPENSHOCK_URL,
)
shk = api.create_shocker(
    shocker_id=OPENSHOCK_SHOCKER or os.environ.get("OPENSHOCK_SHOCKER") or shocker_err(),
)

op_to_type = {
    "0": ControlType.SHOCK,
    "1": ControlType.VIBRATE,
    "2": ControlType.SOUND,
}


@app.route("/api/apioperate", methods=["POST"])
async def handle_pishock_request():
    data = request.get_json()
    if data is None:
        print("No json from client!")
        return "Invalid request.", 400

    print(f"Recieved from client: {data}")

    res = await shk.control(
        type=op_to_type[data["Op"]],
        intensity=int(data["Intensity"]),
        duration=int(data["Duration"]) * 1000,
        author=data["Name"],
    )
    print(f"Recieved from server: {res.text}")

    return "Operation Succeeded.", 200  # well... probably!


if __name__ == "__main__":
    app.run(host="localhost", port=PORT, debug=True, ssl_context=("cert.pem", "key.pem"))
