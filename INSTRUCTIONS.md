# CockroachDB learning

Following the tutorial here: https://www.cockroachlabs.com/docs/stable/build-a-python-app-with-cockroachdb-sqlalchemy.html?filters=local

## Init commands

Reference: https://www.cockroachlabs.com/docs/v21.1/install-cockroachdb-linux.html

```bash
curl https://binaries.cockroachdb.com/cockroach-v21.1.11.linux-amd64.tgz | tar -xz && sudo cp -i cockroach-v21.1.11.linux-amd64/cockroach /usr/local/bin/
mkdir -p /usr/local/lib/cockroach
cp -i cockroach-v21.1.11.linux-amd64/lib/libgeos.so /usr/local/lib/cockroach/
cp -i cockroach-v21.1.11.linux-amd64/lib/libgeos_c.so /usr/local/lib/cockroach/
which cockroach
# /usr/local/bin/cockroach
cockroach demo
SELECT ST_IsValid(ST_MakePoint(1,2));
#   st_isvalid
# --------------
# true
# (1 row)
```

## Steps

### Step 1: Start CockroachDB

```bash
cockroach start-single-node --advertise-addr 'localhost' --insecure
```

## Forgot to document everything else...