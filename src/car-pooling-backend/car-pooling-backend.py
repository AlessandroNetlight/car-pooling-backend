from celery import Celery


class FlaskCelery(Celery):
    """
    Flask aware Celery class. Calls tasks with a new app context for each task call.
    """

    def __init__(self, *args, **kwargs):
        super(FlaskCelery, self).__init__(*args, **kwargs)
        self.patch_task()

        if 'app' in kwargs:
            self.init_app(kwargs['app'])

    def patch_task(self):
        TaskBase = self.Task
        _celery = self

        class ContextTask(TaskBase):
            abstract = True

            def __call__(self, *args, **kwargs):
                with _celery.app.app_context():
                    return TaskBase.__call__(self, *args, **kwargs)

        self.Task = ContextTask

    def configure(self):
        self.conf.task_default_queue = self.app.config['SERVICE_NAME']

    def init_app(self, app):
        self.app = app
        self.conf.broker_url = app.config['BROKER_URI']
        self.configure()
