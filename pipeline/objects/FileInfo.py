import os
from os import path
from datetime import datetime

from .PipelineObject import PipelineObject
from formatters.decorators import visible


def test():
    fi = FileInfo("FileInfo.py")
    print(fi)


class FileInfo(PipelineObject):
    def __init__(self, filePath):
        super().__init__()
        self._filePath = path.abspath(filePath)
        self._statInfo = os.stat(self._filePath)

    @visible()
    def creationTime(self):
        return datetime.fromtimestamp(self._statInfo.st_ctime)

    @visible()
    def modificationTime(self):
        return datetime.fromtimestamp(self._statInfo.st_mtime)

    @visible()
    def accessTime(self):
        return datetime.fromtimestamp(self._statInfo.st_atime)

    @visible("0x{:X}")
    def mode(self):
        return self._statInfo.st_mode

    @visible()
    def inodeNumber(self):
        return self._statInfo.st_ino

    # TODO: replace with collection of FileInfo objects representing the links
    @visible()
    def linkCount(self):
        return self._statInfo.st_nlink

    @visible()
    def size(self):
        return self._statInfo.st_size

    @visible()
    def baseName(self):
        return path.basename(self._filePath)

    @visible()
    def dirName(self):
        return path.dirname(self._filePath)
    

