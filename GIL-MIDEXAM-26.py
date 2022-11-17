from flask import Flask, jsonify, request

app = Flask(__name__)

userRecord = [
    {"Username": "User1", "token": "2001"},
    {"Username": "User2", "token": "2002"},
    {"Username": "User3", "token": "2003"},
]

heartbeatRecord = [
    {"heartrate_id": 1, "Date": "10-17-2022", "Heart rate": 60},
    {"heartrate_id": 2, "Date": "11-17-2022", "Heart rate": 70},
    {"heartrate_id": 3, "Date": "12-17-2022", "Heart rate": 80},
]


@app.route("/auth", methods=["POST"])
def auth_user():
    record = request.get_json()
    for i in range(0, len(userRecord)):
        if (
            record["Username"] == userRecord[i]["Username"]
            and record["token"] == userRecord[i]["token"]
        ):
            return True
    return False


@app.route("/insert", methods=["POST"])
def add_heart():
    if auth_user() == True:
        newRecord = request.get_json()
        heartbeatRecord.append(newRecord)
        return {"Records in the database": len(heartbeatRecord)}, 200
    else:
        return "User is not authorized", 404


@app.route("/update", methods=["POST"])
def update_heart():
    if auth_user() == True:
        record = request.get_json()
        for i in range(0, len(heartbeatRecord)):
            if record["heartbeat_id"] == heartbeatRecord[i]["heartbeat_id"]:
                heartbeatRecord[i]["Heart rate"] = record["Heart rate"]
                heartbeatRecord[i]["Date"] = record["Date"]
                heartbeatRecord[i]["heartbeat_id"] = record["heartbeat_id"]
                return jsonify(heartbeatRecord)
    else:
        return "User is not authorized" , 404


@app.route("/delete", methods=["DELETE"])
def delete_heart():
    if auth_user() == True:
        record = request.get_json()
        for i in range(0, len(heartbeatRecord)):
            if record["heartbeat_id"] == heartbeatRecord[i]["heartbeat_id"]:
                del heartbeatRecord[i]
                return jsonify(heartbeatRecord)
        return "This record does not exist", 404
    else:
        return "User is not authorized", 404


if __name__ == "__main__":
    app.run()