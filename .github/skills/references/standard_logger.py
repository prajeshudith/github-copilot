"""
Enterprise Standard Logging Module.
Demonstrates the required type hinting and docstring formatting.
"""

import logging
from typing import Optional, Dict, Any

def setup_secure_logger(
    name: str, 
    level: str = "INFO", 
    metadata: Optional[Dict[str, Any]] = None
) -> logging.Logger:
    """
    Initializes and returns a secure, standard logger with attached metadata.

    Args:
        name (str): The name of the logger instance.
        level (str, optional): The logging level (e.g., "DEBUG", "INFO"). Defaults to "INFO".
        metadata (Optional[Dict[str, Any]], optional): Contextual metadata to inject into logs. Defaults to None.

    Returns:
        logging.Logger: A configured Python logger instance.

    Raises:
        ValueError: If the provided logging level is invalid.
    """
    valid_levels = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    upper_level = level.upper()
    
    if upper_level not in valid_levels:
        raise ValueError(f"Invalid logging level: {level}")

    logger = logging.getLogger(name)
    logger.setLevel(getattr(logging, upper_level))
    
    # In a real scenario, metadata would be handled by a custom formatter
    if metadata:
        logger.debug(f"Logger initialized with metadata: {metadata}")

    return logger