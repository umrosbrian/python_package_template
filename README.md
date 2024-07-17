This repo is a template for a pip installable package.

## make a new package from this repo

1. `git clone git@github.com:umrosbrian/python_package_template`
2. Rename the `python_package_template` directory to the name of the package you'll be creating; we'll call this *package name*.
3. Remove the `.git` directory with `rm -rf <package name>/.git`.
4. The directory `src/pkg` needs to be renamed to the package name along with the line `src/pkg.egg-info` in `.gitignore`.  This can all be done using ` python <path to pyutils/recursively_replace.py> --path <path to package name directory> --old_string pkg --new_string <package name> --all --dry_run`.  Remove `--dry_run` to do the actual replacements if all looks good.
5. Add dependency packages in `setup.cfg`.
6. Locally install the package with `pip install -e ./<package name>`.
7. A new repo can then be initialized if needed.
