import mysql.connector
from models.User_role import RoleEnum
from models.User import User

class UserRepository: 

    def __init__(self):
        self.db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'root',
            'database': 'nodo_inmobiliario',
            'auth_plugin': 'mysql_native_password'
        }

    def _get_connection(self):
        return mysql.connector.connect(**self.db_config)

    def _execute_query(self, query, params=None, fetch_one=False):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(query, params or ())
        result = cursor.fetchone() if fetch_one else cursor.fetchall()
        cursor.close()
        conn.close()
        return result
    
    def _execute_non_query(self, non_query, params=None):
        conn = self._get_connection()
        cursor = conn.cursor()
        cursor.execute(non_query, params or ())
        conn.commit()
        returned_id = cursor.lastrowid
        cursor.close()
        conn.close()
        return returned_id

    def register_user(self, created_user: User):
        query = """
        INSERT INTO Users (user_id, name, surname, email, password, role,
        register_date, enabled)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        self._execute_non_query(query, (created_user.user_id,
                                    created_user.name,
                                    created_user.surname,
                                    created_user.email,
                                    created_user._password,
                                    created_user.role.value,
                                    created_user._register_date,
                                    created_user.enabled))


    def get_user_by_id(self, user_id: str):
        query = "SELECT * FROM Users WHERE user_id = %s"
        return self._execute_query(query, (user_id,), fetch_one=True)
    
    def get_user_by_email(self, user_email: str):
        query = "SELECT * FROM Users WHERE email = %s"
        return self._execute_query(query, (user_email,), fetch_one=True)

    def get_all_users_by_role(self, role: RoleEnum):
        query = "SELECT * FROM Users WHERE role = %s AND enabled = 1"
        return self._execute_query(query, (role.value,))
    
    def change_user_role(self, user_id: str, role: RoleEnum):
        query = "UPDATE Users SET role = %s WHERE user_id = %s"
        self._execute_non_query(query, (role.value, user_id))