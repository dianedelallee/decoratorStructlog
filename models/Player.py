from typing import Optional

import structlog
from custom_logging import custom_logging_for_class

logger = structlog.get_logger()


@custom_logging_for_class
class Player:

    def __init__(self, name: Optional[str] = None, age: Optional[int] = None) -> None:
        self.name = name if name else 'Player 1'
        self.age = age if age else 18
        self.level = 0
        self.experience = 0

    def get_name(self):
        logger.info('trying to get the name of the user', trace_id=trace_id)
        return self.name

    def set_name(self, new_name: str) -> None:
        logger.critical('trying to set the name of the user', trace_id=trace_id)
        self.name = new_name

    def get_age_in_cat_live(self) -> int:
        logger.info('trying to get the aage in cat referencial', trace_id=trace_id)
        return self.age * self._get_cat_referential()

    def _get_cat_referential(self):
        logger.info('get cat referential', trace_id=trace_id)
        return 7
