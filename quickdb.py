import sqlite3
from sqlite3.dbapi2 import Cursor
from typing import Any

class SQLITE:

    def __init__(self, dbname: str = None):
        if dbname == None:
            dbname = 'database.db'

        self.sqlite = sqlite3.connect(dbname)

        self.db = self.sqlite.cursor()

        self.db.execute('CREATE TABLE IF NOT EXISTS json (id TEXT, value TEXT)')
        self.sqlite.commit()


    def add(self, query: str = None, value = None) -> Cursor:
        """Add value to existing data"""
        if query == None or value == None:
            raise TypeError('Parameters for в add need to be configured')

        if isinstance(value, int) == False:
            raise TypeError('Value for add need to be a number')

        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() == None:
            self.db.execute("INSERT INTO json VALUES (?, ?)", [query, value])
            self.sqlite.commit()
            return True
        else:
            try:
                self.db.execute("SELECT value FROM json WHERE id = ?", [query])
                int(self.db.fetchone()[0])
            except:
                raise TypeError('Column value is not a number to add')
            


            
            self.db.execute("SELECT value FROM json WHERE id = ?", [query])
            self.db.execute("UPDATE json SET value = ? WHERE id = ?", [str(int(self.db.fetchone()[0]) + value), query])
            self.sqlite.commit()
            return True


    def set(self, query: str = None, value = None) -> Cursor:
        """Update data"""
        if query == None or value == None:
            raise TypeError('Parameters for set need to be configured')

        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() == None:
            if isinstance(value, int) == True:
                self.db.execute("INSERT INTO json VALUES (?, ?)", [query, value])
                self.sqlite.commit()
            else:
                self.db.execute("INSERT INTO json VALUES (?, ?)", [query, value])
                self.sqlite.commit()
            return True
        else:
            if isinstance(value, int) == True:
                self.db.execute("UPDATE json SET value = ? WHERE id = ?", [value, query])
                self.sqlite.commit()
            else:
                self.db.execute("UPDATE json SET value = ? WHERE id = ?", [value, query])
                self.sqlite.commit()
            return True


    def get(self, query: str = None) -> Any or None:
        """Get data"""
        if query == None:
            raise TypeError('Parameters for get need to be configured')

        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() == None:
            return None
        else:
            self.db.execute("SELECT value FROM json WHERE id = ?", [query])
            return self.db.fetchone()[0]

    def subtract(self, query: str = None, value = None) -> Cursor:
        """Subtract value from existing data"""
        if query == None or value == None:
            raise TypeError('Parameters for subtract need to be configured')

        if isinstance(value, int) == False:
            raise TypeError('Subtract value must to be int')

        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() == None:
            self.db.execute("INSERT INTO json VALUES (?, ?)", [query, value])
            self.sqlite.commit()
            return True
        else:
            try:
                self.db.execute("SELECT value FROM json WHERE id = ?", [query])
                int(self.db.fetchone()[0])
            except:
                raise TypeError('Column value is not a number to subtract')
            


            
            self.db.execute("SELECT value FROM json WHERE id = ?", [query])
            self.db.execute("UPDATE json SET value = ? WHERE id = ?", [str(int(self.db.fetchone()[0]) - value), query])
            self.sqlite.commit()
            return True


    def fetch(self, query: str = None) -> Any or None:
        """Get data"""
        if query == None:
            raise TypeError('Parameters for fetch need to be configured')

        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() == None:
            return None
        else:
            self.db.execute("SELECT value FROM json WHERE id = ?", [query])
            return self.db.fetchone()[0]

    def has(self, query: str = None) -> bool:
        """Check if data exists"""

        if query == None:
            raise TypeError('Parameters for has need to be configured')
        
        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() == None:
            return False
        else:
            return True

    def all(self) -> list:
        """Get all data in list"""
        arr = []
        self.db.execute("SELECT * FROM json")
        if self.db.execute("SELECT * FROM json") == None:
            return []


        self.db.execute("SELECT * FROM json")
        for a in self.db.fetchall():
            arr.append(a)

        return arr
    
    def delete(self, query: str = None) -> Cursor:
        """Delete data"""

        self.db.execute("SELECT value FROM json WHERE id = ?", [query])
        if self.db.fetchone() is None:
            raise TypeError('Cannot delete not existing data')
        else:
            self.db.execute("DELETE FROM json WHERE id = ?", [query])
            self.sqlite.commit()
            return True