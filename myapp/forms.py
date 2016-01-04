from datetime import datetime
import os
import errno

from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from models import Gif

from gif_highlights import settings


class UserLogin(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')


class UploadPictureForm(forms.Form):
    picture = forms.ImageField(label='Select an Image')

    def save_image(self, user, pic):
        """"Function saves image on disk in a path using default image
         folder and separate directory for each user, and returns the
         path of the image to be stored in db"""

        # setting directory to MEDIA_ROOT/MEDIA_URL from settings +
        # user directory
        # directory = settings.MEDIA_ROOT + \
        #             user.username.encode('ascii', 'ignore') + '/'
        directory = settings.MEDIA_ROOT

        # check if directory exists, if not create
        try:
            os.makedirs(directory)
        except OSError as exception:
            if exception.errno != errno.EEXIST:
                raise

        # change filename to current date
        directory += datetime.today().strftime('%d-%m-%Y')

        # write file to disk
        destination = open(directory, 'wb+')
        for chunk in pic.chunks():
            destination.write(chunk)
            destination.close()

        # return path to image
        return directory

    @staticmethod
    def get_image(user):

        try:
            pic_path = Gif.objects.get(id=1)
            pic_path = pic_path.replace(settings.MEDIA_ROOT, '')

        except ObjectDoesNotExist:
            pic_path = None

        return pic_path
