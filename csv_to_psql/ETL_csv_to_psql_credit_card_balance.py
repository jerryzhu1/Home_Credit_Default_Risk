import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=54zhusiqi")
cur = conn.cursor()

# Build tabel
cur.execute("""
DROP TABLE IF EXISTS kaggle_credit_card_balance;
CREATE TABLE  kaggle_hcdr.credit_card_balance
(
    SK_ID_PREV numeric,
    SK_ID_CURR numeric,
    MONTHS_BALANCE numeric,
    AMT_BALANCE numeric,
    AMT_CREDIT_LIMIT_ACTUAL numeric,
    AMT_DRAWINGS_ATM_CURRENT text,
    AMT_DRAWINGS_CURRENT numeric,
    AMT_DRAWINGS_OTHER_CURRENT text,
    AMT_DRAWINGS_POS_CURRENT text,
    AMT_INST_MIN_REGULARITY numeric,
    AMT_PAYMENT_CURRENT text,
    AMT_PAYMENT_TOTAL_CURRENT numeric,
    AMT_RECEIVABLE_PRINCIPAL numeric,
    AMT_RECIVABLE numeric,
    AMT_TOTAL_RECEIVABLE numeric,
    CNT_DRAWINGS_ATM_CURRENT text,
    CNT_DRAWINGS_CURRENT numeric,
    CNT_DRAWINGS_OTHER_CURRENT text,
    CNT_DRAWINGS_POS_CURRENT text,
    CNT_INSTALMENT_MATURE_CUM numeric,
    NAME_CONTRACT_STATUS text,
    SK_DPD numeric,
    SK_DPD_DEF numeric
)
""")

cur.execute("""
    COPY  kaggle_hcdr.credit_card_balance(SK_ID_PREV, SK_ID_CURR, MONTHS_BALANCE, AMT_BALANCE, AMT_CREDIT_LIMIT_ACTUAL, AMT_DRAWINGS_ATM_CURRENT, AMT_DRAWINGS_CURRENT, AMT_DRAWINGS_OTHER_CURRENT, AMT_DRAWINGS_POS_CURRENT, AMT_INST_MIN_REGULARITY, AMT_PAYMENT_CURRENT, AMT_PAYMENT_TOTAL_CURRENT, AMT_RECEIVABLE_PRINCIPAL, AMT_RECIVABLE, AMT_TOTAL_RECEIVABLE, CNT_DRAWINGS_ATM_CURRENT, CNT_DRAWINGS_CURRENT, CNT_DRAWINGS_OTHER_CURRENT, CNT_DRAWINGS_POS_CURRENT, CNT_INSTALMENT_MATURE_CUM, NAME_CONTRACT_STATUS, SK_DPD, SK_DPD_DEF)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\credit_card_balance.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


