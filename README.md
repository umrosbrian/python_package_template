This repo is a template for a pip installable package.

## make a new package from this repo

1. `git clone git@github.com:umrosbrian/python_package_template`
2. Rename the `python_package_template` directory to the name of the package you'll be creating; we'll call this *package name*.
    - Python package names should be lowercase and need to be one word (no spaces).  Underscores won't break anything, but they aren't the standard.
3. Remove the `<package name>/.git` directory.
    - You'll probably want to initialize a new using the new package name.
4. The `<package name>/src/pkg` directory needs to be renamed to the `<package name>/src/<package name>`.
5. If you've initialized a new repo, modify `<package name>/.gitignore` by replacing the line `src/pkg.egg-info` with `src/<package name>.egg-info`.
6. All of the package's code goes in the `<package name>/src/<package name>` directory.
7. Add dependency packages in the `install_requires` directive of `<package name>/setup.cfg`.  Change info in the `metadata` directive too while you're here.
8. Upgrade pip with `pip install -U pip` to ensure that you can install editable packages.
9. Locally install the package with `pip install -e ./<package name>`.
