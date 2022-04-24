def set_alarm(employed, vacation):
    return employed and not vacation


assert not set_alarm(True, True)
assert not set_alarm(False, True)
assert not set_alarm(False, False)
assert set_alarm(True, False)
