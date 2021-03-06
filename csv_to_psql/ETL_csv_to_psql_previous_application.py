import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=54zhusiqi")
cur = conn.cursor()

# Build table
cur.execute("""
DROP TABLE IF EXISTS kaggle_hcdr.previous_application;
CREATE TABLE  kaggle_hcdr.previous_application
(
    SK_ID_PREV numeric,
    SK_ID_CURR numeric,
    NAME_CONTRACT_TYPE text,
    AMT_ANNUITY text,
    AMT_APPLICATION numeric,
    AMT_CREDIT numeric,
    AMT_DOWN_PAYMENT text,
    AMT_GOODS_PRICE text,
    WEEKDAY_APPR_PROCESS_START text,
    HOUR_APPR_PROCESS_START numeric,
    FLAG_LAST_APPL_PER_CONTRACT text,
    NFLAG_LAST_APPL_IN_DAY numeric,
    RATE_DOWN_PAYMENT text,
    RATE_INTEREST_PRIMARY text,
    RATE_INTEREST_PRIVILEGED text,
    NAME_CASH_LOAN_PURPOSE text,
    NAME_CONTRACT_STATUS text,
    DAYS_DECISION numeric,
    NAME_PAYMENT_TYPE text,
    CODE_REJECT_REASON text,
    NAME_TYPE_SUITE text,
    NAME_CLIENT_TYPE text,
    NAME_GOODS_CATEGORY text,
    NAME_PORTFOLIO text,
    NAME_PRODUCT_TYPE text,
    CHANNEL_TYPE text,
    SELLERPLACE_AREA numeric,
    NAME_SELLER_INDUSTRY text,
    CNT_PAYMENT text,
    NAME_YIELD_GROUP text,
    PRODUCT_COMBINATION text,
    DAYS_FIRST_DRAWING text,
    DAYS_FIRST_DUE text,
    DAYS_LAST_DUE_1ST_VERSION text,
    DAYS_LAST_DUE text,
    DAYS_TERMINATION text,
    NFLAG_INSURED_ON_APPROVAL text
)
""")

cur.execute("""
    COPY kaggle_hcdr.previous_application(SK_ID_PREV, SK_ID_CURR, NAME_CONTRACT_TYPE, AMT_ANNUITY, AMT_APPLICATION, AMT_CREDIT, AMT_DOWN_PAYMENT, AMT_GOODS_PRICE, WEEKDAY_APPR_PROCESS_START, HOUR_APPR_PROCESS_START, FLAG_LAST_APPL_PER_CONTRACT, NFLAG_LAST_APPL_IN_DAY, RATE_DOWN_PAYMENT, RATE_INTEREST_PRIMARY, RATE_INTEREST_PRIVILEGED, NAME_CASH_LOAN_PURPOSE, NAME_CONTRACT_STATUS, DAYS_DECISION, NAME_PAYMENT_TYPE, CODE_REJECT_REASON, NAME_TYPE_SUITE, NAME_CLIENT_TYPE, NAME_GOODS_CATEGORY, NAME_PORTFOLIO, NAME_PRODUCT_TYPE, CHANNEL_TYPE, SELLERPLACE_AREA, NAME_SELLER_INDUSTRY, CNT_PAYMENT, NAME_YIELD_GROUP, PRODUCT_COMBINATION, DAYS_FIRST_DRAWING, DAYS_FIRST_DUE, DAYS_LAST_DUE_1ST_VERSION, DAYS_LAST_DUE, DAYS_TERMINATION, NFLAG_INSURED_ON_APPROVAL)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\previous_application.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


