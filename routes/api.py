from flask import FLask, request, jsonify
from models.activity import ActivityManager

api_bp = Blueprint("api", __name__)

activity_manager = ActivityManager()

@api_bp.route("/acctivities", methods=["GET"])

def get_activities():
    return jsonify(activity_manager.get_all())

def add_activity():
    data = request.get_json()
    title = data.get("title")
    category = data.get("category")

    if title and category:
        activity_manager.add(title, category)
        return jsonify({"status: succes"})
    return jsonify(({"status": "error", "message": "Missing data"})), 400
