<!-- Run -->

Creating a new table in the database Postgres.

```sql

CREATE TABLE users
(
    id SERIAL PRIMARY KEY,
    email character varying(255),
    first_name character varying(255),
    last_name character varying(255),
)

```