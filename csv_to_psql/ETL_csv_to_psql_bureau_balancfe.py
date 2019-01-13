import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=54zhusiqi")
cur = conn.cursor()

# Build table
cur.execute("""
DROP TABLE IF EXISTS kaggle_hcdr.bureau_balance;
CREATE TABLE kaggle_hcdr.bureau_balance
(
    SK_ID_BUREAU numeric,
    MONTHS_BALANCE numeric,
    STATUS text
)
""")

cur.execute("""
    COPY kaggle_hcdr.bureau_balance(SK_ID_BUREAU, MONTHS_BALANCE, STATUS) 
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\bureau_balance.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()
