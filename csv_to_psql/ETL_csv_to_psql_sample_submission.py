import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=postgres user=postgres password=54zhusiqi")
cur = conn.cursor()

# Build table
cur.execute("""
DROP TABLE IF EXISTS kaggle_hcdr.sample_submission;
CREATE TABLE kaggle_hcdr.sample_submission
(
    SK_ID_CURR numeric,
    TARGET numeric
)
""")

cur.execute("""
    COPY kaggle_hcdr.sample_submission(SK_ID_CURR, TARGET)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\sample_submission.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()