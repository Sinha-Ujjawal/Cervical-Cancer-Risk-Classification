"""This script is for downloading data from kaggle
"""
import kaggle
from utils import create_dir_if_not_exists


if __name__ == "__main__":
    RAW_DATA_PATH = "./data/raw"
    DATASET_NAME = "loveall/cervical-cancer-risk-classification"
    create_dir_if_not_exists(RAW_DATA_PATH)
    kaggle.api.dataset_download_files(DATASET_NAME, path=RAW_DATA_PATH, unzip=True)
