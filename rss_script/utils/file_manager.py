import json
import os
import yaml
from dotenv import load_dotenv
from ..types import SubredditConfig, Credentials, Database


def load_credentials() -> Credentials:
    """
    Loads the credentials from the environment variables

    Returns:
        The credentials from the environment variables
    """
    load_dotenv()
    return Credentials(
        user=os.getenv('USER_NAME'),
        password=os.getenv('PASSWORD'),
        client_id=os.getenv('CLIENT_ID'),
        client_secret=os.getenv('CLIENT_SECRET')
    )


def load_config(config_file: str) -> list[SubredditConfig]:
    """
    Loads the config file

    Args:
        config_file: Absolute path to the config file

    Returns:
        The configurations and credentials from the config file
    """
    try:
        with open(config_file) as yaml_data_file:
            config = yaml.safe_load(yaml_data_file)
            return config
    except Exception as e:
        print(f'Error loading {config_file}: {str(e)}')


def load_db(filename: str) -> Database:
    """
    Loads the database file

    Args:
        filename: Absolute path to the database JSON file

    Returns:
        The dictionary stored in the database JSON file if it exists, otherwise an empty dictionary
    """
    try:
        with open(filename) as file:
            return json.load(file)
    except Exception as e:
        print(f'Error loading {filename}: {str(e)}')
        print(f'Creating new db...')
        return {}


def update_db(filename: str, db: Database) -> None:
    """
    Updates the database file

    Args:
        filename: Path to the database JSON file
        db: The dictionary to be stored in the database JSON file

    Returns:
        None
    """
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(filename, 'w') as file:
        json.dump(db, file, indent=2)
