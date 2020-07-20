import logging
import traceback

logger = logging.getLogger()


def functionLogger(fn):
    from functools import wraps
    @wraps(fn)
    def wrapper(*args, **kwargs):
        logger.info('About to run %s' % fn.__name__)
        try:
            fn(*args, **kwargs)
            out = fn(*args, **kwargs)
            return out
        except Exception:
            logger.error(
                    'Error running {0}: {1}'.format(
                                fn.__name__,
                                traceback.format_exc()
                            )
                    )
        logger.info('Done running {0}'.format(fn.__name__))
    return wrapper
