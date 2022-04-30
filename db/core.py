
import sqlite3

class DB(object):
	def __init__(self, db_name) -> None:
		self.db = sqlite3.connect(db_name)
		

	def does_table_exist(self, table: str) -> bool:
		
		# check if the table exists
		cursor = self.db.cursor()
		cursor.execute(f'SELECT name FROM sqlite_master WHERE type="table" AND name="{table}"')
		
		# If there is no such table, it will return None,
		# so we have to check if it is None before returning
		a = cursor.fetchone()

		return a is not None and a[0] == table
	
	def new_table(self, table: str, cols: dict={'key': 'TEXT', 'value': 'TYPE'}) -> None:

		# Setup the table column values
		columns: str = ''
		for key, val in cols.items():
			columns += f'{key} {val},'

		# Remove the ',' at the end of the columns ---------------------v
		self.db.execute(f'CREATE TABLE IF NOT EXISTS {table} ({columns[:-1]})')

	def del_table(self, table: str) -> None:
		# delete a table if it exists
		self.db.execute(f'DROP TABLE IF EXISTS {table}')

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
