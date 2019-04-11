class Version():
    def __init__(self, major, minor, patch):
        if major < 0:
            raise Exception
        if minor < 0:
            raise Exception
        if patch < 0:
            raise Exception
        self.major = major
        self.minor = minor
        self.patch = patch
