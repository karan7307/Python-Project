import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def log_info(message):
    logging.info(message)

def log_error(message):
    logging.error(message)

def format_prediction(score):
    """
    Formats the burnout score as a percentage.
    """
    return f"{score * 100:.2f}%"
