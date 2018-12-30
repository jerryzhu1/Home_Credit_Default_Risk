import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=home_credit_default_risk user=postgres password=")
cur = conn.cursor()

# Build table
cur.execute("""
CREATE TABLE sample_submission
(
    SK_ID_CURR numeric,
    TARGET numeric
)
""")

cur.execute("""
    COPY sample_submission(SK_ID_CURR, TARGET)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\sample_submission.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()