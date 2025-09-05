from typing import Any
import logging

LOGGER_DB = logging.getLogger(__name__)

def cast_to_schema(schema: Any, record: dict | list[dict] | None) -> Any:
    """
    Cast a dictionary to a schema object.
    
    Args:
        schema (Any): The schema to cast to.
        record (dict): The dictionary to cast.
        
    Returns:
        Any: The casted object.
    """
    
    if record is None:
        return None
    
    if isinstance(record, list):
        return [schema.from_dict(r) for r in record]
    else:
        return schema.from_dict(record)
    
def log(message: str, level: int = logging.INFO, *args, **kwargs) -> None:
    """
    Log a message with the specified logging level.
    
    Args:
        message (str): The message to log.
        level (int): The logging level.
    """
    
    LOGGER_DB.log(level, message, *args, **kwargs)