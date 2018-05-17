from setuptools import setup
import sys

setup(name='python_ikr_client',
      version='0.3',
      description='',
      url='https://github.com/andrii-dubytskyi/python_ikr_client.git',
      download_url = 'https://github.com/andrii-dubytskyi/python_ikr_client/archive/master.zip',
      author='Chi Tester',
      author_email='chi.tester@gmail.com',
      license='MIT',
      packages=['python_ikr_client'],
      install_requires=[
        'prompt_toolkit',
        #'pysha3==1.0b1',
        #'requests==2.13.0',
        #'sha3==0.2.1'
      ],
      dependency_links=[
        'https://github.com/jonathanslenders/python-prompt-toolkit/archive/2.0.zip#egg=prompt_toolkit'
      ],
      zip_safe=False)


def configure():
    from prompt_toolkit.formatted_text import HTML
    from prompt_toolkit.application.current import get_app
    from prompt_toolkit.shortcuts.dialogs import message_dialog
    from prompt_toolkit.styles import Style
    from prompt_toolkit.layout.containers import VSplit
    from prompt_toolkit.widgets import Label, TextArea
    from prompt_toolkit.shortcuts.dialogs import yes_no_dialog, button_dialog, progress_dialog
    from prompt_toolkit.layout.dimension import Dimension as D
    from prompt_toolkit.widgets import MenuContainer, MenuItem
    import time
    from python_ikr_client.custom_prompts import form
    from python_ikr_client import ikr_client as ikr

    config = {
        'server_url': ikr.config['server_url']
    }
    def login(form_data, app):

        result = {'token': 'asdasd'} #ikr.refresh_token(form_data['User ID'], form_data['Password'])
        if result is None:
            try:
                show_ikr_login_form('Credentials provided are incorrect')
            except:
                pass
        else:
            config['userid'] = form_data['User ID']
            config['password'] = form_data['Password']
            app.exit(result=form_data)

    def add_another_directory():
        pass

    def add_directory():
        pass

    def set_db_path():
        pass

    def set_log_path():
        pass

    def save_config():
        pass

    def show_ikr_login_form(error=None):

        form(
            title=HTML('<style bg="black" fg="white">IKR Python Client Setup</style>'),
            text=HTML('<style fg="red">' + str(error if error is not None else '') + '</style>\nProvide your IKR user ID and password below:'),
            inputs=[
                {'label': 'User ID', 'padding': 2, 'type': 'text'},
                {'label': 'Password', 'padding': 1, 'type': 'password'},
            ],
            buttons=[
                {'type': 'ok', 'handler': login}
            ]
        )

    def show_directory_setup_form(error=None):
        form(
            title=HTML('<style bg="black" fg="white">IKR Python Client Setup</style>'),
            text='Add a file/directory to the registry:',
            inputs=[
                {'label': 'Directory', 'padding': 2, 'type': 'text'},
                {'label': 'Recursive', 'padding': 2, 'type': 'switch'},
            ],
            buttons=[
                {
                    'title': 'Add another',
                    'handler': None
                },
                {
                    'title': 'Finish',
                    'handler': None
                },
                'cancel'
            ]
        )

    def show_dbpath_setup_form():
        pass

    def show_logpath_setup_form():
        pass

    def show_complete_dialog():
        pass


    show_ikr_login_form()
    show_directory_setup_form()

if (len(sys.argv) > 0 and sys.argv[1] != "sdist") or len(sys.argv) == 0:
    configure()
