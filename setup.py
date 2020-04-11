"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# flake8: noqa=E501
from os import path
from io import open
from setuptools import setup, find_packages

HERE = path.abspath(path.dirname(__file__))

with open(path.join(HERE, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='websys2020_srvnet_example_app',  # Required
    version='0.0.1',  # Required
    description='WEBSYS2020 Server/Network course, Example Django project',  # Optional
    long_description=LONG_DESCRIPTION,  # Optional
    long_description_content_type='text/markdown',  # Optional (see note above)
    url='https://github.com/netmarkjp/websys2020-srvnet-example-app',  # Optional
    author='Toshiaki Baba',  # Optional
    author_email='toshiaki@netmark.jp',  # Optional
    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP',

        # Pick your license as you wish
        'License :: OSI Approved :: MIT License',
        'Framework :: Django :: 2.2',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        # These classifiers are *not* checked by 'pip install'. See instead
        # 'python_requires' below.
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    keywords='websys2020 example django',  # Optional
    package_dir={'': 'app'},  # Optional
    packages=find_packages(where='app'),  # Required
    python_requires='>=3.6',

    # This field lists other packages that your project depends on to run.
    # Any package you put here will be installed by pip when your project is
    # installed, so they must be valid existing projects.
    #
    # For an analysis of "install_requires" vs pip's requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'django~=2.2',
    ],  # Optional

    # List additional groups of dependencies here (e.g. development
    # dependencies). Users will be able to install these using the "extras"
    # syntax, for example:
    #
    #   $ pip install sampleproject[dev]
    #
    # Similar to `install_requires` above, these must be valid existing
    # projects.
    extras_require={  # Optional
        'prod': [
            'gunicorn',
            'mysqlclient',
        ],
        'dev': [
            'flake8',
            'pylint',
            'coverage',
            'ipython',
            'autopep8',
        ],
    },

    # # If there are data files included in your packages that need to be
    # # installed, specify them here.
    # #
    # # If using Python 2.6 or earlier, then these have to be included in
    # # MANIFEST.in as well.
    # package_data={  # Optional
    #     'sample': ['package_data.dat'],
    # },

    # # Although 'package_data' is the preferred approach, in some case you may
    # # need to place data files outside of your packages. See:
    # # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files
    # #
    # # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],  # Optional

    # # To provide executable scripts, use entry points in preference to the
    # # "scripts" keyword. Entry points provide cross-platform support and allow
    # # `pip` to create the appropriate form of executable for the target
    # # platform.
    # #
    # # For example, the following would provide a command called `sample` which
    # # executes the function `main` from this package when invoked:
    # entry_points={  # Optional
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },

    # List additional URLs that are relevant to your project as a dict.
    #
    # This field corresponds to the "Project-URL" metadata fields:
    # https://packaging.python.org/specifications/core-metadata/#project-url-multiple-use
    #
    # Examples listed include a pattern for specifying where the package tracks
    # issues, where the source is hosted, where to say thanks to the package
    # maintainers, and where to support the project financially. The key is
    # what's used to render the link text on PyPI.
    project_urls={  # Optional
        'Source': 'https://github.com/netmarkjp/websys2020-srvnet-example-app/',
    },
)
