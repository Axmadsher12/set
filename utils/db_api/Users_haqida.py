import sqlite3

class Database:
    def __init__(self, path_to_db="main.db"):
        self.path_to_db=path_to_db

    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def Execute(self, sql:str, parameters: tuple=None, fetchone=False, fetchall=False, commit=False):
        if not parameters:
            parameters=()
            connection=self.connection
            connection.set_trace_callback(logger)
            curser=connection.cursor()
            data=None
            curser.execute(sql, parameters)

            if commit:
                connection.commit()
            if fetchall:
                data=curser.fetchall()
            if fetchone:
                data=curser.fetchone()
            connection.close()
            return data

    def create_table_users(self):
        sql="""
            CREATE TABLE mayfiles_teacher (id int NOT NULL
            Name varchar (255)NOT NULL,
            email varchar (255),
            language varchar(3),
            PRIMARY KEY (id)
            );"""
        self.Execute(sql,commit=True)

    @staticmethod
    def format_ards(sql, parametes: dict):
        sql += "AND".join([f"{item}=?" for item in parametes])
        return sql, tuple(parametes.values())

    def add_User(self, id: int, name: str, email:str = None, language:str = 'uz'):
        # SSQ_EXAMPLE = "INSERT INTO mayfiles_teacher(id, Name, email) VALUES(1,'John','John@gmail.com')"
        sql="""
        INSERT INTO nayfils_teacher(id, name, email, language) VALUES(?,?,?,?)
        """
        self.Execute(sql, parameters=(id, name,email,language),commit=True)

    def sellect_all_users(self):
        sql='''SELLECT * FROM myfils_teacher'''
        return self.Execute(sql, fetchall=True)

    def sellect_users(self, **kwargs):
        # SQL_EXAMPLE = "SELLECT * FROM myfiles_teacher where id=1 AND Name='John'"
        sql="SELLECT * FROM myfiles_teacher WHERE"
        sql,parametrs=self.format_ards(sql, kwargs)
        return self.Execute(sql, parameters=parametrs,fetchone=True)

    def count_users(self):
        return self.Execute("SELLECT COUNT(*) FROM myfiles_teacher;",fetchone=True)

    def update_user_email(self,email,id):
        sql=f"""UPDATE myfils_teacher SET email=? WHERE id=?"""
        return self.Execute(sql,parameters=(email,id),commit=True)

    def delete_users(self):
        self.Execute("DELETE FROM myfils_teacher WHERE TRUE",commit=True)

    'Foydalanilayotgan funksiyalar'
    "______________________________________________________________________________________________________________"
    def add_User_Kompyuterlar_123bot(self, Name: str,Telegram_id: int,Username: str=None):
        # SSQ_EXAMPLE = "INSERT INTO mayfiles_teacher(id, Name, email) VALUES(1,'John','John@gmail.com')"
        sql = """
        INSERT INTO BOT_Users(Name,Telegram_id,Username) VALUES(?, ?, ?)
        """
        self.Execute(sql, parameters=(Name,Telegram_id,Username), commit=True)

    def sellect_all_users_Kompyuterlar_123bot(self):
        sql='''SELLECT * FROM BOT_Users'''
        return self.Execute(sql, fetchall=True)
    "______________________________________________________________________________________________________________"


def logger(statement):
    print(f"""Executing:{statement}""")

