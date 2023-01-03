## Bit.IO Wrapper Package
<hr>

### Setup
```
pip install git+https://github.com/AlexQ0807/bitdotiowrapper.git
```


### Example

```
from bitdotiowrapper.bitdotio_service import BitdotIOService

token = "<your_bitdotio_access_token>"
b_io = BitdotIOService(bitdotio_access_token=token)

db = "<username>/<database_name>"
command = "SELECT * FROM <db_table>"
res = b_io.query_data(db_name=db, query_command=command)

print(res)
```

```
from bitdotiowrapper.bitdotio_service import BitdotIOService

token = "<your_bitdotio_access_token>"
b_io = BitdotIOService(bitdotio_access_token=token)

db = "<username>/<database_name>"
command_create = '''
    CREATE TABLE Persons (
        PersonID int,
        LastName varchar(255),
        FirstName varchar(255),
        Address varchar(255),
        City varchar(255)
    );
'''
execute_success = b_io.execute_command(db_name=db, command=command_create)
if execute_success:
    print("Successfully Created DB")

command_drop = "DROP TABLE Persons;"
b_io.execute_command(db_name=db, command=command_drop)
if execute_success:
    print("Successfully Dropped DB")

```