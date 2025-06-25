from dataclasses import dataclass


@dataclass
class Country:
    StateAbb: str
    CCode: int
    StateNme: str

    def __hash__(self):
        return hash(self.CCode)

    def __eq__(self, other):
        return self.CCode == other.CCode

    def __lt__(self, other):
        return self.StateNme < other.StateNme

    def __str__(self):
        return self.StateNme
