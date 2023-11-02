import os
from pathlib import Path
from types import SimpleNamespace
from typing import Optional

from alembic.config import Config

PROJECT_PATH_POSIX = Path(__file__).parent.parent.resolve()
PROJECT_PATH = str(PROJECT_PATH_POSIX)


def make_alembic_config(cmd_opts: Optional[SimpleNamespace],
                        base_path: str = PROJECT_PATH) -> Config:
    """ Создает объект конфигурации alembic на основе аргументов командной строки,
        подменяет относительные пути на абсолютные.
    """
    # Подменяем путь до файла alembic.ini на абсолютный
    if not os.path.isabs(cmd_opts.config):
        cmd_opts.config = os.path.join(base_path, cmd_opts.config)

    config = Config(file_=cmd_opts.config, ini_section=cmd_opts.name,
                    cmd_opts=cmd_opts)

    # Подменяем путь до папки с alembic на абсолютный
    alembic_location = config.get_main_option('script_location')
    if not os.path.isabs(alembic_location):
        config.set_main_option('script_location',
                               os.path.join(base_path, alembic_location))
    if cmd_opts.pg_url:
        config.set_main_option('sqlalchemy.url', cmd_opts.pg_url)

    return config


# def fill_prepared_data():
