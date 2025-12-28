import argparse
import os
import shutil
import string

ap = argparse.ArgumentParser()
required = ap.add_argument_group('required named arguments')
required.add_argument('-p', '--package_name',
                      required=True,
                      help="Name of package that is being create.  Python package names should be lowercase and need to be one word (no spaces).  Underscores won't break anything, but they aren't the standard.")
args = vars(ap.parse_args())

old_package_name = 'python_package_template'  # name of this repo as it currently stands
new_package_name = args['package_name']
# new_package_name = 'sshauth'

def update_package_name(file_path):
    """Change all occurrences of the current package name (python_package_template) in a file to the new package
    name.
    :param file_path: path to file needing the change"""
    with open(file_path, 'r') as f:
        old_contents = f.read().splitlines()
    new_contents = []
    for line in old_contents:
        if old_package_name in line:
            new_contents.append(line.replace(old_package_name, new_package_name))
        else:
            new_contents.append(line)
    with open(file_path, 'w') as f:
        f.write('\n'.join(line for line in new_contents))
    print(f"updated package name in '{file_path}'")

## all paths are relative to the parent dir of this script
#os.chdir(os.pardir)

# exit if the package name won't work
for char in new_package_name:
    if char in string.whitespace:
        exit("Package names can't contain whitespace characters.")

# remove .git dir of the python_package_template repo
git_dir_path = os.path.join(old_package_name, '.git')
shutil.rmtree(git_dir_path)
print(f"removed '{git_dir_path}'")

# rename package directory
shutil.move(old_package_name, new_package_name)
print(f"renamed '{old_package_name}' to '{new_package_name}'")

# update the package's config file
cfg_path = os.path.join(new_package_name, 'setup.cfg')
update_package_name(cfg_path)

# change package dir in src
old_src_subdir_path = os.path.join(new_package_name, 'src', old_package_name)
new_src_subdir_path = os.path.join(new_package_name, 'src', new_package_name)
shutil.move(old_src_subdir_path, new_src_subdir_path)
print(f"renamed '{old_src_subdir_path}' to '{new_src_subdir_path}'")

# change package name in .gitignore
gitignore_path = os.path.join(new_package_name, '.gitignore')
update_package_name(gitignore_path)

# change package name sphinx-related files
sphinx_config_path = os.path.join(new_package_name, 'docs', 'conf.py')
update_package_name(sphinx_config_path)
sphinx_api_path = os.path.join(new_package_name, 'docs', 'api.rst')
update_package_name(sphinx_api_path)
sphinx_index_path = os.path.join(new_package_name, 'docs', 'index.rst')
update_package_name(sphinx_index_path)

print(f"""
Now you'll need to:

1. Change the values of the directives in the 'metadata' section of '{cfg_path}'.
2. Add dependency packages in the 'install_requires' directive of '{cfg_path}'.
3. Optionally, delete this script with 'rm {new_package_name}/set_package_name.py', also remove the README.md if needed.
4. Optionally, initiate a new git repo in the '{new_package_name}' directory.
5. Add the package's code to the '{new_src_subdir_path}' directory.
6. Upgrade pip with 'pip install -U pip' to ensure that you can install editable packages.
7. Locally install the package with 'pip install -e ./{new_package_name}'.""")
