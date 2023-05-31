from dbcon import PostgresConnection
import psycopg2.extras
import pandas as pd
class Query:
    def __init__(self):
        self.con = PostgresConnection().getConnection()
        print("Constructor called")

    def execute(self):
        con = PostgresConnection().getConnection()
        cur = con.cursor(cursor_factory=psycopg2.extras.DictCursor)
        query =       "SELECT DISTINCT specialist" \
                      "FROM doctorlistdb_schema.doctor_list_table" \
                      "GROUP BY specialist" \
                      "ORDER BY specialist"
        cur.execute(query)
        result = cur.fetchall()
        pd_data = pd.DataFrame(list(result), columns=['specialist'])
        pd_data = pd_data.dropna()
        #print(pd_data)
        return pd_data()

if __name__ == '__main__':
    q1 = Query()
    data = q1.execute()
    #print(data)