import subprocess

# get the version from the most recent tag
def get_version():
    try:
        tag = subprocess.check_output(['git', 'describe', '--tags']).strip().decode('utf-8')
        version = tag[:(min(tag.find('-'), len(tag)))]
    except subprocess.CalledProcessError:
        version = "0.0.0"
    return version

def UpdateVersion():

    # update the version in my version file
    version = get_version()
    with open('src/ccbcge/version.py', 'w') as version_file:
        version_file.write(f'__version__ = "{version}"\n')

    # read the toml file
    with open('pyproject.toml', 'r') as read_file:
        lines = read_file.readlines()

    # update the toml file with the new version
    with open('pyproject.toml', 'w') as write_file:
        for line in lines:
            if line.startswith('version ='):
                write_file.write(f'version = "{version}"\n')
            else:
                write_file.write(line)

if __name__ == "__main__":
    UpdateVersion()
    print("Version Updated")
