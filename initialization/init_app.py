import structlog


def init_app():
    structlog.configure(
        processors=[
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer(indent=2, sort_keys=True),  # for production
            # structlog.dev.ConsoleRenderer()   # for development
        ],
        context_class=dict,
        cache_logger_on_first_use=True,
    )
