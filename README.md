# decoratorAndStructlog

Small project to play with the decorators and the Structlog library.

## Goal of the project
Create a decorator that will use structlog to add a logging system to each function of a class.

One of the goal is to have a trace_id to follow the code and to get easily information about the context when the function is called. 
For instance, the parameters provided to the function and the error message ...

## Different types of output

### Development
![development output](https://raw.githubusercontent.com/dianedelallee/decoratorStructlog/master/resources/output_development.png "Development output")

### Production
![production output](https://raw.githubusercontent.com/dianedelallee/decoratorStructlog/master/resources/output_production.png "Production output")


## References
* [Struct log library](https://www.structlog.org/en/20.1.0/index.html)
* [Nice Article about struclog](https://atymo.me/blog/python_logging.html)
