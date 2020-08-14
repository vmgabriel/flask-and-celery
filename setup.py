"""
Main Module, this run the app
"""

# Export Data
from src import server

# Configuration
from src.config import server as server_conf, broker

if __name__ == '__main__':
    print('broker - ', broker)

    server.run(
        host=server_conf.get('host'),
        port=server_conf.get('port'),
        debug=server_conf.get('debug'),
    )
