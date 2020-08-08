"""
The module responsible for the process of saving data to local storage
"""

import logging
import os

logger = logging.getLogger()


def save_source_locally(filename, output_dir, content) -> bool:
    """
    The function of saving data to the specified directory
    by the specified name

    Args:
        filename (str): The name of the file to save
        output_dir (str): The path to the directory where the file
            will be stored
        content (str): Data to be saved to file

    Raises:
        PermissionError : can't create directory or file
        Exception : in all other cases
    """
    if not os.path.exists(output_dir):
        logger.debug(
            " ".join((
                "The specified directory does not exist. ",
                "Create a new directory '{}'".format(output_dir)
            ))
        )
        try:
            os.makedirs(output_dir)
        except PermissionError:
            logger.error(
                "Can't create directory {}. Permission denided".format(
                    output_dir
                )
            )
            raise
        except Exception as error:
            logger.error(
                "Can't create directoryi {}. {}".format(output_dir, error)
            )
            raise
        else:
            logger.debug(
                "New directory '{}' created successfully".format(output_dir)
            )

    file_path = os.path.join(output_dir, filename)
    try:
        with open(file_path, 'w') as file_object:
            file_object.write(content)
    except PermissionError:
        logger.error("Insufficient rights to write file {}".format(file_path))
        raise
    except Exception as error:
        logger.error(error)
        raise
