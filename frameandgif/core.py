import ffmpeg
from .errors import GIFBadFormat


class FFmpeg:
    def __init__(self, filename, method, params, output):
        self.filename = filename
        self.method = method
        self.params = params
        self.output = output

        self.probe = ffmpeg.probe(self.filename)
        self.duration = self.probe['streams'][0]['duration']
        self.width = self.probe['streams'][0]['width']

    def extract_frame(self, timestamp):
        (
            ffmpeg
            .input(self.filename, ss=timestamp)
            .filter('scale', self.width, -1)
            .output(self.output, vframes=1)
            .run()

        )

    def create_gif(self, start, duration):

        if self.output.split('.')[-1].lower() != 'gif':
            raise GIFBadFormat
        else:
            (
                ffmpeg
                .input(self.filename, ss=start, t=duration)
                .filter('scale', self.width, -1)
                .output(self.output)
                .run()
            )

    def run(self):
        if self.method == 'extract_frame':
            self.extract_frame(self.params[0])

        elif self.method == 'create_gif':
            self.create_gif(self.params[0], self.params[1])

