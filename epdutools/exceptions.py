class ePDUException(Exception):
    def __init__(self, *args, **kwargs):
        super(ePDUException, self).__init__(*args)
        self.error = kwargs.get("error", None)