import sys

# If Nuitka compiled...
# https://nuitka.net/doc/user-manual.html#detecting-nuitka-at-run-time
if "__compiled__" in globals():
    # Then set sys property that Gooey looks at
    # https://github.com/chriskiehl/Gooey/blob/012bb89b8911536ca3b73b96bfc0f8e98570c391/gooey/python_bindings/config_generator.py#L28-L35
    sys.frozen = True
