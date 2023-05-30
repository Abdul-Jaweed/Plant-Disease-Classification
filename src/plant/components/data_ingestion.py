import os
import urllib.request as request
from zipfile import ZipFile
from tqdm import tqdm
from pathlib import Path
from plant.entity import DataIngestionConfig
from plant import logger
from plant.utils import get_size


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    
    def download_file(self):
        logger.info(f"Trying to download file .....")
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading started...")
            filename, headers = request.urlretrieve(
                url = self.config.source_URL,
                filename = self.config.local_data_file
            )


    def unzip_and_clean(self):
        logger.info(f"Unzipping file")
        with ZipFile(self.config.local_data_file, 'r') as zf:
            for f in zf.namelist():
                self._preprocess(zf, f, self.config.unzip_dir)

    def _preprocess(self, zf, f, working_dir):
        target_filepath = os.path.join(working_dir, f)
        if not os.path.exists(target_filepath):
            zf.extract(f, working_dir)

        if os.path.isfile(target_filepath) and os.path.getsize(target_filepath) == 0:
            os.remove(target_filepath)