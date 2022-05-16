from fastapi import FastAPI, File, UploadFile, status, HTTPException
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
from databases import Database
import sqlalchemy


DATABASE_URL = "sqlite:///FieldInsepection.db"
APPOINTMENT_ID_PREFIX = "aj_"


metadata = sqlalchemy.MetaData()

database = Database(DATABASE_URL)

app = FastAPI(title="Field Insepection", docs_url="/docs", redoc_url="/redoc")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# data model for appointment detail
appointment = sqlalchemy.Table(
    "appointment",
    metadata,
    sqlalchemy.Column("appointmentId", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("inspection_date", sqlalchemy.String),
    sqlalchemy.Column("inspection_time", sqlalchemy.String),
    sqlalchemy.Column("year", sqlalchemy.String),
    sqlalchemy.Column("month", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_battery_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_battery_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_battery_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_battery_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_battery_cc_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_battery_cc_value_4", sqlalchemy.String),
    sqlalchemy.Column(
        "engineTransmission_engineoilLevelDipstick_value", sqlalchemy.String
    ),
    sqlalchemy.Column(
        "engineTransmission_engineOilLevelDipstick_cc_value_0", sqlalchemy.String
    ),
    sqlalchemy.Column("engineTransmission_engineOil", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_4", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_5", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_6", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_7", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_8", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineOil_cc_value_9", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_4", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_5", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_6", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_7", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_8", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_9", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engine_cc_value_10", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_coolant_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_coolant_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_coolant_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_coolant_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_coolant_cc_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineMounting_value", sqlalchemy.String),
    sqlalchemy.Column(
        "engineTransmission_engineMounting_cc_value_0", sqlalchemy.String
    ),
    sqlalchemy.Column("engineTransmission_engineSound_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineSound_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineSound_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineSound_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineSound_cc_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineSound_cc_value_4", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_engineSound_cc_value_5", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_exhaustSmoke_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_exhaustSmoke_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column(
        "engineTransmission_engineBlowByBackCompression_value", sqlalchemy.String
    ),
    sqlalchemy.Column(
        "engineTransmission_engineBlowByBackCompression_cc_value_0", sqlalchemy.String
    ),
    sqlalchemy.Column("engineTransmission_clutch_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_4", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_5", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_clutch_cc_value_6", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_gearShifting_value", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_gearShifting_cc_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_gearShifting_cc_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_gearShifting_cc_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_comments_value_0", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_comments_value_1", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_comments_value_2", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_comments_value_3", sqlalchemy.String),
    sqlalchemy.Column("engineTransmission_comments_value_4", sqlalchemy.String),
    sqlalchemy.Column("fuel_type", sqlalchemy.String),
    sqlalchemy.Column("odometer_reading", sqlalchemy.String),
    sqlalchemy.Column("rating_engineTransmission", sqlalchemy.String),
)
engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)

# connecting to db at strtup
@app.on_event("startup")
async def database_connect():
    await database.connect()

# closing db connection at end
@app.on_event("shutdown")
async def database_disconnect():
    await database.disconnect()

# route to upload data
@app.post("/upload_data")
async def upload(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        buffer = BytesIO(contents)
        df = pd.read_excel(buffer)
        buffer.close()
        df = df.fillna("")
        df = df.applymap(str)
        df.rename(
            columns={
                "inspection date": "inspection_date",
                "inspection time": "inspection_time",
            },
            inplace=True,
        )
        df.to_sql("appointment", engine, if_exists="append", index=False)
        return {"Message": "Data Uploaded"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e)
        )


# route to get record by appointment_id
@app.get("/get_record", status_code=status.HTTP_200_OK)
async def get_record_by_appointment_d(appointment_id: str):
    query = appointment.select().where(
        appointment.c.appointmentId == APPOINTMENT_ID_PREFIX + appointment_id
    )
    responses = await database.fetch_one(query)
    print(responses)
    if responses == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No record for appointment id: %s" % (appointment_id),
        )
    else:
        return responses
