class Version():
    def __init__(self, major, minor, patch):
        if major < 0 or minor < 0 or patch < 0:
            raise Exception
        self.major = major
        self.minor = minor
        self.patch = patch
