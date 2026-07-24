# === Stage 23: Add tag add/remove helpers and tag-based summaries ===
# Project: PantryMate
class PantryItem:
    def __init__(self, name: str = "", expiry_date: datetime.date | None = None):
        self.name = name
        self.expiry_date = expiry_date

    @property
    def is_expired(self) -> bool:
        if self.expiry_date is None:
            return False
        return self.expiry_date < datetime.date.today()

    @classmethod
    def from_csv_line(cls, line: str, delimiter: str = ",") -> "PantryItem":
        parts = line.strip().split(delimiter)
        if len(parts) >= 2:
            name = parts[0].strip()
            try:
                expiry_date = datetime.date.fromisoformat(parts[1].strip())
            except ValueError:
                expiry_date = None
        else:
            name = line.strip()
            expiry_date = None
        return cls(name=name, expiry_date=expiry_date)

    def to_csv_line(self, delimiter: str = ",") -> str:
        if self.expiry_date is not None:
            return f"{self.name}{delimiter}{self.expiry_date.isoformat()}"
        else:
            return self.name


class PantryMate:
    def __init__(self):
        self.items: list[PantryItem] = []

    @property
    def total_items(self) -> int:
        return len(self.items)

    @property
    def expired_items(self) -> list[PantryItem]:
        return [item for item in self.items if item.is_expired]

    @classmethod
    def from_csv(cls, file_path: str, delimiter: str = ",") -> "PantryMate":
        pantry_mate = cls()
        with open(file_path, 'r') as file:
            lines = file.readlines()
        for line in lines[1:]:  # skip header
            item = PantryItem.from_csv_line(line.strip(), delimiter)
            if item.name:
                pantry_mate.items.append(item)
        return pantry_mate

    def to_csv(self, file_path: str, delimiter: str = ",") -> None:
        with open(file_path, 'w') as file:
            file.write("Name,Expiry Date\n")
            for item in self.items:
                file.write(item.to_csv_line(delimiter) + "\n")

    @classmethod
    def from_file(cls, file_path: str) -> "PantryMate":
        return cls.from_csv(file_path)

    def to_file(self, file_path: str) -> None:
        self.to_csv(file_path)


def main():
    pantry_mate = PantryMate()
    pantry_mate.items.append(PantryItem("Rice", datetime.date(2025, 12, 31)))
    pantry_mate.items.append(PantryItem("Oil", datetime.date(2024, 6, 15)))
    print(f"Total items: {pantry_mate.total_items}")
    print(f"Expired items: {[item.name for item in pantry_mate.expired_items]}")


if __name__ == "__main__":
    main()
