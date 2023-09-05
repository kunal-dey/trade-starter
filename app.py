from quart import Quart, Blueprint
from quart_cors import cors

from routes.login import login

app = Quart(__name__)
app.config["PROPAGATE_EXCEPTIONS"] = True
app = cors(app, allow_origin="*")

resource_list:Blueprint=[login]

for resource in resource_list:
    app.register_blueprint(blueprint=resource)

if __name__ == "__main__":
    app.run(port=8080)
