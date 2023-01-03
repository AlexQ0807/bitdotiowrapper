from bitdotio import bitdotio
from bitdotio.utils import validate_token

class BitdotIOService:
    context = None

    def __init__(self, bitdotio_access_token: str):
        try:
            # Validate token format
            validate_token(bitdotio_access_token)

            self.context = bitdotio(access_token=bitdotio_access_token)

            # Try listing databases to determine if token auth is valid, invalid token will yield an exception
            self.list_databases()
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise e

    def list_databases(self):
        try:
            return self.context.list_databases()
        except Exception as e:
            raise e

    def query_data(self, db_name: str, query_command: str) -> list:
        ''' Use for SELECT SQL commands

        :param db_name:
        :param query_command:
        :return:
        '''
        conn = None
        cursor = None
        try:
            conn = self.context.get_connection(db_name)
            cursor = conn.cursor()
            cursor.execute(query_command)

            columns = [d[0] for d in cursor.description]

            row_list = []
            for rows in cursor:
                row_obj = {}
                for i, value in enumerate(rows):
                    row_obj[columns[i]] = value
                row_list.append(row_obj)

            return row_list

        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

    def execute_command(self, db_name: str, command: str) -> bool:
        ''' Use for non-SELECT SQL commands

        :param db_name:
        :param command:
        :return:
        '''
        rtn = False
        conn = None
        cursor = None
        try:
            conn = self.context.get_connection(db_name)
            cursor = conn.cursor()

            cursor.execute(command)
            conn.commit()
            rtn = True
        except Exception as e:
            raise e
        finally:
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close()

        return rtn
