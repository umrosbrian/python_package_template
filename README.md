his repo is a template for a pip installable package.

## make a new package from this repo

1. `git clone git@github.com:umrosbrian/python_package_template`
2. Rename the `python_package_template` directory to the name of the package you'll be creating; we'll call this *package name*.
3. Remove the `<package name>/.git` directory with `rm -rf <package name>/.git`.
4. The directory `src/pkg` needs to be renamed to the package name along with the line `src/pkg.egg-info` in `.gitignore`.
5. Add dependency packages in `setup.cfg`.
6. Upgrade pip with `pip install -U pip` to ensure that you can install editable packages.
7. Locally install the package with `pip install -e ./<package name>`.
8. A new repo can be initialized if needed.
