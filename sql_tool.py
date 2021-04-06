import mariadb


class Database:
    def __init__(self, *args):
        self.args = args

    def run(self):
        try:
            conn = mariadb.connect(
                user="root",
                password="statbot3412++",
                host="localhost",
                port=3306,
                database="mysql"
            )
            cur = conn.cursor()
            try:
                for command in self.args:
                    cur.execute(command)
                    print(f'[SQL QUERY] {command}')
                conn.commit()
                print('Commit')
            except mariadb.Error as e:
                conn.rollback()
                print(f"ERROR: {e}")
            conn.close()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")

    def get(self):
        result = []
        try:
            conn = mariadb.connect(
                user="root",
                password="statbot3412++",
                host="localhost",
                port=3306,
                database="mysql"
            )
            cur = conn.cursor()

            try:
                for command in self.args:
                    cur.execute(command)
                    print(f'[SQL QUERY] {command}')
                    # print(*cur)
                    for row in cur:
                        result.append(row)
                    #return result
            except mariadb.Error as e:
                conn.rollback()
                print(f"ERROR: {e}")
            conn.close()
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
        return result

