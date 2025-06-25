from database.DB_connect import DBConnect
from model.country import Country


class DAO():

    @staticmethod
    def getAllCountries(year):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT co.StateAbb, co.CCode, co.StateNme 
                    from contiguity c, country co
                    where c.`year` <= %s
                    and c.state1no = co.CCode 
                    group by c.state1no ORDER BY StateAbb"""

        cursor.execute(query, (year, ))

        for row in cursor:
            result.append(Country(**row))

        cursor.close()
        conn.close()
        return result


    @staticmethod
    def getEdgesByYear(year, idMapCountries):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT c.state1no as id1, c.state2no as id2
                    from contiguity c 
                    where c.year < %s
                    and c.conttype = 1"""

        cursor.execute(query, (year,))

        for row in cursor:
            result.append((idMapCountries[row["id1"]], idMapCountries[row["id2"]]))

        cursor.close()
        conn.close()
        return result
