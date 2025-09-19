from flask import Flask

from controllers.routes import main as main_blueprint


def create_app() -> Flask:
	app = Flask(__name__, template_folder='views', static_folder='static')
	app.register_blueprint(main_blueprint)
	return app


app = create_app()


if __name__ == '__main__':
	app.run(host='0.0.0.0', port='4000', debug=True)


