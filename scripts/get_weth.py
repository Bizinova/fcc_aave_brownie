from scripts.helpful_scripts import get_account
from brownie import accounts, network, config, interface


def main():
    get_weth()


def get_weth():
    """
    Mints WETH by depositing ETH
    """
    # ABI
    # Address
    account = get_account()
    weth = interface.IWeth(config["networks"][network.show_active()]["weth_token"])
    tx = weth.deposit({"from": account, "value": 0.05 * 10 ** 18})
    tx.wait(1)
    print("Received 0.05 WETH")
    return tx
