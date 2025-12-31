from flask import Flask
# Importing the logic blueprints
from routes.idea import idea_bp
from routes.roadmap import roadmap_bp
from routes.finance import finance_bp
from routes.customer import customer_bp

def create_app():
    # Initialize the Business Intelligence Engine
    app = Flask(__name__)

    # Registering endpoints for structured data analysis
    app.register_blueprint(idea_bp, url_prefix="/api/idea")
    app.register_blueprint(roadmap_bp, url_prefix="/api/roadmap")
    app.register_blueprint(finance_bp, url_prefix="/api/finance")
    app.register_blueprint(customer_bp, url_prefix="/api/customer")

    @app.route("/")
    def health():
        return {
            "status": "online",
            "engine": "FastEarn Strategic Planner",
            "message": "Data processing systems active"
        }

    return app

if __name__ == "__main__":
    app = create_app()
    # Running the production-ready server logic
    app.run(debug=True)
