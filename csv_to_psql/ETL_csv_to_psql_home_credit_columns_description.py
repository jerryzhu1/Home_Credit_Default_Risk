import psycopg2

# password deleted
conn = psycopg2.connect("host=localhost dbname=home_credit_default_risk user=postgres password=")
cur = conn.cursor()

# Build table
cur.execute("""
CREATE TABLE home_credit_columns_description
(
    Record_index numeric,
    Table_name text,
    Row text,
    Description text,
    Special text
)
""")

cur.execute("""
    COPY home_credit_columns_description(Record_index, Table_name, Row, Description, Special)
    FROM 'D:\\Projects\\Home_Credit_Default_Risk\\data\\HomeCredit_columns_description.csv' DELIMITER ',' CSV HEADER;
""")

conn.commit()


