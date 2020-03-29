from . import config_reader

def get_specific_helper():
    if config_reader.get_db_type() == 'postgres':
        from . import psql_database_helper
        return psql_database_helper
    else:
        from . import mysql_database_helper
        return mysql_database_helper
