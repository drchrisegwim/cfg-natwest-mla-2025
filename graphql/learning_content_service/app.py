from flask import Flask
from flask_graphql import GraphQLView
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from learning_content_service.schema import schema

app = Flask(__name__)
app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True # For easy testing in the browser
    )
)

if __name__ == '__main__':
    app.run(port=5001) # Run on a different port than the study-path-service