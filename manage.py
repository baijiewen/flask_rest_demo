import os
from flask_script import Manager, Shell
from flask_migrate import Migrate, MigrateCommand
from celery import Celery
from app import create_app, db
from app.models import User


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)

celery = Celery(app.name, broker=app.config['CELERY_BROKER_URL'])
celery.conf.update(app.config)


@app.shell_context_processor
def make_shell_context():
    return dict(db=db,User=User)


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
