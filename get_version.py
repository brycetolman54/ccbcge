import subprocess

# get the version from the most recent tag
def get_version():
    try:
        tag = subprocess.check_output(['git', 'describe', '--tags'], text=True)
        version = tag[:(min(tag.find('-'), len(tag)))]
    except subprocess.CalledProcessError:
        with open('src/ccbcge/version.py', 'r') as version_file:
            line = version_file.readlines()
            version = line[14:]
    return version

def UpdateVersion(version):

    # update the version in my version file
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
    version = get_version()
    UpdateVersion(version)
    print(f"\nVersion Updated: {version}\n")
