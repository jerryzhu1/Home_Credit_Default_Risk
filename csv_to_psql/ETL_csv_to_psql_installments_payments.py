import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=54zhusiqi")
cur = conn.cursor()

# Build table
cur.execute("""
DROP TABLE IF EXISTS kaggle_installments_payments;
CREATE TABLE kaggle_hcdr.installments_payments
(
    SK_ID_PREV numeric,
    SK_ID_CURR numeric,
    NUM_INSTALMENT_VERSION numeric,
    NUM_INSTALMENT_NUMBER numeric,
    DAYS_INSTALMENT numeric,
    DAYS_ENTRY_PAYMENT numeric,
    AMT_INSTALMENT numeric,
    AMT_PAYMENT numeric
)
""")

cur.execute("""
    COPY kaggle_hcdr.installments_payments(SK_ID_PREV, SK_ID_CURR, NUM_INSTALMENT_VERSION, NUM_INSTALMENT_NUMBER, DAYS_INSTALMENT, DAYS_ENTRY_PAYMENT, AMT_INSTALMENT, AMT_PAYMENT)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\installments_payments.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


