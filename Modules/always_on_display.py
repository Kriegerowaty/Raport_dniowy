from main import window


def always_on_display():
    if window.attributes("-topmost"):
        window.attributes("-topmost", False)
    else:
        window.attributes("-topmost", True)
