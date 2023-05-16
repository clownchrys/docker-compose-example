import pymysql
from fastapi import APIRouter

router = APIRouter()

# conn = pymysql.connect(
#     user="root",
#     password="root",
#     host="mariadb",  # docker-compose: <service_name>
#     port=3306  # exposed port
# )
# cursor = conn.cursor()

@router.get("/get")
async def handle_getDummyData():
    sql = """
    SELECT * FROM example.tbl1;
    """
    # sql = "show databases;"

    cursor.execute(sql)
    rows = cursor.fetchall()

    result = {
        "data": [{"id": row[0], "value": row[1]} for row in rows]
    }

    return result
