from setuptools import setup

setup_requires = []

install_requires = [
      'grpcio == 1.8.4'
]
dependency_links = []

setup(name='grpc_wrapper',
      version='0.3',
      description='simple client and server for grpc',
      url='',
      author='loveloper',
      author_email='loveloper44@gmail.com',
      license='MIT',
      packages=['grpc_wrapper', 'grpc_wrapper.pb2'],
      zip_safe=False)
