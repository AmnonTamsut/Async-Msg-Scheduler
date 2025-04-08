import base64
import json

from flask import Blueprint, request, jsonify, Response
from redis_client import ma_redis_client

echo_at_time_bp = Blueprint('echo_at_time', __name__)
health_check_bp = Blueprint('health_check', __name__)
SCHEDULED_MESSAGES = "scheduled messages"

@echo_at_time_bp.route('', methods=['POST'])
def echo_at_time():
    data = request.get_json()

    message = data['message']
    time = data['time']

    if not time or not message:
        return jsonify({'error': 'time and message is required'}), 400

    time = int(time)
    ma_redis_client.zadd(SCHEDULED_MESSAGES, {json.dumps({"time": time, "message": message}): time})

    return jsonify({"status": "Received your request" })

@health_check_bp.route('', methods=['GET'])
def health_check():
    base64_image = 'IC4uLiAgICAuLi4gICAuLi4uLi4gIC4uLi4uLiAgLi4uICAuLi4gICAjIyMjICAjIyMjIyggIyMjIyMjIyAlIyMgIyMsICAlIyMgIyMvLy4KIC4uLi4gICAuLi4gIC4uLiAgLi4gLi4uICAuLiAgLi4uICAuLi4gICAjIyMjICAoIyMgICAgICAjIyMgICAqJSUgJSMjICAjIyAgIyMgICAKIC4uLi4uIC4uLi4uIC4uLiAgLi4uLi4uICAuLi4gLi4uLiAuLi4gICUjJSMjKCAvIyMgICAgICAjIyMgICAsIyMgLiMjIC4jIyAgIyMgICAKIC4uLi4uIC4uLi4uIC4uLiAgLi4uLi4uICAuLi4gLi4uLi4uLi4gICMjIC4jIyAqIyMgICAgICAjIyMgICAqIyMgICMjICUjIyAgIyMgICAKIC4uLi4uLi4uLi4uIC4uLiAgLi4uLi4uICAuLi4gLi4uLi4uLi4gICMjIyMjIyAuIyMgICAgICAjIyMgICAoIyMgICMjLyMjLiAgIyMjIyAKIC4uIC4uLi4uIC4uIC4uLiAgLi4uLi4uICAuLi4gLi4gLi4uLi4gKiMjICAjIyAgIyMsICAgICAjIyMgICAlIyMgICgjIyMjICAgIyMgICAKIC4uIC4uLi4gIC4uLiAuLiAgLi4gIC4uICAuLiAuLi4gIC4uLi4gJSMjICAjIy8gIyMjICAgICAjIyMgICAlIyMgICAjIyMjICAgIyMgICAKLi4uICAuLi4gIC4uLiAuLi4uLi4gIC4uLi4uLiAuLi4gIC4uLi4gIyMsICAjIyMgIyMjIyMgICAjIyMgICAoIyMgICAjIyMvICAgIyMjIyM='
    image = base64.b64decode(base64_image).decode('utf-8')
    print(ma_redis_client.set('key', 'value'))
    print(ma_redis_client.get('key'))
    return Response(image, mimetype='text/plain')
