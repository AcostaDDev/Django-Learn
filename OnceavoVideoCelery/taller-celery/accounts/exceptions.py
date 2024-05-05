from .models import Account, Transfer, TransferStates, Notification


class AccountDoesntHaveEnoughMoney(Exception):
    pass


class TransferError(Exception):
    pass


class AccountDoesntExistsError(Exception):
    pass
