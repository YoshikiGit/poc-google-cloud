import functions_framework
import json
from datetime import datetime
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@functions_framework.http
def cf_hello_world(request):
    """
    基本的なHTTP関数のサンプル
    GET/POSTリクエストを処理
    """
    headers = {
        'Access-Control-Allow-Origin': '*',
        'Access-Control-Allow-Methods': 'GET, POST, OPTIONS',
        'Access-Control-Allow-Headers': 'Content-Type'
    }
    
    if request.method == 'OPTIONS':
        return ('', 204, headers)
    
    if request.method == 'GET':
        name = request.args.get('name', 'World')
        message = f"Hello, {name}!"
        
    elif request.method == 'POST':
        request_json = request.get_json()
        if request_json and 'name' in request_json:
            name = request_json['name']
        else:
            name = 'World'
        message = f"Hello, {name}! (from POST)"
    
    else:
        return ('Method not allowed', 405, headers)
    
    response_data = {
        'message': message,
        'timestamp': datetime.now().isoformat(),
        'method': request.method
    }
    
    logger.info(f"Request processed: {message}")
    
    return (json.dumps(response_data), 200, headers)
