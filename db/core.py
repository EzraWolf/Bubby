
class DB(object):
	def __init__(self) -> None:
		pass

	def new_db(self, db_name: str) -> None:
		pass

	def del_db(self, db_name: str) -> None:
		pass

	def new_table(self, table: str) -> None:
		pass

	def del_table(self, table: str) -> None:
		pass

	def new_col(self, table: str, col: str) -> None:
		pass

	def del_col(self, table: str, col: str) -> None:
		pass

	def new_row(self, table: str, row: str) -> None:
		pass

	def del_row(self, table: str, row: str) -> None:
		pass

	def set_row_val(self, table: str, row: str, val: dict) -> None:
		pass

	def get_row_val(self, table: str, row: str) -> dict:
		pass

	def add_row_val(self, table: str, row: str, val: float) -> None:
		pass

	def sub_row_val(self, table: str, row: str, val: float) -> None:
		pass

	def psh_row_val(self, table: str, row: str, val: dict) -> None:
		pass

	def pop_row_val(self, table: str, row: str) -> dict:
		pass

	def has_row_val(self, table: str, row: str) -> bool:
		pass
