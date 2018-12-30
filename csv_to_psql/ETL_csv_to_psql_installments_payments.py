import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=home_credit_default_risk user=postgres password=")
cur = conn.cursor()

# Build application_test
cur.execute("""
CREATE TABLE installments_payments
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
    COPY installments_payments(SK_ID_PREV, SK_ID_CURR, NUM_INSTALMENT_VERSION, NUM_INSTALMENT_NUMBER, DAYS_INSTALMENT, DAYS_ENTRY_PAYMENT, AMT_INSTALMENT, AMT_PAYMENT)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\installments_payments.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


