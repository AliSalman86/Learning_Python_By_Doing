# custom errors can be created by inheritance from built-in errors in Python.
class RunTimeErrors(TypeError):
    """This is a custom error, exception raised when a specific error code is needed"""
    def __init__(self, msg, code):
        super().__init__(f"Error code {code}: {msg}")
        self.code = code

#raise MyCustomError('This is a custom error', 500)
err = RunTimeErrors("A return expected, 0 receieved", 500)
print(err)
print(err.__doc__)    # -> This is a custom error, exception raised when a specific error code is needed