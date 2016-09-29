import os
import config
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from server import app, db


# Custom or Default Config
if 'APP_SETTINGS' in os.environ:
    app.config.from_object(os.environ['APP_SETTINGS'])
else:
    app.config.from_object(config.Config)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
