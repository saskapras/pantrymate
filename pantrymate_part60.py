# === Stage 60: Add saved views for frequently used filters ===
# Project: PantryMate
import sqlite3

def create_saved_views(conn):
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS saved_views (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL, filters TEXT)")
    
    # Example: "Default" view with no specific filters
    cur.execute("INSERT OR IGNORE INTO saved_views (name, filters) VALUES ('Default', '{}')")
    
    # Example: "Expiring Soon" view - items expiring within 7 days
    cur.execute("""INSERT OR IGNORE INTO saved_views (name, filters) 
                   VALUES ('Expiring Soon', '{"date_filter": {"from": null, "to": "+7d"}}'""")
    
    # Example: "Needs Restock" view - items with quantity below threshold or zero
    cur.execute("INSERT OR IGNORE INTO saved_views (name, filters) VALUES ('Needs Restock', '{\"quantity_filter\": {\"max\": 1}}')")
    
    conn.commit()
