import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=54zhusiqi")
cur = conn.cursor()

# Build table
cur.execute("""
DROP TABLE IF EXISTS kaggle_pos_cash_balance;
CREATE TABLE  kaggle_hcdr.pos_cash_balance
(
    SK_ID_PREV numeric,
    SK_ID_CURR numeric,
    MONTHS_BALANCE numeric,
    CNT_INSTALMENT numeric,
    CNT_INSTALMENT_FUTURE numeric,
    NAME_CONTRACT_STATUS text,
    SK_DPD numeric,
    SK_DPD_DEF numeric
)
""")

cur.execute("""
    COPY kaggle_hcdr.pos_cash_balance(SK_ID_PREV, SK_ID_CURR, MONTHS_BALANCE, CNT_INSTALMENT, CNT_INSTALMENT_FUTURE, NAME_CONTRACT_STATUS, SK_DPD, SK_DPD_DEF)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\POS_CASH_balance.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


