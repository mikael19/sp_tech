# Contains all snowplow tracker details

from snowplow_tracker import Tracker, Emitter, Subject, logger


SNOWPLOW_MICRO_URI = "0.0.0.0:9090"
CLOUDFRONT_URI = "ddpsbsb5cdpko.cloudfront.net"
PAGE_VIEW = "PAGE_VIEW"
FORM_SUBMIT = "FORM_SUBMIT"
STRUCT = "STRUCT_EVENT"

def success(x):
    """
    Called when an event is tracked successfully
    """
    print(str(x) + " event sent successfully!")

def failure(x, y):
    """
    Called when an event is NOT tracked successfully
    """
    print(str(y) + " events NOT sent!")

def track(type, data):
    """
    Called for the tracking of events
    input: type of event to track, data to pass
    output: No return
    """
    emitter = Emitter(SNOWPLOW_MICRO_URI, buffer_size=1, on_success=success, on_failure=failure)
    tracker = Tracker(emitter)
    # Dictionary to contain all events we want to track and their corresponding methods.
    # So we can have a more generic way to track
    dict = {
        PAGE_VIEW: tracker.track_page_view,
        FORM_SUBMIT: tracker.track_form_submit,
        STRUCT: tracker.track_struct_event
    }
    subject = Subject()
    subject.set_platform("pc")
    tracker.set_subject(subject)
    if isinstance(data, list):
        dict[type](*data)
    else:
        dict[type](data)
    logger.setLevel(10)