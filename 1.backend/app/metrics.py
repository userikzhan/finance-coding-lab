upload_counter = 0


def increment_uploads():
    global upload_counter
    upload_counter += 1


def get_uploads():
    return upload_counter
