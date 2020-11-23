import uuid
import structlog

logger = structlog.get_logger()


def custom_logging_for_function(original_function):
    trace_id = str(uuid.uuid4())
    global_var = original_function.__globals__
    global_var['trace_id'] = trace_id
    function_name = f'{original_function.__module__}.{original_function.__name__}'

    def new_function(*args, **kwargs):
        logger.info(
            'Before calling the function', function_name=function_name, trace_id=trace_id, args=args, kwargs=kwargs
        )
        try:
            result = original_function(*args, **kwargs)
        except Exception as e:
            logger.warning(
                'An issue occured during the function', function_name=function_name, trace_id=trace_id, error=str(e)
            )
            raise Exception(e)
        logger.info('After calling the function', function_name=function_name, trace_id=trace_id, result=result)

        return result

    return new_function


def custom_logging_for_class(Cls):
    class NewCls:
        def __init__(self, *args, **kwargs):
            self.oInstance = Cls(*args, **kwargs)

        def __getattribute__(self, s):
            """
            this is called whenever any attribute of a NewCls object is accessed. This function first tries to
            get the attribute off NewCls. If it fails then it tries to fetch the attribute from self.oInstance (an
            instance of the decorated class). If it manages to fetch the attribute from self.oInstance, and
            the attribute is an instance method then `time_this` is applied.
            """
            try:
                x = super(NewCls, self).__getattribute__(s)
            except AttributeError:
                pass
            else:
                return x
            x = self.oInstance.__getattribute__(s)
            if type(x) == type(self.__init__):  # an instance method
                return custom_logging_for_function(x)
            else:
                return x

    return NewCls
