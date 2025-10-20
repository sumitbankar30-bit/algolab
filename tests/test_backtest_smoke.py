from utils.config import load_config
from backtests.runner import run_backtest

def test_backtest_smoke():
    cfg = load_config("configs/default.yaml")
    summary = run_backtest(cfg)
    assert "total_return" in summary and "sharpe_annualized" in summary