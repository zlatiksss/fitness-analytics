import os
import time
import random
from datetime import datetime
import psycopg2
from psycopg2.extras import execute_values



DB_HOST = os.getenv("DB_HOST", "postgres")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "fitness")
DB_USER = os.getenv("DB_USER", "fitness_user")
DB_PASSWORD = os.getenv("DB_PASSWORD", "fitness_pass")


ACTIVITY_TYPES = ["rest", "walk", "run", "bike"]


def get_connection():
    """Wait for PostgreSQL to be ready"""
    while True:
        try:
            conn = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                dbname=DB_NAME,
                user=DB_USER,
                password=DB_PASSWORD,
            )
            conn.autocommit = True
            print("Connected to PostgreSQL")
            return conn
        except Exception as e:
            print(f"DB not ready: {e}")
            time.sleep(3)


def create_table(conn):
    create_sql = """
    CREATE TABLE IF NOT EXISTS fitness_events (
        id SERIAL PRIMARY KEY,
        ts TIMESTAMPTZ NOT NULL DEFAULT NOW(),
        user_id INT NOT NULL,
        steps INT NOT NULL,
        heart_rate INT NOT NULL,
        calories NUMERIC(6,2) NOT NULL,
        activity_type VARCHAR(20) NOT NULL
    );
    
    CREATE INDEX IF NOT EXISTS idx_ts ON fitness_events(ts);
    CREATE INDEX IF NOT EXISTS idx_user ON fitness_events(user_id);
    """
    
    with conn.cursor() as cur:
        cur.execute(create_sql)
    print("Table fitness_events created")


def generate_event(user_id: int):
    activity = random.choices(
        ACTIVITY_TYPES,
        weights=[0.3, 0.4, 0.2, 0.1],  
        k=1
    )[0]

    if activity == "rest":
        steps = random.randint(0, 10)
        heart_rate = random.randint(60, 80)
        calories = round(random.uniform(0.1, 2.0), 2)
    elif activity == "walk":
        steps = random.randint(50, 150)
        heart_rate = random.randint(80, 110)
        calories = round(random.uniform(3.0, 12.0), 2)
    elif activity == "run":
        steps = random.randint(150, 300)
        heart_rate = random.randint(120, 170)
        calories = round(random.uniform(15.0, 30.0), 2)
    else:  
        steps = 0
        heart_rate = random.randint(100, 150)
        calories = round(random.uniform(10.0, 25.0), 2)

    return {
        "ts": datetime.utcnow(),
        "user_id": user_id,
        "steps": steps,
        "heart_rate": heart_rate,
        "calories": calories,
        "activity_type": activity,
    }


def insert_batch(conn, events):
    sql = """
    INSERT INTO fitness_events (ts, user_id, steps, heart_rate, calories, activity_type)
    VALUES %s
    """
    values = [(e["ts"], e["user_id"], e["steps"], e["heart_rate"], e["calories"], e["activity_type"]) for e in events]
    
    with conn.cursor() as cur:
        execute_values(cur, sql, values)
    print(f"Inserted {len(events)} events at {datetime.utcnow().isoformat()[:19]}")


def main():
    print("Starting Fitness Data Generator...")
    conn = get_connection()
    create_table(conn)
    
    users = [1, 2, 3, 4, 5] 
    
    while True:
        try:
            batch = [generate_event(uid) for uid in users]
            insert_batch(conn, batch)
        except Exception as e:
            print(f"Error: {e}")
            conn.close()
            conn = get_connection()
        
        time.sleep(10) 


if __name__ == "__main__":
    main()
