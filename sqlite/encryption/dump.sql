BEGIN TRANSACTION;
CREATE TABLE orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    amount REAL NOT NULL,
    order_date TEXT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(id)
);
INSERT INTO "orders" VALUES(1,1,100.5,'2025-03-01');
INSERT INTO "orders" VALUES(2,1,50.75,'2025-03-05');
INSERT INTO "orders" VALUES(3,2,200.0,'2025-03-02');
INSERT INTO "orders" VALUES(4,3,150.25,'2025-03-03');
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL
);
INSERT INTO "users" VALUES(1,'Alice Johnson','alice@example.com');
INSERT INTO "users" VALUES(2,'Bob Smith','bob@example.com');
INSERT INTO "users" VALUES(3,'Charlie Brown','charlie@example.com');
DELETE FROM "sqlite_sequence";
INSERT INTO "sqlite_sequence" VALUES('users',3);
INSERT INTO "sqlite_sequence" VALUES('orders',4);
COMMIT;
