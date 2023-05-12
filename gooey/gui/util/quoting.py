import sys


if sys.platform.startswith("win"):
  def quote(value):
    return f""""{f'{value}'.replace('"', '""')}\""""
else:  # POSIX shell
  def quote(value):
    return u"'{}'".format(f'{value}'.replace(u"'", u"'\\''"))

