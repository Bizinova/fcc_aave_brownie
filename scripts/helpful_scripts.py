from brownie import (
    network,
    config,
    accounts,
    Contract,
    interface,
)

FORKED_LOCAL_ENVIRONMENTS = ["mainnet-fork", "mainnet-fork-dev2"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = ["development", "ganache-local-two"]


def get_account(index=None, id=None):
    # method 1 - local chain: accounts[0]
    # method 2 - env variable: accounts.add("env")
    # method 3 - cmd line native: accounts.load("id")
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENVIRONMENTS
    ):
        return accounts[0]
    return accounts.add(config["wallets"]["from_key"])
