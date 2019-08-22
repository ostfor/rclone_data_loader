from setuptools import setup, find_packages

required = []
setup(name='rclone_data_loader',
      use_scm_version=True,
      setup_requires=['setuptools_scm'],
      install_requires=required,
      description='Open visualization tools for training process',
      url='http://github.com/ostfor/rclone_data_loader',
      author='Denis Brailovsky',
      author_email='denis.brailovsky@gmail.com',
      license='MIT',
      data_files=[('', ['LICENSE'])],
      packages=["rclone_data_loader.{}".format(pkg) for pkg in find_packages("rclone_data_loader")] + ["rclone_data_loader"],

      zip_safe=False)
