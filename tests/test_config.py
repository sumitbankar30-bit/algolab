from pathlib import Path
from utils.config import load_config, AppConfig

def test_config_loads(tmp_path: Path):
    cfg = load_config(Path("configs/default.yaml"))
    assert isinstance(cfg, AppConfig)
    assert cfg.features.sma_long > cfg.features.sma_short