class BakingStep:
    def __init__(self, title, duration, waitDuration):
        self._title = title
        self._duration = duration
        self._waitDuration = waitDuration
        self._totalDuration = duration + waitDuration

    def get_duration(self):
        return self._duration

    def get_title(self):
        return self._title

    def get_waitDuration(self):
        return self._waitDuration

    def get_totalDuration(self):
        return self._totalDuration
