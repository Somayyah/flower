import logging

def setup_logging(level=logging.INFO):
    logging.basicConfig(
        filename="flower.log",
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    )