class Version():
    def __init__(self, major, minor, patch):
        if major < 0 or minor < 0 or patch < 0:
            raise Exception
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return str(self.major) + "." + str(self.minor) + "." + str(self.patch)
