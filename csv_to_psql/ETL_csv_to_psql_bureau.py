import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=home_credit_default_risk user=postgres password=")
cur = conn.cursor()

# Build application_test
cur.execute("""
CREATE TABLE bureau
(
    SK_ID_CURR numeric,
    SK_ID_BUREAU numeric,
    CREDIT_ACTIVE text,
    CREDIT_CURRENCY text,
    DAYS_CREDIT numeric,
    CREDIT_DAY_OVERDUE numeric,
    DAYS_CREDIT_ENDDATE text,
    DAYS_ENDDATE_FACT text,
    AMT_CREDIT_MAX_OVERDUE text,
    CNT_CREDIT_PROLONG numeric,
    AMT_CREDIT_SUM numeric,
    AMT_CREDIT_SUM_DEBT text,
    AMT_CREDIT_SUM_LIMIT text,
    AMT_CREDIT_SUM_OVERDUE numeric,
    CREDIT_TYPE text,
    DAYS_CREDIT_UPDATE numeric,
    AMT_ANNUITY text
)
""")

cur.execute("""
    COPY bureau(SK_ID_CURR, SK_ID_BUREAU, CREDIT_ACTIVE, CREDIT_CURRENCY, DAYS_CREDIT, CREDIT_DAY_OVERDUE, DAYS_CREDIT_ENDDATE, DAYS_ENDDATE_FACT, AMT_CREDIT_MAX_OVERDUE, CNT_CREDIT_PROLONG, AMT_CREDIT_SUM, AMT_CREDIT_SUM_DEBT, AMT_CREDIT_SUM_LIMIT, AMT_CREDIT_SUM_OVERDUE, CREDIT_TYPE, DAYS_CREDIT_UPDATE, AMT_ANNUITY)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\bureau.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


