import dataclasses


@dataclasses.dataclass(frozen=True)
class RetrieveAccountDTO:
    id: int