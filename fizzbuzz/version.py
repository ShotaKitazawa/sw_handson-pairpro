class Version():
    def __init__(self, major, minor, patch):
        if not (isinstance(major, int) and isinstance(minor, int) and isinstance(patch, int)):
            raise TypeError
        if major < 0 or minor < 0 or patch < 0:
            raise ValueError
        self.major = major
        self.minor = minor
        self.patch = patch

    def __str__(self):
        return str(self.major) + "." + str(self.minor) + "." + str(self.patch)

    def __eq__(self, other):
        return self.major == other.major and self.minor == other.minor and self.patch == other.patch

    def __ne__(self, other):
        return not (self.major == other.major and self.minor == other.minor and self.patch == other.patch)

    def __lt__(self, other):
        return self.major > other.major or self.minor > other.minor or self.patch > other.patch

    def __le__(self, other):
        return self == other or self.major > other.major or self.minor > other.minor or self.patch > other.patch

    def __gt__(self, other):
        return self.major < other.major or self.minor < other.minor or self.patch < other.patch

    def __ge__(self, other):
        return self == other or self.major < other.major or self.minor < other.minor or self.patch < other.patch
