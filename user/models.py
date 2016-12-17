from application import db # db global variable

from utilities.common import utc_ts_now as now # import utc time from utilities

class User(db.Document): #Document equivalent to rows in RDS.
    username = db.StringField(db_field="u", required=True) # db_field creates a field u instead of Username
    password = db.StringField(db_field="p", required=True)
    email = db.EmailField(db_field="e", required=True)
    first_name = db.StringField(db_field="fn", max_length=50)
    last_name = db.StringField(db_field="ln", max_length=50)
    created = db.IntField(db_field="c", default=now())
    




   
    
