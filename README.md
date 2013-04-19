So you want commands?
=====================

Simple demonstration of setuptools console_scripts entry points.

Firs things, first.
-------------------

By default, the project layout should look something like this:

    .
    ├── README.md
    ├── setup.py
    └── tools
        ├── __init__.py
        ├── commands.py
        ├── runner
        │   ├── __init__.py
        │   └── example.py
        └── version.py

Firstly, use virtualenv:

    virtualenv .
    source bin/active

Then, run development mode:

    python setup.py develop

Output should look something like this:

    running develop
    running egg_info
    writing tools.egg-info/PKG-INFO
    writing top-level names to tools.egg-info/top_level.txt
    writing dependency_links to tools.egg-info/dependency_links.txt
    writing entry points to tools.egg-info/entry_points.txt
    reading manifest file 'tools.egg-info/SOURCES.txt'
    writing manifest file 'tools.egg-info/SOURCES.txt'
    running build_ext
    Creating /Users/amarshall/Desktop/console/lib/python2.6/site-packages/tools.egg-link (link to .)
    tools 0.0.1 is already the active version in easy-install.pth
    Installing runner script to /Users/amarshall/Desktop/console/bin
    Installing foo script to /Users/amarshall/Desktop/console/bin
    Installing bar script to /Users/amarshall/Desktop/console/bin
    Installing example script to /Users/amarshall/Desktop/console/bin

    Installed /Users/amarshall/Desktop/console
    Processing dependencies for tools==0.0.1
    Finished processing dependencies for tools==0.0.1

What just happened?
-------------------

By running ``python setup.py develop`` you installed the package in
development mode, which basically means that the current source tree was
installed into your path by means of creating a tools.egg-link file in your
site-packages directory (currently in your active virtualenv) that links to
the current directory.  Among other things, it also created some commands in
bin/ (currently part of your path, again, thanks to virtualenv).

This process lets you test the package installation process without interfering
with your system environment, while still being able to make changes without
having to repeatedly re-install the package.  Ultimately, when your package is
installed as an egg, the changes will be made at the system level (or user
level, if installing to ~/.local, which is recommended)

You'll notice that the following commands were installed into ``bin/``:

- runner
- foo
- bar
- example

Defining commands
-----------------

Take a look at setup.py.  You'll notice a section that lookes like this:

    entry_points = {
      'console_scripts': [
        'runner = tools.runner:main',
        'example = tools.runner.example:Example',
        'foo = tools.commands:foo',
        'bar = tools.commands:bar'
      ]
    }

Each entry correlates to a callable within the package namespace.  For example,
the ``runner`` command correlates with the behavior defined in
``tools/runner/__init.py:main()``, ``example`` with
``tools/runner/example.py:Example.__init__()``, ``foo`` with
``tools/commands.py:foo()``, and ``bar`` with ``tools/commands.py:bar()``.

To add new commands, add the appropriate entry under ``console_scripts``, and
re-run ``python setup.py develop`` to install them.