import os
import sys
import shutil

APPLICATION_NAME = 'YourAppName'
APPLICATION_DIR = '/path/to/your/application'

def create_app_bundle():
    app_bundle_path = f'./{APPLICATION_NAME}.app'
    if os.path.exists(app_bundle_path):
        shutil.rmtree(app_bundle_path)
    os.makedirs(os.path.join(app_bundle_path, 'Contents', 'MacOS'))
    os.makedirs(os.path.join(app_bundle_path, 'Contents', 'Resources'))

    # Copy your application files into the bundle
    shutil.copytree(APPLICATION_DIR, os.path.join(app_bundle_path, 'Contents', 'MacOS'))
    print(f'{APPLICATION_NAME}.app bundle created successfully at {os.path.abspath(app_bundle_path)}')

if __name__ == '__main__':
    create_app_bundle()