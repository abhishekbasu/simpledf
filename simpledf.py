from typing import Any

class DataFrame:
    def __init__(self):
        object.__setattr__(self, "columns", [])

    def __setattr__(self, name: str, val: Any) -> None:
        if name in self.columns:
            getattr(self, name).append(val)
        else:
            self.columns.append(name)
            object.__setattr__(self, name, [])
            getattr(self, name).append(val)

    def __repr__(self) -> str:
        return "DataFrame columns : {}".format(self.columns)
    
    def __len__(self) -> int:
        return 0 if len(self.columns) == 0 else len(getattr(self, self.columns[0]))
