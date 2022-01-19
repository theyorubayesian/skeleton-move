"""
"This script removes whitespaces in columns names and fills missing values"
"""
import argparse
import logging
import time


logging.basicConfig(
    filename=f"logs/{__name__}_{time.time()}.log",
    format="%(asctime)s - %(levelname)s - %(name)s - PID: %(process)d -  %(message)s",
    datefmt="%m/%d/%Y %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


def go(args):
    # --------------
    # YOUR CODE HERE
    # --------------
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This script cleans the transactions data")

    parser.add_argument(
        "--threshold",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--input_data",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )

    parser.add_argument(
        "--output_data",
        type= # TODO,
        default= # TODO,
        help= # TODO,
        required= # TODO,
    )


    args = parser.parse_args()
    go(args)
