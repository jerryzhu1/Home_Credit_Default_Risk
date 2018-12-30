import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=home_credit_default_risk user=postgres password=")
cur = conn.cursor()

# Build table
cur.execute("""
CREATE TABLE bureau_balance
(
    SK_ID_BUREAU numeric,
    MONTHS_BALANCE text,
    STATUS text
)
""")

cur.execute("""
    COPY bureau_balance(SK_ID_BUREAU, MONTHS_BALANCE, STATUS) 
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\bureau_balance.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()
