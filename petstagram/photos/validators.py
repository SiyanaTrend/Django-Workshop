from typing import Optional

from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import UploadedFile
from django.utils.deconstruct import deconstructible

"""
 def validate_size(value):
     if value.size > 5 * 1024 * 1024:   ## = 5242880
         raise ValidationError('The maximum file size that can be uploaded is 5MB')
"""

@deconstructible
class FileSizeValidator:
    def __init__(self, file_size_mb: int, message: Optional[str] = None):
        self.file_size_mb = file_size_mb
        self.message = message

    @property
    def message(self):
        return self.__message

    @message.setter
    def message(self, value: str):
        if value is None:
            self.__message = f"The maximum file size that can be uploaded is {self.file_size_mb}MB"
        else:
            self.__message = value

    def __call__(self, value: UploadedFile) -> None:
        if value.size > self.file_size_mb * 1024 * 1024:
            raise ValidationError(self.message)
