from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from {{ cookiecutter.module_name }}.config import MODELS_DIR, PROCESSED_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    features_path: Path = PROCESSED_DATA_DIR / "some_features.csv",
    labels_path: Path = PROCESSED_DATA_DIR / "some_labels.csv",
    model_path: Path = MODELS_DIR / "some_model.pkl",
):
    logger.info("Training some model...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Modeling training complete.")


if __name__ == "__main__":
    app()
